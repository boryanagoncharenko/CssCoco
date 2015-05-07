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
        transformer._add_missing_tokens(s_expr)
        transformer._pull_up_whitespace(s_expr)
        transformer._split_up_whitespace(s_expr)
        return s_expr

    def __init__(self, s_expr):
        self._root = s_expr

    def _add_missing_tokens(self, s_expr):
        """
        The method adds missing values and omitted tokens to a given s_expr
        """
        if SExprTransformer._is_terminal_expr(s_expr):
            return

        SExprTransformer._add_value_transformation(s_expr)
        SExprTransformer._block_transformation(s_expr)
        SExprTransformer._declaration_transformation(s_expr)

        i = 1
        while i < len(s_expr):
            self._add_missing_tokens(s_expr[i])
            i += 1

    @staticmethod
    def _has_no_children(s_expr):
        return type(s_expr[1]) is not list

    @staticmethod
    def _is_terminal_expr(s_expr):
        return type(s_expr) is not list

    @staticmethod
    def _add_value_transformation(s_expr):
        if SExprTransformer._is_expr_without_value(s_expr):
            value = SExprTransformer._get_value(s_expr[0])
            s_expr.append(value)

    @staticmethod
    def _get_value(type_):
        if type_ not in SExprTransformer._type_to_value:
            raise NotImplementedError('Cannot infer value for token type')
        return SExprTransformer._type_to_value[type_]

    @staticmethod
    def _is_expr_without_value(s_expr):
        return len(s_expr) == 1

    @staticmethod
    def _block_transformation(s_expr):
        if s_expr[0] == 'block':
            s_expr.insert(1, ['symbol', '{'])
            s_expr.append(['symbol', '}'])

    @staticmethod
    def _declaration_transformation(s_expr):
        if s_expr[0] == 'declaration':
            s_expr.insert(2, ['symbol', ':'])

    # Whitespace nodes should not be the first of the last child of a node, except it if is the root node
    # Moreover spaces should bubble up until the condition above is met
    # The method relies on the assumption that gonzales does not produce two sibling spaces
    def _pull_up_whitespace(self, current, parent=None, position_in_parent=-1):
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
                return self._pull_up_whitespace(self._root)

            self._pull_up_whitespace(child, current, i)
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

    def _split_up_whitespace(self, s_expr):
        """
        The method breaks space token into \n, tab, space, indent
        """
        if self._has_no_children(s_expr):
            return
        index = 1
        while index < len(s_expr):
            child = s_expr[index]
            if child[0] == 's':
                del s_expr[index]
                spaces = self._get_whitespace_tokens(child)
                for offset, s in enumerate(spaces):
                    s_expr.insert(index+offset, s)
                # index += len(spaces)
            else:
                self._split_up_whitespace(child)
            index += 1

    def _get_whitespace_tokens(self, s_expr):
        result = []
        values = SExprTransformer._split_whitespace_value(s_expr[1])
        for index, value in enumerate(values):
            prev_value = None if index == 0 else values[index-1]
            type_ = SExprTransformer._get_whitespace_type(value, prev_value)
            result.append([type_, value])
        return result

    @staticmethod
    def _split_whitespace_value(str):
        result = []
        buffer = []
        for s in str:
            if len(buffer) == 0 or s == buffer[-1]:
                buffer.append(s)
            else:
                result.append(''.join(buffer))
                buffer = [s]
        if len(buffer) > 0:
            result.append(''.join(buffer))
        return result

    @staticmethod
    def _get_whitespace_type(value, prev_value):
        if value[0] == '\n':
            return 'newline'
        if prev_value and prev_value[0] == '\n':
            return 'indent'
        if value[0] == ' ':
            return 'space'
        if value[0] == '\t':
            return 'tab'
        else:
            raise NotImplementedError('Whitespace token with unknown value')

