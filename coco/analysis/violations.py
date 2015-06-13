import threading
import queue
import time
from multiprocessing.dummy import Pool as ThreadPool
import coco.ast.ast as ast
import coco.analysis.expressions as expr
import coco.visitor_decorator as vis
import coco.analysis.pattern_matcher as p_matcher


class Violations(object):
    def __init__(self):
        self._inner = []

    def add_violation(self, violation):
        self._inner.append(violation)

    def to_string(self):
        vs = []
        for v in self._inner:
            vs.append('\n')
            vs.append(v.to_string())
        return ''.join(vs)


class Violation(object):
    def __init__(self, message, line):
        self._message = message
        self._line = line

    def to_string(self):
        return ''.join(['Violation on line ', str(self._line), ': ', self._message])


class MyThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            m, arg = self.q.get()
            m(arg)
            print('processed!')
            # sock = urllib2.urlopen(host)
            # data = sock.read()
            self.q.task_done()


class ViolationsFinder(object):

    def __init__(self, tree):
        assert tree
        self._violations = Violations()
        self._tree = tree
        self._context = None
        self.q = queue.Queue()
        self.tot_time = 0

    @staticmethod
    def find(sheet, tree):
        finder = ViolationsFinder(tree)
        finder.visit(sheet)
        # print(finder._violations.to_string())
        print(len(finder._violations._inner))
        print(finder.tot_time)

    @vis.visitor(ast.ConventionSet)
    def visit(self, sheet):
        for c in sheet.contexts:
            self.visit(c)

    # def best_first_search(self, problem, f):
    #     f = memoize(f, 'f')
    #     node = Node(problem.initial)
    #     if problem.goal_test(node.state):
    #         return node
    #     frontier = PriorityQueue(min, f)
    #     frontier.append(node)
    #     explored = set()
    #     while frontier:
    #         node = frontier.pop()
    #         if problem.goal_test(node.state):
    #             return node
    #         explored.add(node.state)
    #         for child in node.expand(problem):
    #             if child.state not in explored and child not in frontier:
    #                 frontier.append(child)
    #             elif child in frontier:
    #                 incumbent = frontier[child]
    #                 if f(child) < f(incumbent):
    #                     del frontier[incumbent]
    #                     frontier.append(child)
    #     return None


    @vis.visitor(ast.SemanticContext)
    def visit(self, context):
        self._set_current_context(context)

        # pool = ThreadPool(4)
        # results = pool.map(self.visit, context.conventions)
        #
        # pool.close()
        # pool.join()

        # for i in range(len(context.conventions)):
        #     t = MyThread(self.q)
        #     t.daemon = True
        #     t.start()
        #
        for c in context.conventions:
            self.visit(c)
        #     self.q.put((self.visit,c))
        # self.q.join()

        # for convention in context.conventions:
        #     t = MyThread(self.q)
        #     t.daemon = True
        #     print('started')
        #     t.start()
        #
        # start = time.perf_counter()
        # # self.q.join()
        # print('time:',time.perf_counter() - start)

        self._reset_current_context()


    def _set_current_context(self, context):
        self._context = context

    def _reset_current_context(self):
        self._context = None

    def _get_current_context(self):
        return self._context

    num_worker_threads = 10

    # lock to serialize console output
    lock = threading.Lock()

    def do_work(self, item):
        time.sleep(.1) # pretend to do some lengthy work.
        # Make sure the whole print completes or threads can mix up output in one line.
        with self.lock:
            print(threading.current_thread().name, item)

    def worker(self):
        while True:
            item = self.q.get()
            if item is None:
                break
            self.do_work(item)
            self.q.task_done()


    @vis.visitor(ast.FindRequireConvention)
    def visit(self, find_require):
        filter_ = p_matcher.Filter(self._get_current_context().get_ignored_and_target_patterns())
        matcher = p_matcher.PatternMatcher(filter_)
        start = time.time()
        all_ = matcher.find_pattern_in_tree(self._tree, find_require.target_pattern)
        self.tot_time += time.time() - start
        for id_node_table in all_:
            constraint_filter = p_matcher.Filter(self._get_current_context().get_ignored_patterns())
            eval_context = expr.ConstraintContext(p_matcher.PatternMatcher(constraint_filter), id_node_table)
            is_fulfilled = expr.ExprEvaluator.evaluate(find_require.constraint, eval_context)
            if not is_fulfilled.value:
                anchor_desc = find_require.target_pattern.get_anchors()[0]
                anchor_node = id_node_table[anchor_desc]
                self._violations.add_violation(Violation(find_require.message, anchor_node.start_position.line))


    @vis.visitor(ast.ForbidConvention)
    def visit(self, forbid):
        filter_seq = p_matcher.Filter(self._get_current_context().get_ignored_and_target_patterns())
        matcher = p_matcher.PatternMatcher(filter_seq)
        for id_node_table in matcher.find_pattern_in_tree(self._tree, forbid.target_pattern):
            # anchor_desc = forbid.target_pattern.get_anchors()[0]
            # anchor_node = id_node_table[anchor_desc]
            self._violations.add_violation(Violation(forbid.message, 1)) # anchor_node.start_position.line))

    @vis.visitor(ast.FindForbidConvention)
    def visit(self, find_forbid):
        return expr.ExprEvaluator.evaluate(find_forbid.constraint, self._context[0])

