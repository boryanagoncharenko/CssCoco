from unittest import TestCase

from csscoco.lang.analysis import type_checker as checker
from csscoco.lang.ast import ast as ast


class TypeCheckerTests(TestCase):

    def wrap_convention_in_set(self, convention):
        return ast.ConventionSet([ast.SemanticContext([convention], [])])

    def test_diff_eq_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.EqualExpr(ast.StringExpr('test'), ast.IntegerExpr(5), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors_for_convention(a)) == 1

    def test_same_eq_argument_types_string(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.EqualExpr(ast.StringExpr('n'), ast.StringExpr('m'), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_same_eq_argument_types_list(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.EqualExpr(ast.ListExpr([]),
                                                                   ast.ListExpr([]), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_diff_ineq_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.NotEqualExpr(ast.StringExpr('t'), ast.IntegerExpr(5), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors_for_convention(a)) == 1

    def test_same_ineq_argument_types_string(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.NotEqualExpr(ast.StringExpr('n'), ast.StringExpr('m'), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_gr_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.GreaterThanExpr(ast.StringExpr('t'),
                                                                         ast.IntegerExpr(5), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors_for_convention(a)) == 1

    def test_same_gr_argument_types_integer(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.GreaterThanExpr(ast.IntegerExpr(2), ast.IntegerExpr(2), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_gr_eq_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.GreaterThanOrEqualExpr(ast.StringExpr('t'),
                                                                                ast.IntegerExpr(5), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors_for_convention(a)) == 1

    def test_same_gr_eq_argument_types_integer(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.GreaterThanOrEqualExpr(ast.IntegerExpr(2),
                                                                                ast.IntegerExpr(2), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_lt_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.LessThanExpr(ast.NodeTypeExpr('t'),
                                                                      ast.IntegerExpr(5), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_same_lt_argument_types_integer(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.LessThanExpr(ast.IntegerExpr(2), ast.IntegerExpr(2), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_lt_or_eq_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.LessThanOrEqualExpr(ast.NodeTypeExpr('t'),
                                                                             ast.IntegerExpr(5), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_same_lt_or_eq_argument_types_integer(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.LessThanOrEqualExpr(ast.IntegerExpr(2),
                                                                             ast.IntegerExpr(2), 3)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_in_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.InExpr(ast.ListExpr([ast.StringExpr('p')]),
                                                                ast.StringExpr('t'), '')), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_list_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.InExpr(ast.StringExpr('t'),
                                                                ast.ListExpr([ast.StringExpr('p')]))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_match_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.MatchExpr(ast.IntegerExpr(4),
                                                                   ast.StringExpr('t'), '')), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_match_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.MatchExpr(ast.StringExpr('t'),
                                                                   ast.StringExpr('m'))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_is_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.IsExpr(ast.IntegerExpr(4),
                                                                ast.StringExpr('t'), '')), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_is_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.IsExpr(ast.VariableExpr(''),
                                                                ast.NodeTypeExpr('m'))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_and_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.AndExpr(ast.BooleanExpr(True),
                                                                 ast.StringExpr('t'), '')), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_and_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.AndExpr(ast.BooleanExpr(True),
                                                                 ast.BooleanExpr(False))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_or_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.OrExpr(ast.BooleanExpr(True),
                                                                ast.StringExpr('t'), '')), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_or_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.OrExpr(ast.BooleanExpr(True),
                                                                ast.BooleanExpr(False))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_not_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.NotExpr(ast.StringExpr(''))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_not_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.NotExpr(ast.BooleanExpr(True))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_minus_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.UnaryMinusExpr(ast.StringExpr(''))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_minus_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.EqualExpr(ast.UnaryMinusExpr(ast.IntegerExpr(1)),
                                                                   ast.IntegerExpr(2))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_boolean_constraint(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.IntegerExpr(1)), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_list_with_diff_elements(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.EqualExpr(ast.ListExpr([ast.IntegerExpr(1), ast.StringExpr('')]),
                                                                   ast.IntegerExpr(2))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_contains_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.ContainsExpr(ast.VariableExpr.DEFAULT,
                                                                      ast.Node(ast.NodeTypeDescriptor(type_='a')))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_contains_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.ContainsExpr(ast.VariableExpr.DEFAULT, ast.IntegerExpr(2))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1

    def test_valid_contains_all_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.ContainsAllExpr(
                                              ast.VariableExpr.DEFAULT,
                                              ast.ListExpr([ast.Node(ast.NodeTypeDescriptor(type_='a'))]))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert not error_log.contain_errors()

    def test_invalid_contains_all_argument_types(self):
        a = ast.ForbidConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'),
                                          constraint=ast.ContainsAllExpr(
                                              ast.VariableExpr.DEFAULT,
                                              ast.ListExpr([ast.IntegerExpr(2)]))), '')
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1
        
    def test_undefined_variable(self):
        a = ast.FindRequireConvention(ast.Node(descriptor=ast.NodeTypeDescriptor(type_='property'), identifier='a'), '',
                                      constraint=ast.NotExpr(ast.VariableExpr('b')))
        convention_set = self.wrap_convention_in_set(a)
        error_log = checker.TypeChecker.check(convention_set)
        assert error_log.contain_errors()
        assert len(error_log.get_errors()) == 1