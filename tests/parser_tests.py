import src.parser as parser


def test_add_value_transformation_delim():
    s_expr = ['delim']
    expected = ['delim', ',']

    parser.SExprTransformer()._add_value_transformation(s_expr)

    assert s_expr == expected


def test_add_value_transformation_decldelim():
    s_expr = ['decldelim']
    expected = ['decldelim', ';']

    parser.SExprTransformer()._add_value_transformation(s_expr)

    assert s_expr == expected


def test_block_transformation():
    s_expr = ['block', ['decl', '...'], ['decl', '...']]
    expected = ['block', ['symbol', '{'], ['decl', '...'], ['decl', '...'], ['symbol', '}']]

    parser.SExprTransformer()._block_transformation(s_expr)

    assert s_expr == expected

def test_declaration_transformation():
    s_expr = ['declaration', ['property', '...'], ['value', '...']]
    expected = ['declaration', ['property', '...'], ['symbol', ':'], ['value', '...']]

    parser.SExprTransformer()._declaration_transformation(s_expr)

    assert s_expr == expected


def test_add_missing_tokens():
    s_expr = ['stylesheet', ['ruleset',
                            ['selector', ['simpleselector', ['ident', 'a']], ['delim'],
                            ['simpleselector', ['ident', 'p']]],
                            ['block', ['declaration', ['property', ['ident', 'font']], ['value', ['ident', 'black']]],
                            ['decldelim']]]]
    expected = ['stylesheet', ['ruleset',
                              ['selector', ['simpleselector', ['ident', 'a']], ['delim', ','],
                              ['simpleselector', ['ident', 'p']]],
                              ['block', ['symbol', '{'], ['declaration', ['property', ['ident', 'font']],
                              ['symbol', ':'], ['value', ['ident', 'black']]], ['decldelim', ';'], ['symbol', '}']]]]

    parser.SExprTransformer()._add_missing_tokens(s_expr)

    assert s_expr == expected


def test_whitespace_pull_up_first():
    s_expr = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p']]]]]
    expected = ['root', ['s', ' '], ['ch1', ['ch2',  ['ch3', ['p', 'p']]]]]

    parser.SExprTransformer()._pull_up_whitespace(s_expr)

    assert s_expr == expected


def test_whitespace_pull_up_last():
    s_expr = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p'], ['s', ' ']]]]]
    expected = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]

    parser.SExprTransformer()._pull_up_whitespace(s_expr)

    assert s_expr == expected


def test_whitespace_pull_up_both():
    s_expr = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p'], ['s', ' ']]]]]
    expected = ['root', ['s', ' '], ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]

    parser.SExprTransformer()._pull_up_whitespace(s_expr)

    assert s_expr == expected


def test_whitespace_pull_up_both_with_stop():
    s_expr = ['root', ['ch1', ['stopper', ''], ['ch2', ['ch3', ['s', ' '], ['p', 'p'], ['s', '\t']]], ['b', '']]]
    expected = ['root', ['ch1', ['stopper', ''], ['s', ' '], ['ch2', ['ch3', ['p', 'p']]], ['s', '\t'], ['b', '']]]

    parser.SExprTransformer()._pull_up_whitespace(s_expr)

    assert s_expr == expected


def test_split_up_whitespace_nl_space():
    s_expr = ['root', ['s', '\n    ']]
    expected = ['root', ['newline', '\n'], ['indent', '    ']]

    parser.SExprTransformer()._split_up_whitespace(s_expr)

    assert s_expr == expected


def test_split_up_whitespace_nl_tab():
    s_expr = ['root', ['s', '\n\t\t']]
    expected = ['root', ['newline', '\n'], ['indent', '\t\t']]

    parser.SExprTransformer()._split_up_whitespace(s_expr)

    assert s_expr == expected


def test_split_up_whitespace_space_tab_space_nl():
    s_expr = ['root', ['s', ' \t \n']]
    expected = ['root', ['space', ' '], ['tab', '\t'], ['space', ' '], ['newline', '\n']]

    parser.SExprTransformer()._split_up_whitespace(s_expr)

    assert s_expr == expected


def test_split_whitespace_value_nl():
    str = '\n    '
    expected = ['\n', '    ']
    result = parser.SExprTransformer()._split_whitespace_value(str)
    assert result == expected


def test_get_whitespace_type_space_after_nl():
    result = parser.SExprTransformer()._get_whitespace_type(' ', '\n')
    assert result == 'indent'


def test_get_whitespace_type_space_after_tab():
    result = parser.SExprTransformer()._get_whitespace_type(' ', '\t')
    assert result == 'space'


def test_get_whitespace_type_tab_after_nl():
    result = parser.SExprTransformer()._get_whitespace_type('\t', '\n')
    assert result == 'indent'