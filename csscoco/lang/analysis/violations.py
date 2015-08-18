import csscoco.lang.ast.ast as ast
import csscoco.lang.analysis.expressions as expr
import csscoco.lang.visitor_decorator as vis
import csscoco.lang.analysis.pattern_matcher as p_matcher


class Violation(object):
    def __init__(self, message, line):
        self.message = message
        self.line = line

    def to_string(self):
        return ''.join(['Violation on line ', str(self.line), ': ', self.message])


class ViolationLog(object):
    def __init__(self):
        self._inner = []

    def add_violation(self, violation):
        self._inner.append(violation)

    def number_of_violations(self):
        return len(self._inner)

    def to_string(self):
        if not self._inner:
            return 'No violations were discovered.'
        self._sort_violations()
        vs = []
        for v in self._inner:
            vs.append(v.to_string())
            vs.append('\n')
        return ''.join(vs[:-1])

    def _sort_violations(self):
        self._inner.sort(key=lambda v: v.line)


class ViolationsFinder(object):
    def __init__(self, tree):
        assert tree
        self._violations = ViolationLog()
        self._tree = tree
        self._context = None

    @staticmethod
    def find(convention_set, tree):
        finder = ViolationsFinder(tree)
        return finder._visit(convention_set)

    @vis.visitor(ast.ConventionSet)
    def _visit(self, sheet):
        for context in sheet.contexts:
            self._set_current_context(context)
            for conv in context.conventions:
                try:
                    css_patterns = self._get_matched_css_patterns(conv)
                    self._visit(conv, css_patterns)
                except expr.InvalidPropertyException as e:
                    return False, CocoRuntimeError(e.message)
        return True, self._violations

    @vis.visitor(ast.FindRequireConvention)
    def _visit(self, convention, matched_patterns):
        for css_pattern in matched_patterns:
            is_fulfilled = self._evaluate_constraint(convention.constraint, css_pattern)
            if not is_fulfilled.value:
                self._log_violation(convention, css_pattern)

    @vis.visitor(ast.ForbidConvention)
    def _visit(self, convention, matched_patterns):
        for css_pattern in matched_patterns:
            self._log_violation(convention, css_pattern)

    @vis.visitor(ast.FindForbidConvention)
    def _visit(self, convention, matched_patterns):
        for css_pattern in matched_patterns:
            is_fulfilled = self._evaluate_constraint(convention.constraint, css_pattern)
            if is_fulfilled.value:
                self._log_violation(convention, css_pattern)

    def _set_current_context(self, context):
        self._context = context

    def _get_matched_css_patterns(self, convention):
        ignored = self._context.ignored_patterns.copy()
        if convention.has_constraint():
            ignored += ViolationsHelper.get_additional_constraint(convention.constraint)
        matcher = p_matcher.PatternMatcher(p_matcher.Filter(ignored))
        return matcher.find_pattern_in_tree(self._tree, convention.pattern)

    def _evaluate_constraint(self, constraint, pattern):
        constraint_filter = p_matcher.Filter(self._context.ignored_patterns)
        eval_context = expr.ConventionConstraintContext(p_matcher.PatternMatcher(constraint_filter), pattern, self._tree)
        return expr.ExprEvaluator.evaluate(constraint, eval_context)

    def _log_violation(self, convention, css_pattern):
        anchor_desc = convention.pattern.get_anchors()[0]
        anchor_node = css_pattern[anchor_desc]
        self._violations.add_violation(Violation(convention.description, anchor_node.start_position.line))


class ViolationsHelper(object):
    @staticmethod
    def get_additional_constraint(e):
        result = []
        if ViolationsHelper()._visit(e):
            result.append(ViolationsHelper._get_sequence('space')),
            result.append(ViolationsHelper._get_sequence('newline')),
            result.append(ViolationsHelper._get_sequence('tab')),
        return result

    @staticmethod
    def _get_sequence(node_type):
        return ast.SequencePattern([ast.Node(ast.NodeTypeDescriptor.build_type(type_=node_type))])

    @vis.visitor(ast.BinaryExpr)
    def _visit(self, e):
        return self._visit(e.left) or self._visit(e.right)

    @vis.visitor(ast.UnaryExpr)
    def _visit(self, e):
        return self._visit(e.operand)

    @vis.visitor(ast.Expr)
    def _visit(self, e):
        return False

    @vis.visitor(ast.BeforeExpr)
    def _visit(self, e):
        return True

    @vis.visitor(ast.AfterExpr)
    def _visit(self, e):
        return True

    @vis.visitor(ast.BetweenExpr)
    def _visit(self, e):
        return True


class CocoRuntimeError(object):
    def __init__(self, message):
        self.message = message

    def to_string(self):
        return self.message