import src.ast as ast

def test_whitespace_pull_up_first():
    json = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p']]]]]
    print(json)
    transformer = ast.AstTransformer(json)
    transformer._traverse_for_whitespace(json)
    print(json)
    expected = ['root', ['s', ' '], ['ch1', ['ch2',  ['ch3', ['p', 'p']]]]]
    assert json == expected
    pass

def test_whitespace_pull_up_last():
    json = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p'], ['s', ' ']]]]]
    print(json)
    transformer = ast.AstTransformer(json)
    transformer._traverse_for_whitespace(json)
    print(json)
    expected = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]
    assert json == expected
    pass

def test_whitespace_pull_up_both():
    json = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p'], ['s', ' ']]]]]
    print(json)
    transformer = ast.AstTransformer(json)
    transformer._traverse_for_whitespace(json)
    print(json)
    expected = ['root', ['s', ' '], ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]
    assert json == expected
    pass