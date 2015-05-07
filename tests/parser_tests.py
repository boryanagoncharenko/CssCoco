import src.parser as parser


def whitespace_pull_up_first_test():
    s_expr = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p']]]]]
    expected = ['root', ['s', ' '], ['ch1', ['ch2',  ['ch3', ['p', 'p']]]]]

    transformer = parser.SExprTransformer(s_expr)
    transformer._pull_up_whitespace(s_expr)

    assert s_expr == expected


def test_whitespace_pull_up_last():
    s_expr = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p'], ['s', ' ']]]]]
    expected = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]

    transformer = parser.SExprTransformer(s_expr)
    transformer._pull_up_whitespace(s_expr)

    assert s_expr == expected


def test_whitespace_pull_up_both():
    s_expr = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p'], ['s', ' ']]]]]
    expected = ['root', ['s', ' '], ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]

    transformer = parser.SExprTransformer(s_expr)
    transformer._pull_up_whitespace(s_expr)

    assert s_expr == expected


def test_whitespace_pull_up_both_with_stop():
    s_expr = ['root', ['ch1', ['stopper', ''], ['ch2', ['ch3', ['s', ' '], ['p', 'p'], ['s', '\t']]], ['b', '']]]
    expected = ['root', ['ch1', ['stopper', ''], ['s', ' '], ['ch2', ['ch3', ['p', 'p']]], ['s', '\t'], ['b', '']]]

    transformer = parser.SExprTransformer(s_expr)
    transformer._pull_up_whitespace(s_expr)
    assert s_expr == expected


def test_split_up_whitespace_nl():
    str = '\n    '
    expected = ['\n', '    ']
    result = parser.SExprTransformer._split_whitespace_value(str)
    assert result == expected


def test_space_after_nl():
    result = parser.SExprTransformer._get_whitespace_type(' ', '\n')
    assert result == 'indent'


def test_space_after_tab():
    result = parser.SExprTransformer._get_whitespace_type(' ', '\t')
    assert result == 'space'


def test_tab_after_nl():
    result = parser.SExprTransformer._get_whitespace_type('\t', '\n')
    assert result == 'indent'