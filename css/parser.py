from subprocess import Popen, PIPE

GONZO_PATH = 'css/gonzales_parser.js'


class Parser(object):
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
    _type_to_value = {'decldelim': ';', 'delim': ','}

    @staticmethod
    def transform(s_expr):
        transformer = SExprTransformer()
        transformer._add_missing_tokens(s_expr)
        transformer._add_eof(s_expr)
        # transformer._push_down(s_expr)
        # transformer._pull_up_whitespace(s_expr)
        transformer._replace_descendant_selectors(s_expr)
        transformer._split_up_whitespace(s_expr)
        return s_expr

    def _add_missing_tokens(self, s_expr):
        """
        The method adds missing values and omitted tokens to a given s_expr
        """
        if self._is_terminal_expr(s_expr):
            return

        self._add_value_transformation(s_expr)
        self._block_transformation(s_expr)
        self._declaration_transformation(s_expr)

        i = 1
        while i < len(s_expr):
            self._add_missing_tokens(s_expr[i])
            i += 1

    def _add_eof(self, s_expr):
        s_expr.append(['eof', ''])

    def _has_no_children(self, s_expr):
        return type(s_expr[1]) is not list

    def _is_terminal_expr(self, s_expr):
        s = type(s_expr) is not list
        if s:
            pass
        return s

    def _add_value_transformation(self, s_expr):
        """
        Gonzales produces nodes that have type, but no value, e.g. delim and decldelim
        The method adds the omitted values, i.e. ['delim', ','] and ['decldelim', ';']
        """
        if self._is_expr_without_value(s_expr):
            type_ = s_expr[0]
            value = ['dummy', '']
            if type_ in self._type_to_value:
                value = self._type_to_value[type_]
            else:
                pass
            s_expr.insert(1, value)

    def _is_expr_without_value(self, s_expr):
        if len(s_expr) == 1:
            return True
        if type(s_expr[1]) is not list:
            return False
        # selector 'a, ' produces a simple selector that has one space as a child that is later pulled up
        if len(s_expr) == 2 and s_expr[1][0] == 's':
            return True
        return False

    def _block_transformation(self, s_expr):
        """
        Gonzales omits the symbols '{' and '}' in a block
        The method adds the two missing values to the block s-expr
        """
        if s_expr[0] == 'block':
            s_expr.insert(1, ['symbol', '{'])
            s_expr.append(['symbol', '}'])

    def _declaration_transformation(self, s_expr):
        """
        Gonzalez omits the ':' symbol between the property and value of a declaration
        The method adds the missing value to the declaration s-expr
        """
        if s_expr[0] == 'declaration':
            s_expr.insert(2, ['symbol', ':'])

    def _push_down(self, s_expr):
        has_transformed = self._push_down_declaration_delimiter(s_expr)
        if has_transformed:
            self._push_down(s_expr)

    def _push_down_declaration_delimiter(self, current):
        # TODO: extract a method that takes a transformation as a param and applies it
        if self._has_no_children(current):
            return False
        i = 1
        while i < len(current):
            child = current[i]
            if self._try_push_down(child, current, i):
                return True

            transformed = self._push_down_declaration_delimiter(child)
            if transformed:
                return True
            i += 1
        return False

    def _try_push_down(self, child, current, index):
        if current[0] == 'block' and child[0] == 'decldelim':
            previous_child = current[index - 1]
            if previous_child and previous_child[0] == 'declaration':
                current.pop(index)
                previous_child.append(child)
                return True
            else:
                raise NotImplementedError('Y U write ";" without declaration?')
        return False

    # Whitespace nodes should not be the first of the last child of a node, except it if is the root node
    # Moreover spaces should bubble up until the condition above is met
    # The method relies on the assumption that gonzales does not produce two sibling spaces
    def _pull_up_whitespace(self, s_expr):
        """
        Whenever a transformation is made the method aborts and starts traversing from the root
        """
        has_transformed = self._try_pull_up_whitespace(s_expr, None, -1)
        if has_transformed:
            self._pull_up_whitespace(s_expr)

    def _try_pull_up_whitespace(self, current, parent, position_in_parent):
        """
        Returns True right after it performs a whitespace pull up.
        If no transformations are made, returns False
        """
        if self._has_no_children(current):
            return False
        i = 1
        while i < len(current):
            child = current[i]
            if self._should_pull_up_child(child, current, parent, i):
                self._pull_up_child(current, parent, i, position_in_parent)
                return True

            transformed = self._try_pull_up_whitespace(child, current, i)
            if transformed:
                return True
            i += 1
        return False

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
                spaces = self._get_whitespace_expr(child)
                for offset, s in enumerate(spaces):
                    s_expr.insert(index + offset, s)
            else:
                self._split_up_whitespace(child)
            index += 1

    def _replace_descendant_selectors(self, s_expr):
        """
        This method transforms space in selectors into descendant selectors
        """
        self._node_transform(self._is_descendant_selector, self._descendant_transformer, s_expr)

    def _node_transform(self, selector, transformer, s_expr):
        if self._has_no_children(s_expr):
            return
        index = 1
        while index < len(s_expr):
            child = s_expr[index]
            if selector(s_expr, child, index):
                transformer(child)
            else:
                self._node_transform(selector, transformer, child)
            index += 1

    def _is_descendant_selector(self, s_expr, child, index):
        return s_expr[0] == 'simpleselector' and \
               child[0] == 's' and ' ' in child[1] and \
               index > 1 and index < len(s_expr) - 1 and \
               s_expr[index - 1][0] != 'combinator' and \
               s_expr[index + 1][0] != 'combinator'

    def _descendant_transformer(self, child):
        child[0] = 'descendant-selector'

    def _get_whitespace_expr(self, s_expr):
        result = []
        values = self._split_whitespace_value(s_expr[1])
        for index, value in enumerate(values):
            prev_value = None if index == 0 else values[index - 1]
            type_ = self._get_whitespace_type(value, prev_value)
            if type_ == 'indent':
                result.append([type_, value])
            else:
                for v in value:
                    result.append([type_, v])
        return result

    def _split_whitespace_value(self, str):
        result = []
        for value in self._get_whitespace_values(str):
            result.append(''.join(value))
        return result

    def _get_whitespace_values(self, str):
        buffer = []
        for s in str:
            if len(buffer) == 0 or s == buffer[-1]:
                buffer.append(s)
            else:
                yield buffer
                buffer = [s]
        if len(buffer) > 0:
            yield buffer

    def _get_whitespace_type(self, value, prev_value):
        char = value[0]
        if char == '\n':
            return 'newline'
        if prev_value and prev_value[0] == '\n':
            return 'indent'
        if char == ' ':
            return 'space'
        if char == '\t':
            return 'tab'
        raise NotImplementedError('Whitespace token with unknown value')

