from unittest import TestCase

from csscoco.lang.analysis import values as values
from csscoco.lang.ast import ast as ast


class EvaluationTests(TestCase):

    def test_in_bool_negative(self):
        l = values.List([values.Boolean.TRUE, values.Boolean.TRUE, values.Boolean.TRUE])
        r = values.Boolean.FALSE
        result = r.in_(l)
        assert not result.value

    def test_in_bool(self):
        l = values.List([values.Boolean.FALSE, values.Boolean.TRUE])
        r = values.Boolean.TRUE
        result = r.in_(l)
        assert result.value

    def test_in_str_negative(self):
        l = values.List([values.String('a'), values.String('b'), values.String('c')])
        r = values.String('d')
        result = r.in_(l)
        assert not result.value

    def test_in_str(self):
        l = values.List([values.String('a'), values.String('b'), values.String('c')])
        r = values.String('a')
        result = r.in_(l)
        assert result.value

    def test_in_dec_negative(self):
        l = values.List([values.Decimal(1.1), values.Decimal(2.2), values.Decimal(3.3)])
        r = values.Decimal(4.3)
        result = r.in_(l)
        assert not result.value

    def test_in_dec(self):
        l = values.List([values.Decimal(1.1), values.Decimal(2.2), values.Decimal(3.3)])
        r = values.Decimal(1.1)
        result = r.in_(l)
        assert result.value

    def test_in_int_negative(self):
        l = values.List([values.Integer(1), values.Integer(2), values.Integer(3)])
        r = values.Integer(4)
        result = r.in_(l)
        assert not result.value

    def test_in_int(self):
        l = values.List([values.Integer(1), values.Integer(2), values.Integer(1)])
        r = values.Integer(1)
        result = r.in_(l)
        assert result.value

    def test_less_than_equals_dec_int(self):
        l = values.Integer(3)
        r = values.Decimal(2.5)
        result = l.less_than_equals(r)
        assert not result.value

    def test_less_than_equals_dec_negative(self):
        l = values.Decimal(1.5)
        r = values.Decimal(2.5)
        result = l.less_than_equals(r)
        assert result.value

    def test_less_than_equals_dec(self):
        l = values.Decimal(2.5)
        r = values.Decimal(1.5)
        result = l.less_than_equals(r)
        assert not result.value

    def test_less_than_equals_int_negative(self):
        l = values.Integer(1)
        r = values.Integer(2)
        result = l.less_than_equals(r)
        assert result.value

    def test_less_than_equals_int(self):
        l = values.Integer(2)
        r = values.Integer(1)
        result = l.less_than_equals(r)
        assert not result.value

    def test_less_than_dec_int(self):
        l = values.Integer(3)
        r = values.Decimal(2.5)
        result = l.less_than(r)
        assert not result.value

    def test_less_than_dec_negative(self):
        l = values.Decimal(1.5)
        r = values.Decimal(2.5)
        result = l.less_than(r)
        assert result.value

    def test_less_than_dec(self):
        l = values.Decimal(2.5)
        r = values.Decimal(1.5)
        result = l.less_than(r)
        assert not result.value

    def test_less_than_int_negative(self):
        l = values.Integer(1)
        r = values.Integer(2)
        result = l.less_than(r)
        assert result.value

    def test_less_than_int(self):
        l = values.Integer(2)
        r = values.Integer(1)
        result = l.less_than(r)
        assert not result.value

    def test_greater_than_equals_dec_int(self):
        l = values.Integer(3)
        r = values.Decimal(2.5)
        result = l.greater_than_equals(r)
        assert result.value

    def test_greater_than_equals_dec_negative(self):
        l = values.Decimal(1.5)
        r = values.Decimal(2.5)
        result = l.greater_than_equals(r)
        assert not result.value

    def test_greater_than_equals_dec(self):
        l = values.Decimal(2.5)
        r = values.Decimal(1.5)
        result = l.greater_than_equals(r)
        assert result.value

    def test_greater_than_equals_int_negative(self):
        l = values.Integer(1)
        r = values.Integer(2)
        result = l.greater_than_equals(r)
        assert not result.value

    def test_greater_than_equals_int(self):
        l = values.Integer(2)
        r = values.Integer(1)
        result = l.greater_than_equals(r)
        assert result.value

    def test_greater_than_dec_int(self):
        l = values.Integer(3)
        r = values.Decimal(2.5)
        result = l.greater_than(r)
        assert result.value

    def test_greater_than_dec_negative(self):
        l = values.Decimal(1.5)
        r = values.Decimal(2.5)
        result = l.greater_than(r)
        assert not result.value

    def test_greater_than_dec(self):
        l = values.Decimal(2.5)
        r = values.Decimal(1.5)
        result = l.greater_than(r)
        assert result.value

    def test_greater_than_int_negative(self):
        l = values.Integer(1)
        r = values.Integer(2)
        result = l.greater_than(r)
        assert not result.value

    def test_greater_than_int(self):
        l = values.Integer(2)
        r = values.Integer(1)
        result = l.greater_than(r)
        assert result.value

    def test_not_eq_strings(self):
        l = values.String('a')
        r = values.String('a')
        result = l.not_equals(r)
        assert not result.value

    def test_not_eq_strings_negative(self):
        l = values.String('a')
        r = values.String('b')
        result = l.not_equals(r)
        assert result.value

    def test_not_eq_bool_negative(self):
        l = values.Boolean.TRUE
        r = values.Boolean.FALSE
        result = l.not_equals(r)
        assert result.value

    def test_not_eq_bool(self):
        l = values.Boolean.TRUE
        r = values.Boolean.TRUE
        result = l.not_equals(r)
        assert not result.value

    def test_not_eq_dec_int(self):
        l = values.Integer(1.5)
        r = values.Decimal(2.5)
        result = l.not_equals(r)
        assert result.value

    def test_not_eq_dec_negative(self):
        l = values.Decimal(1.5)
        r = values.Decimal(2.5)
        result = l.not_equals(r)
        assert result.value

    def test_not_eq_dec(self):
        l = values.Decimal(1.5)
        r = values.Decimal(1.5)
        result = l.not_equals(r)
        assert not result.value

    def test_not_eq_int_negative(self):
        l = values.Integer(1)
        r = values.Integer(2)
        result = l.not_equals(r)
        assert result.value

    def test_not_eq_int(self):
        l = values.Integer(1)
        result = l.not_equals(l)
        assert not result.value

    def test_eq_strings(self):
        l = values.String('a')
        r = values.String('a')
        result = l.equals(r)
        assert result.value

    def test_eq_strings_negative(self):
        l = values.String('a')
        r = values.String('b')
        result = l.equals(r)
        assert not result.value

    def test_eq_bool_negative(self):
        l = values.Boolean.TRUE
        r = values.Boolean.FALSE
        result = l.equals(r)
        assert not result.value

    def test_eq_bool(self):
        l = values.Boolean.TRUE
        r = values.Boolean.TRUE
        result = l.equals(r)
        assert result.value

    def test_eq_dec_int(self):
        l = values.Integer(1.5)
        r = values.Decimal(2.5)
        result = l.equals(r)
        assert not result.value

    def test_eq_dec_negative(self):
        l = values.Decimal(1.5)
        r = values.Decimal(2.5)
        result = l.equals(r)
        assert not result.value

    def test_eq_dec(self):
        l = values.Decimal(1.5)
        r = values.Decimal(1.5)
        result = l.equals(r)
        assert result.value

    def test_eq_int_negative(self):
        l = values.Integer(1)
        r = values.Integer(2)
        result = l.equals(r)
        assert not result.value

    def test_eq_int(self):
        l = values.Integer(1)
        result = l.equals(l)
        assert result.value

    def test_plus_dec(self):
        l = values.Decimal(10.5)
        result = l.unary_plus()
        assert result.value == 10.5

    def test_plus_int(self):
        l = values.Integer(5)
        result = l.unary_plus()
        assert result.value == 5

    def test_minus_dec(self):
        l = values.Decimal(10.5)
        result = l.unary_minus()
        assert result.value == -10.5

    def test_minus_int(self):
        l = values.Integer(5)
        result = l.unary_minus()
        assert result.value == -5

    def test_is_false_false(self):
        v = values.Boolean.FALSE
        assert v.is_false()

    def test_is_false_true(self):
        v = values.Boolean.TRUE
        assert not v.is_false()

    def test_not_true(self):
        v = values.Boolean.TRUE
        result = v.not_()
        assert not result.value

    def test_not_false(self):
        v = values.Boolean.FALSE
        result = v.not_()
        assert result.value

    def wrap_convention_in_set(self, convention):
        return ast.ConventionSet([ast.Context([convention], [])])
