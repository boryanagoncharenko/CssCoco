import os
import platform
from subprocess import Popen, PIPE


GONZO_PATH = os.path.dirname(os.path.realpath(__file__)) + '/gonzales_parser.js'
NODE_PATH = {
    "windows": "C:/Program Files/nodejs/node.exe",
    "linux2": "/usr/bin/nodejs",
    "darwin": "/usr/local/bin/node"
}


class Parser(object):
    @staticmethod
    def parse_css(css):
        encoded_css = css.encode('utf8')
        try:
            node_command = Parser._get_node_command()
            process = Popen([node_command, GONZO_PATH, encoded_css], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        except OSError:
            raise Exception('')

        out, err = process.communicate(input=encoded_css)
        if out:
            return out
        return err

    @staticmethod
    def _get_node_command():
        system = platform.system().lower()
        if system in NODE_PATH:
            return NODE_PATH[system]
        return 'node'


class SExprTransformer(object):
    def __init__(self):
        self._type_to_value = {'decldelim': ';', 'delim': ','}

    @staticmethod
    def transform(s_expr):
        transformer = SExprTransformer()
        transformer._add_missing_tokens(s_expr)
        transformer._add_eof(s_expr)
        transformer._push_down(s_expr)
        transformer._pull_up_whitespace(s_expr)
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
        self._function_transformation(s_expr)
        self._declaration_transformation(s_expr)
        self._rename_transformation(s_expr)

        i = 1
        while i < len(s_expr):
            self._add_missing_tokens(s_expr[i])
            i += 1

    def _add_eof(self, s_expr):
        s_expr.append(['eof', ''])

    def _has_children(self, s_expr):
        return type(s_expr[1]) is list

    def _is_terminal_expr(self, s_expr):
        s = type(s_expr) is not list
        return s

    def _add_value_transformation(self, s_expr):
        """
        Gonzales produces nodes that have type, but no value, e.g. delim and decldelim
        The method adds the omitted values, i.e. ['delim', ','] and ['decldelim', ';']
        """
        if self._is_expr_without_value(s_expr):
            type_ = s_expr[0]
            if type_ == 'block':
                return
            value = ['dummy', '']
            if type_ in self._type_to_value:
                value = self._type_to_value[type_]
            s_expr.insert(1, value)

    def _is_expr_without_value(self, s_expr):
        if len(s_expr) == 1:
            return True
        if type(s_expr[1]) is not list:
            return False
        # selector 'a, ' produces a simple selector that has one space as a child that is later pulled up
        if len(s_expr) == 2 and s_expr[1][0] == 's' :
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

    def _function_transformation(self, s_expr):
        if s_expr[0] == 'uri':
            s_expr.insert(1, ['opening-parenthesis', '('])
            s_expr.append(['closing-parenthesis', ')'])

    def _declaration_transformation(self, s_expr):
        """
        Gonzalez omits the ':' symbol between the property and value of a declaration
        The method adds the missing value to the declaration s-expr
        """
        if s_expr[0] == 'declaration':
            s_expr.insert(2, ['colon', ':'])

    def _rename_transformation(self, s_expr):
        if s_expr[0] == 'operator' and s_expr[1] == ',':
            s_expr[0] = 'comma'
        if s_expr[0] == 'dimension':
            s_expr[2][0] = 'unit'
        if s_expr[0] == 'combinator' and s_expr[1] == '>':
            s_expr[0] = 'child-selector'

    def _push_down(self, s_expr):
        """
        Gonzales puts the declaration delimiter ';' outside the declaration
        The method pushes the delimiter as the last child of the declaration
        """
        stack = [s_expr]
        while stack:
            current = stack.pop()
            if current[0] == 'selector' or not self._has_children(current):
                continue
            # The transformation does not require to reset the traversal
            # However, because the s_expr is transformed, there is no way to use a for loop below
            i = 1
            while i < len(current):
                child = current[i]
                if self._should_push_down(child, current, i):
                    self._perform_push_down(child, current, i)
                else:
                    stack.append(child)
                i += 1

    def _should_push_down(self, child, current, index):
        """
        Checks if a push down should be performed
        """
        if current[0] == 'block' and child[0] == 'decldelim':
            previous_child = current[index - 1]
            if previous_child and previous_child[0] == 'declaration':
                return True
        return False

    def _perform_push_down(self, child, current, index):
        """
        Makes the push down transformation
        """
        current.pop(index)
        current[index - 1].append(child)

    # Whitespace nodes should not be the first of the last child of a node, except it if is the root node
    # Moreover spaces should bubble up until the condition above is met
    # The method relies on the assumption that gonzales does not produce two sibling spaces
    def _pull_up_whitespace(self, s_expr):
        """
        Whenever a transformation is made the method aborts and starts traversing from the root
        """
        stack = NodePositionStack()
        stack.append(s_expr, -1)
        return self._try_pull(stack)

    def _try_pull(self, stack):
        if stack.len() == 0:
            return
        current = stack.get_current()
        if self._has_children(current):
            parent = stack.get_parent()
            i = 1
            while i < len(current):
                child = current[i]
                if self._should_pull_up_child(child, current, parent, i):
                    self._det_how_to_pull_up(stack, i)
                else:
                    stack.append(child, i)
                    self._try_pull(stack)
                    stack.pop()
                i += 1

    def _det_how_to_pull_up(self, stack, i):
        expr = -1
        position_in_parent = stack.get_position_in_parent()
        position = position_in_parent if i == 1 else position_in_parent + 1
        for j in range(stack.len()-2, 0, -1):
            current = stack[j]
            if self._is_first_child(position) or position == len(current[0]):
                expr = j
                pos = current[1]
                position = pos if position == 1 else pos + 1
            else:
                break
        space = stack[-1][0].pop(i)
        stack[expr-1][0].insert(position, space)
        if stack[expr][1] >= position:
            stack.update(expr, (stack[expr][0], stack[expr][1] + 1))

    def _should_pull_up_child(self, child, current, parent, i):
        if parent and child[0] == 's':
            return self._is_first_child(i) or self._is_last_child(i, current)
        return False

    def _pull_up_ws_recursively(self, stack):
        has_transformed, new_stack = self._try_pull_up_whitespace(stack)
        if self.should_continue(has_transformed, new_stack):
            self._pull_up_ws_recursively(new_stack.trim_last_element())

    def should_continue(self, has_transformed, new_stack):
        return new_stack.len() != 1 or has_transformed

    def _try_pull_up_whitespace(self, stack):
        """
        Returns True right after it performs a whitespace pull up.
        If no transformations are made, returns False
        """
        current = stack.get_current()
        if not self._has_children(current):
            return False, stack
        for i in range(1, len(current)):
            child = current[i]
            parent = stack.get_parent()
            position_in_parent = stack.get_position_in_parent()
            if self._should_pull_up_child(child, current, parent, i):
                self._pull_up_child(current, parent, i, position_in_parent)
                return True, stack

            stack.append(child, i)
            transformed, new_stack = self._try_pull_up_whitespace(stack)
            if transformed:
                return True, new_stack
            stack.pop()

        return False, stack

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
        if not self._has_children(s_expr):
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
        if not self._has_children(s_expr):
            return
        index = 1
        while index < len(s_expr):
            child = s_expr[index]
            if s_expr[0] == 'simpleselector' and child[0] == 'ident':
                child[0] = 'universal' if child[1] == '*' else 'tag'
            if selector(s_expr, child, index):
                transformer(child)
            else:
                self._node_transform(selector, transformer, child)
            index += 1

    def _is_descendant_selector(self, s_expr, child, index):
        return s_expr[0] == 'simpleselector' and child[0] == 's' and ' ' in child[1] and 1 < index < len(s_expr) - 1 \
            and s_expr[index - 1][0] != 'child-selector' and s_expr[index + 1][0] != 'child-selector'

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

    def _split_whitespace_value(self, string):
        result = []
        for value in self._get_whitespace_values(string):
            result.append(''.join(value))
        return result

    def _get_whitespace_values(self, string):
        buffer = []
        for s in string:
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


class NodePositionStack(object):
    def __init__(self):
        self.inner = []

    def __getitem__(self, item):
        return self.inner[item]

    def update(self, item, tuple_):
        self.inner[item] = tuple_

    def len(self):
        return len(self.inner)

    def append(self, node, position):
        self.inner.append((node, position))

    def pop(self):
        self.inner.pop()

    def get_current(self):
        return self.inner[-1][0]

    def get_parent(self):
        if len(self.inner) > 1:
            return self.inner[-2][0]
        return None

    def get_position_in_parent(self):
        return self.inner[-1][1]

    def trim_last_element(self):
        if len(self.inner) > 1:
            self.inner = self.inner[:-1]
        return self
