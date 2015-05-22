import src.descriptors as descriptors
import src.sequences as seqs
import coco.ast.ast_node as ast
import coco.ast.expressions as expr
import coco.ast.markers as markers


class Sheet(ast.AstNode):

    def __init__(self, contexts):
        self.contexts = contexts

    def get_children(self):
        return self.contexts


class Context(ast.AstNode):

    def __init__(self, statements):
        self.statements = statements

    def get_children(self):
        return self.statements

    def get_condition_ignore_sequences(self):
        pass

    def get_requirement_ignore_sequences(self):
        pass


class WhitespaceContext(Context):

    def __init__(self, statements):
        Context.__init__(self, statements)

    def get_condition_ignore_sequences(self):
        return self.get_requirement_ignore_sequences() + [seqs.SiblingSequence([descriptors.NodeDescriptor.WHITESPACE])]

    def get_requirement_ignore_sequences(self):
        return [seqs.SiblingSequence([descriptors.NodeDescriptor.INDENT]),
                seqs.SiblingSequence([descriptors.NodeDescriptor.COMMENT]),
                seqs.SiblingSequence([descriptors.SimpleDescriptor(type_='newline'),
                               descriptors.SimpleDescriptor(type_='comment')])]

    def is_marker_in_condition(self, marker):
        return marker.is_css_marker()


class CommentsContext(Context):

    def __init__(self, statements):
        Context.__init__(self, statements)

    def get_condition_ignore_sequences(self):
        return self.get_requirement_ignore_sequences()
               # [seqs.Sequence([descriptors.NegativeSimpleDescriptor(type_='comment')])]

    def get_requirement_ignore_sequences(self):
        return [seqs.SiblingSequence([descriptors.NodeDescriptor.INDENT])]

    def is_marker_in_condition(self, marker):
        return True
        # return type(marker) is not markers.CommentMarker


class Statement(ast.AstNode):
    """
    Abstract class
    """
    pass


class Declaration(Statement):
    pass


class Rule(Statement):

    def __init__(self, markers_list):
        self.markers_list = markers_list

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers_list:
            s = ''.join([s, m.pretty_print(level+1)])
        return s


class RequireRule(Rule):

    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class ForbidRule(Rule):

    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class AllowRule(Rule):

    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class MarkerSequence(ast.AstNode):

    def __init__(self, markers):
        self.markers = markers

    def __getitem__(self, x):
        return self.markers[x]

    def __iter__(self):
        return iter(self.markers)

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers:
            s = ''.join([s, m.pretty_print(level + 1)])
        return s


class MarkerSequenceVariation(ast.AstNode):

    def __init__(self, marker_sequences):
        self.marker_sequences = marker_sequences

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for sequence in self.marker_sequences:
            s = ''.join([s, sequence.pretty_print(level + 1)])
        return s

MarkerSequenceVariation.NONE = MarkerSequenceVariation([])


class AstBuilder(object):

    @staticmethod
    def build(ply_tree):
        builder = AstBuilder()
        return builder.__build_sheet(ply_tree)

    def __build_sheet(self, ply_sheet):
        contexts = []
        for c in ply_sheet.select('context'):
            contexts.append(self.__build_context(c))
        return Sheet(contexts)

    def __build_context(self, ply_context):
        statements = []
        for stat in ply_context.select('rule'):
            rule = self.__build_rule(stat)
            statements.append(rule)

        name = ply_context.select('context > *')[0].lower()
        if name == 'whitespace':
            return WhitespaceContext(statements)
        if name == 'comments':
            return CommentsContext(statements)

        raise NotImplementedError('Other contexts are not implemented yet')

    def __build_rule(self, ply_rule):
        children = ply_rule.select('rule > *')
        markers = self._build_markers(children[1:])
        name = children[0].lower()

        if name == 'require':
            return RequireRule(markers)

        if name == 'forbid':
            return ForbidRule(markers)

        if name == 'allow':
            return AllowRule(markers)

        raise NotImplementedError('Other rules are not implemented yet')

    def _build_markers(self, marker_list):
        result = []
        for m in marker_list:
            result.append(self._build_marker(m))
        return result

    def _generate_possible_sequences(self, option_list, res):
        if len(option_list) == 0:
            yield MarkerSequence(list(res))
        else:
            first_option = option_list[0]
            for option in first_option:
                res.append(option)
                yield from self._generate_possible_sequences(option_list[1:], res)
                del res[-1]

    def _build_marker(self, ply_node):
        if self._is_or_expr(ply_node):
            return self._handle_or_expr(ply_node)

        if self._is_parenthesis_expr(ply_node):
            return self._handle_parenthesis_expr(ply_node)

        if self._is_terminal_expr(ply_node):
            return self._handle_terminal_expr(ply_node)

        raise NotImplementedError('Unknown marker')

    def _is_or_expr(self, ply_node):
        return len(ply_node.tail) == 3 and \
            ply_node.tail[1] == 'or'

    def _handle_or_expr(self, ply_node):
        left = self._build_marker(ply_node.tail[0])
        right = self._build_marker(ply_node.tail[2])

        option_list = []
        if type(left) is expr.OrExpression:
            option_list = option_list + left.markers_list
        else:
            option_list.append(left)

        if type(right) is expr.OrExpression:
            option_list = option_list + right.markers_list
        else:
            option_list.append(right)

        return expr.OrExpression(option_list)

    def _is_parenthesis_expr(self, ply_node):
        return ply_node.tail[0] == '(' and \
            ply_node.tail[-1] == ')'

    def _handle_parenthesis_expr(self, ply_node):
        elements = ply_node.tail[1:-1]
        markers = []
        if len(elements) == 1:
            result = self._build_marker(elements[0])
            if type(result) in [expr.OrExpression, expr.MarkersExpression]:
                return result

        for element in elements:
            markers.append(self._build_marker_two(element))
        return expr.MarkersExpression(markers)

    def _is_terminal_expr(self, ply_node):
        return len(ply_node.tail) == 1

    def _handle_terminal_expr(self, ply_node):
        marker = self._build_marker_two(ply_node.tail[0])
        return expr.MarkersExpression([marker])

    def _build_marker_two(self, ply_node):
        name = ply_node.select('name > *')[0]
        if name == 'rule':
            return markers.RuleMarker()
        if name == 'declaration':
            return markers.DeclarationMarker()
        if name == 'selector':
            return markers.SelectorMarker()
        if name == 'block':
            return markers.BlockMarker()
        if self._is_string(name):
            return markers.SymbolMarker(name[1:-1])
        if name == 'property':
            return markers.PropertyMarker()
        if name == 'value':
            return markers.ValueMarker()
        if name == 'eof':
            return markers.EofMarker()
        if name == 'comment':
            return markers.CommentMarker()
        if name == 'csv-comma':
            return markers.CsvCommaMarker()
        if name == 'selector-comma':
            return markers.SelectorCommaMarker()


        repetitions = self._get_repetition(ply_node)
        if name == 'whitespace':
            return markers.WhitespaceMarker(repetitions)
        if name == 'space':
            return markers.SpaceMarker(repetitions)
        if name == 'newline':
            return markers.NewlineMarker(repetitions)
        if name == 'tab':
            return markers.TabMarker(repetitions)

        raise NotImplementedError('Other css marker are not implemented yet')

    def _get_repetition(self, ply_node):
        reps = ply_node.select('repetition > *')
        if len(reps) == 0:
            return 1
        if reps[1] == '*':
            return -1
        return int(reps[1])

    def _is_string(self, str):
        return len(str) > 1 and str[0] == '"' and str[-1] == '"'
