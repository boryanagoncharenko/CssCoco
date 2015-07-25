import csscoco.lang.ast.ast as ast
import csscoco.lang.analysis.expressions as expr
import csscoco.lang.visitor_decorator as vis
import csscoco.lang.analysis.pattern_matcher as p_matcher


class Violation(object):
    def __init__(self, message, line):
        self._message = message
        self._line = line

    def to_string(self):
        return ''.join(['Violation on line ', str(self._line), ': ', self._message])


class ViolationLog(object):
    def __init__(self):
        self._inner = []

    def add_violation(self, violation):
        self._inner.append(violation)

    def number_of_violations(self):
        return len(self._inner)

    def to_string(self):
        if not self._inner:
            return ''
        vs = []
        for v in self._inner:
            vs.append('\n')
            vs.append(v.to_string())
        return ''.join(vs)


class ViolationsFinder(object):
    def __init__(self, tree):
        assert tree
        self._violations = ViolationLog()
        self._tree = tree
        self._context = None

    @staticmethod
    def find(sheet, tree):
        finder = ViolationsFinder(tree)
        finder.visit(sheet)
        return finder._violations

    @vis.visitor(ast.ConventionSet)
    def visit(self, sheet):
        for context in sheet.contexts:
            self._set_current_context(context)
            for conv in context.conventions:
                css_patterns = self.get_matched_css_patterns(conv)
                self.visit(conv, css_patterns)

    @vis.visitor(ast.FindRequireConvention)
    def visit(self, convention, matched_patterns):
        for css_pattern in matched_patterns:
            is_fulfilled = self._evaluate_constraint(convention.constraint, css_pattern)
            if not is_fulfilled.value:
                self._log_violation(convention, css_pattern)

    @vis.visitor(ast.ForbidConvention)
    def visit(self, convention, matched_patterns):
        for css_pattern in matched_patterns:
            self._log_violation(convention, css_pattern)

    @vis.visitor(ast.FindForbidConvention)
    def visit(self, convention, matched_patterns):
        for css_pattern in matched_patterns:
            is_fulfilled = self._evaluate_constraint(convention.constraint, css_pattern)
            if is_fulfilled.value:
                self._log_violation(convention, css_pattern)

    def _set_current_context(self, context):
        self._context = context

    def get_matched_css_patterns(self, convention):
        ignored = self._context.get_ignored_patterns().copy()
        if convention.has_constraint():
            ignored += ViolationsHelper.get_additional_constraint(convention.constraint)
        matcher = p_matcher.PatternMatcher(p_matcher.Filter(ignored))
        return matcher.find_pattern_in_tree(self._tree, convention.pattern)

    def _evaluate_constraint(self, constraint, pattern):
        constraint_filter = p_matcher.Filter(self._context.get_ignored_patterns())
        eval_context = expr.ConventionConstraintContext(p_matcher.PatternMatcher(constraint_filter), pattern)
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
            result.append(ast.SequencePattern([ast.Node(ast.NodeTypeDescriptor.build_type(type_='space'))])),
            result.append(ast.SequencePattern([ast.Node(ast.NodeTypeDescriptor.build_type(type_='newline'))])),
            result.append(ast.SequencePattern([ast.Node(ast.NodeTypeDescriptor.build_type(type_='tab'))]))
        return result

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