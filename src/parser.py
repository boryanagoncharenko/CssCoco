from subprocess import Popen, PIPE

GONZO_PATH = 'src/gonzales_parser.js'


class ParseWrapper(object):

    @staticmethod
    def parse_css(css):
        encoded_css = css.encode('utf8')
        try:
            process = Popen(['node', GONZO_PATH, encoded_css], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        except OSError:
            raise Exception('')

        out, err = process.communicate(input=encoded_css)
        if out:
            return out
        return err


class SExprTransformer(object):
    # Shall I transform the ast or the json
    # Maybe I need to keep a reference in the child to its parent and its index
    # In this case, transforming the json and building the ast as a last step would be best

    _type_to_value = {'decldelim': ';', 'delim': ','}

    @staticmethod
    def transform(s_expr):
        transformer = SExprTransformer(s_expr)
        transformer._traverse(s_expr)
        transformer._traverse_for_whitespace(s_expr)
        return s_expr

    def __init__(self, s_expr):
        self._root = s_expr

    def _traverse(self, s_expr):
        """
        The method adds missing values and omitted tokens to a given s_expr
        """
        if SExprTransformer._is_terminal_expr(s_expr):
            return

        self._add_value_transformation(s_expr)
        self._block_transformation(s_expr)
        self._declaration_transformation(s_expr)

        i = 1
        while i < len(s_expr):
            self._traverse(s_expr[i])
            i += 1

    @staticmethod
    def _has_no_children(s_expr):
        return type(s_expr[1]) is not list

    @staticmethod
    def _is_terminal_expr(s_expr):
        return type(s_expr) is not list

    def _add_value_transformation(self, s_expr):
        if SExprTransformer._is_expr_without_value(s_expr):
            value = self._get_value(s_expr[0])
            s_expr.append(value)

    def _get_value(self, type_):
        if type_ not in SExprTransformer._type_to_value:
            raise NotImplementedError('Cannot infer value for token type')
        return self._type_to_value[type_]

    @staticmethod
    def _is_expr_without_value(s_expr):
        return len(s_expr) == 1

    def _block_transformation(self, s_expr):
        if s_expr[0] == 'block':
            s_expr.insert(1, ['symbol', '{'])
            s_expr.append(['symbol', '}'])

    def _declaration_transformation(self, s_expr):
        if s_expr[0] == 'declaration':
            s_expr.insert(2, ['symbol', ':'])

    # Whitespace nodes should not be the first of the last child of a node, except it if is the root node
    # Moreover spaces should bubble up until the condition above is met
    # The method heavily relies on the assumption that gonzales does not produce two sibling spaces
    def _traverse_for_whitespace(self, current, parent=None, position_in_parent=-1):
        """
        The method aborts and starts traversing from the root whenever a transformation is made
        """
        if self._has_no_children(current):
            return
        i = 1
        while i < len(current):
            child = current[i]
            if self._should_pull_up_child(child, current, parent, i):
                self._pull_up_child(current, parent, i, position_in_parent)
                return self._traverse_for_whitespace(self._root)

            self._traverse_for_whitespace(child, current, i)
            i += 1

    def _should_pull_up_child(self, child, current, parent, i):
        if parent is not None and child[0] == 's':
            return self._is_first_child(i) or self._is_last_child(i, current)
        return False

    def _is_first_child(self, i):
        return i == 1

    def _is_last_child(self, i, current):
        return i == len(current) - 1

    def _pull_up_child(self, current, parent, i, pos_in_parent):
        target_position = pos_in_parent if i == 1 else pos_in_parent + 1
        space = current.pop(i)
        parent.insert(target_position, space)