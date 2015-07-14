from unittest import TestCase
import csscoco.css.parser as parser


class CssParser(TestCase):
    
    def test_add_value_transformation_delim(self):
        s_expr = ['delim']
        expected = ['delim', ',']
    
        parser.SExprTransformer()._add_value_transformation(s_expr)
        assert s_expr == expected
    
    def test_add_value_transformation_decldelim(self):
        s_expr = ['decldelim']
        expected = ['decldelim', ';']
    
        parser.SExprTransformer()._add_value_transformation(s_expr)
        assert s_expr == expected

    def test_block_transformation(self):
        s_expr = ['block', ['decl', '...'], ['decl', '...']]
        expected = ['block', ['symbol', '{'], ['decl', '...'], ['decl', '...'], ['symbol', '}']]
    
        parser.SExprTransformer()._block_transformation(s_expr)
        assert s_expr == expected
    
    def test_declaration_transformation(self):
        s_expr = ['declaration', ['property', '...'], ['value', '...']]
        expected = ['declaration', ['property', '...'], ['colon', ':'], ['value', '...']]
    
        parser.SExprTransformer()._declaration_transformation(s_expr)
        assert s_expr == expected
    
    def test_add_missing_tokens(self):
        s_expr = ['stylesheet', ['ruleset',
                                ['selector', ['simpleselector', ['ident', 'a']], ['delim'],
                                ['simpleselector', ['ident', 'p']]],
                                ['block', ['declaration', ['property', ['ident', 'font']], ['value', ['ident', 'black']]],
                                ['decldelim']]]]
        expected = ['stylesheet', ['ruleset',
                                  ['selector', ['simpleselector', ['ident', 'a']], ['delim', ','],
                                  ['simpleselector', ['ident', 'p']]],
                                  ['block', ['symbol', '{'], ['declaration', ['property', ['ident', 'font']],
                                  ['colon', ':'], ['value', ['ident', 'black']]], ['decldelim', ';'], ['symbol', '}']]]]
    
        parser.SExprTransformer()._add_missing_tokens(s_expr)
        assert s_expr == expected
    
    def test_push_down(self):
        s_expr = ['block', ['declaration', ['property', 'color']], ['decldelim', ';']]
        expected = ['block', ['declaration', ['property', 'color'], ['decldelim', ';']]]

        parser.SExprTransformer()._push_down(s_expr)
        assert s_expr == expected

    def test_push_down_multiple_declarations(self):
        s_expr = ['block',
                  ['declaration', ['property', 'color']], ['decldelim', ';'],
                  ['declaration', ['value', 'red']], ['decldelim', ';']]
        expected = ['block',
                    ['declaration', ['property', 'color'], ['decldelim', ';']],
                    ['declaration', ['value', 'red'], ['decldelim', ';']]]

        parser.SExprTransformer()._push_down(s_expr)
        assert s_expr == expected

    def test_push_down_multiple_rules(self):
        s_expr = ['stylesheet',
                  ['rule', ['block', ['declaration', ['property', 'color']], ['decldelim', ';']]],
                  ['rule', ['block', ['declaration', ['value', 'red']], ['decldelim', ';']]]]
        expected = ['stylesheet',
                    ['rule', ['block', ['declaration', ['property', 'color'], ['decldelim', ';']]]],
                    ['rule', ['block', ['declaration', ['value', 'red'], ['decldelim', ';']]]]]

        parser.SExprTransformer()._push_down(s_expr)
        assert s_expr == expected

    def test_whitespace_pull_up_multiple(self):
        s_expr = ['root',
                  ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p']]]],
                  ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p']]]]
                  ]
        expected = ['root',
                    ['s', ' '], ['ch1', ['ch2',  ['ch3', ['p', 'p']]]],
                    ['s', ' '], ['ch1', ['ch2',  ['ch3', ['p', 'p']]]]
                    ]

        parser.SExprTransformer()._pull_up_whitespace(s_expr)
        assert s_expr == expected

    def test(self):
        s_expr = ['ruleset',
                  ['block', ['symbol', '{'], ['s', '\n    '],
                   ['declaration', ['property', ['ident', 'color']],
                    ['colon', ':'], ['value', ['s', ' '], ['ident', 'red']], ['decldelim', ';']], ['s', '\n    '],
                   ['declaration', ['property', ['ident', 'margin']],
                    ['colon', ':'], ['value', ['s', ' '], ['dimension', ['number', '5'], ['ident', 'px']]],
                    ['decldelim', ';']], ['s', '\n'], ['symbol', '}']]]

        expected = ['ruleset',
                  ['block', ['symbol', '{'], ['s', '\n    '],
                   ['declaration', ['property', ['ident', 'color']],
                    ['colon', ':'], ['s', ' '], ['value', ['ident', 'red']], ['decldelim', ';']], ['s', '\n    '],
                   ['declaration', ['property', ['ident', 'margin']],
                    ['colon', ':'], ['s', ' '], ['value', ['dimension', ['number', '5'], ['ident', 'px']]],
                    ['decldelim', ';']], ['s', '\n'], ['symbol', '}']]]

        parser.SExprTransformer()._pull_up_whitespace(s_expr)
        assert s_expr == expected

    def test_whitespace_pull_up_first(self):
        s_expr = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p']]]]]
        expected = ['root', ['s', ' '], ['ch1', ['ch2',  ['ch3', ['p', 'p']]]]]
    
        parser.SExprTransformer()._pull_up_whitespace(s_expr)
        assert s_expr == expected

    def test_whitespace_pull_up_last(self):
        s_expr = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p'], ['s', ' ']]]]]
        expected = ['root', ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]
    
        parser.SExprTransformer()._pull_up_whitespace(s_expr, )
        assert s_expr == expected

    def test_whitespace_pull_up_both(self):
        s_expr = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p'], ['s', ' ']]]]]
        expected = ['root', ['s', ' '], ['ch1', ['ch2', ['ch3', ['p', 'p']]]],['s', ' ']]
    
        parser.SExprTransformer()._pull_up_whitespace(s_expr)
        assert s_expr == expected

    def test_whitespace_pull_up_both_with_stop(self):
        s_expr = ['root', ['ch1', ['stopper', ''], ['ch2', ['ch3', ['s', ' '], ['p', 'p'], ['s', '\t']]], ['b', '']]]
        expected = ['root', ['ch1', ['stopper', ''], ['s', ' '], ['ch2', ['ch3', ['p', 'p']]], ['s', '\t'], ['b', '']]]
    
        parser.SExprTransformer()._pull_up_whitespace(s_expr)
        assert s_expr == expected

    def test_split_up_whitespace_nl_space(self):
        s_expr = ['root', ['s', '\n    ']]
        expected = ['root', ['newline', '\n'], ['indent', '    ']]
    
        parser.SExprTransformer()._split_up_whitespace(s_expr)
        assert s_expr == expected

    def test_split_up_whitespace_nl_tab(self):
        s_expr = ['root', ['s', '\n\t\t']]
        expected = ['root', ['newline', '\n'], ['indent', '\t\t']]
    
        parser.SExprTransformer()._split_up_whitespace(s_expr)
        assert s_expr == expected

    def test_split_up_whitespace_space_tab_space_nl(self):
        s_expr = ['root', ['s', ' \t \n']]
        expected = ['root', ['space', ' '], ['tab', '\t'], ['space', ' '], ['newline', '\n']]
    
        parser.SExprTransformer()._split_up_whitespace(s_expr)
        assert s_expr == expected

    def test_split_whitespace_value_nl(self):
        str = '\n    '
        expected = ['\n', '    ']
        result = parser.SExprTransformer()._split_whitespace_value(str)
        assert result == expected
    
    def test_get_whitespace_type_space_after_nl(self):
        result = parser.SExprTransformer()._get_whitespace_type(' ', '\n')
        assert result == 'indent'

    def test_get_whitespace_type_space_after_tab(self):
        result = parser.SExprTransformer()._get_whitespace_type(' ', '\t')
        assert result == 'space'
    
    def test_get_whitespace_type_tab_after_nl(self):
        result = parser.SExprTransformer()._get_whitespace_type('\t', '\n')
        assert result == 'indent'