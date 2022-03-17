import unittest
from core import SuperNumber, SuperNumbers
import props
import props_supernumbers
import span


class SuperNumberTests(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(SuperNumber(1, 3, 2)), "<1 mod 3 | 2>")

    def test_mult(self):
        # Trivial case: when alpha is zero and we get nowhere near the mod,
        # x * y = x + y
        self.assertEqual(
            SuperNumber(1, 10, 0) * SuperNumber(2, 10, 0), SuperNumber(3, 10, 0)
        )
        # Trivial case: when we get nowhere near the mod (but alpha is
        # nonzero), x * y = x + y + alpha*x*y
        # In this case, that's 1 + 2 + 2*1*2 = 3 + 4 = 7
        self.assertEqual(
            SuperNumber(1, 10, 2) * SuperNumber(2, 10, 2), SuperNumber(7, 10, 2)
        )
        # Test going over the mod with no alpha
        # <4 mod 5> * <2 mod 5> = (4 + 2) mod 5 = 1
        self.assertEqual(
            SuperNumber(4, 5, 0) * SuperNumber(2, 5, 0), SuperNumber(1, 5, 0)
        )
        # Aaaaand the whole shebang
        # <3 mod 5 | 2> * <4 mod 5 | 2>
        # = (3 + 4 + 2*3*4) mod 5
        # = (7 + 24) mod 5
        # = 31 mod 5
        # = 1
        self.assertEqual(
            SuperNumber(3, 5, 2) * SuperNumber(4, 5, 2), SuperNumber(1, 5, 2)
        )

    def test_mult_for_different_mod_or_mult(self):
        x = SuperNumber(2, 4, 3)
        y = SuperNumber(2, 3, 3)
        z = SuperNumber(2, 4, 2)
        with self.assertRaisesRegex(
            Exception, "Modulus and multiplier are not the same"
        ):
            x * y
        with self.assertRaisesRegex(
            Exception, "Modulus and multiplier are not the same"
        ):
            x * z

    def test_eq(self):
        x = SuperNumber(2, 4, 3)
        y = SuperNumber(2, 4, 3)
        self.assertTrue(x == y)

    def test_eq_for_different_mod_or_mult(self):
        x = SuperNumber(1, 3, 2)
        y = SuperNumber(1, 2, 2)
        z = SuperNumber(1, 3, 1)
        self.assertFalse(x == y)
        self.assertFalse(x == z)

    def test_eq_for_non_supernumber(self):
        x = SuperNumber(2, 3, 4)
        y = 1
        with self.assertRaises(AttributeError):
            x == y

    def test_init_with_large_obj(self):
        x = SuperNumber(5, 3, 0)
        self.assertEqual(x, SuperNumber(2, 3, 0))

    def test_init_with_large_alpha(self):
        x = SuperNumber(2, 3, 5)
        self.assertEqual(x, SuperNumber(2, 3, 2))

    def test_init_obj_not_int(self):
        with self.assertRaisesRegex(Exception, "Num is not an int"):
            SuperNumber("a", 3, 5)

    def test_init_mod_not_int(self):
        with self.assertRaisesRegex(TypeError, "Modulus is not an int"):
            SuperNumber(2, "a", 5)

    def test_init_mult_not_int(self):
        with self.assertRaisesRegex(TypeError, "Multiplier is not an int"):
            SuperNumber(2, 3, "a")

    def test_init_obj_less_than_zero(self):
        with self.assertRaisesRegex(Exception, "Num is not greater than zero"):
            SuperNumber(-1, 3, 5)

    def test_init_mult_less_than_zero(self):
        with self.assertRaisesRegex(Exception, "Multiplier is not greater than zero"):
            SuperNumber(2, 3, -1)

    def test_init_mod_less_than_zero(self):
        with self.assertRaisesRegex(Exception, "Modulus is not greater than zero"):
            SuperNumber(2, -1, 5)


class SuperNumbersTests(unittest.TestCase):
    def test_init_mod_not_int(self):
        with self.assertRaisesRegex(TypeError, "Modulus is not an int"):
            SuperNumbers("a", 5)

    def test_init_mult_not_int(self):
        with self.assertRaisesRegex(TypeError, "Multiplier is not an int"):
            SuperNumbers(3, "a")

    def test_init_mult_less_than_zero(self):
        with self.assertRaisesRegex(Exception, "Multiplier is not greater than zero"):
            SuperNumbers(3, -1)

    def test_init_mod_less_than_zero(self):
        with self.assertRaisesRegex(Exception, "Modulus is not greater than zero"):
            SuperNumbers(-1, 5)

    def test_size(self):
        self.assertEqual(SuperNumbers(5, 2).size(), 5)

    def test_large_size(self):
        self.assertEqual(SuperNumbers(10 ** 100, 2).size(), 10 ** 100)

    def test_str(self):
        self.assertEqual(str(SuperNumbers(3, 2)), "<SuperNumbers mod 3 | 2>")

    def test_large_str(self):
        self.assertEqual(
            str(SuperNumbers(10 ** 100, 4)), f"<SuperNumbers mod {10**100} | 4>"
        )

    def test_iteration(self):
        expected = [SuperNumber(0, 3, 0), SuperNumber(1, 3, 0), SuperNumber(2, 3, 0)]
        self.assertEqual([x for x in SuperNumbers(3, 0)], expected)

    def test_repeated_iteration(self):
        expected = [SuperNumber(0, 3, 0), SuperNumber(1, 3, 0), SuperNumber(2, 3, 0)]
        sns = SuperNumbers(3, 0)
        self.assertEqual([x for x in sns], expected)
        self.assertEqual([x for x in sns], expected)

    def test_iteration_lazy(self):
        sns = SuperNumbers(10 ** 100, 0)
        self.assertEqual(next(iter(sns)), SuperNumber(0, 10 ** 100, 0))

    def test_eq(self):
        self.assertEqual(SuperNumbers(3, 2), SuperNumbers(3, 2))

    def test_neq(self):
        self.assertNotEqual(SuperNumbers(3, 2), SuperNumbers(4, 2))
        self.assertNotEqual(SuperNumbers(3, 2), SuperNumbers(3, 1))

    def test_init_with_large_alpha(self):
        self.assertEqual(SuperNumbers(3, 5), SuperNumbers(3, 2))

    def test_iter_below(self):
        sns = SuperNumbers(10, 2)
        expected = [SuperNumber(0, 10, 2), SuperNumber(1, 10, 2), SuperNumber(2, 10, 2)]
        self.assertEqual(expected, list(sns.iter_below(SuperNumber(3, 10, 2))))

    def test_iter_below_mismatched(self):
        with self.assertRaisesRegex(Exception, "is not compatible"):
            SuperNumbers(3, 2).iter_below(SuperNumber(0, 3, 1))


# Tests for both implementations of props
#
# note: this can't inherit from unittest.TestCase, or it'll be treated as a
# test case in its own right. Instead, the concrete children inherit from
# both this class and TestCase. Approach from
# https://stackoverflow.com/a/49545467
class PropsTests:
    def test_commutative(self):
        # trivial case: where mod is 2 and alpha is 0.
        # 0 * 0 = 0 + 0 + 0 mod 2 = 0
        # 0 * 1 = 0 + 1 + 0 mod 2 = 1
        # 1 * 0 = 1 + 0 + 0 mod 2 = 1
        # 1 * 1 = 1 + 1 + 0 mod 2 = 0
        self.assertTrue(self.props.IsCommutativeSuperNumberMultiplication(2, 0))
        self.assertTrue(self.props.IsCommutativeSuperNumberMultiplication(3, 4))

    def test_associative(self):
        # trivial case: where mod is 1 and alpha is 0
        # 0 * (0 * 0) = 0 + 0 + 0 mod 1 = 0
        # (0 * 0) * 0 = 0 + 0 + 0 mod 1 = 0
        self.assertTrue(self.props.IsCommutativeSuperNumberMultiplication(1, 0))
        self.assertTrue(self.props.IsAssociativeSuperNumberMultiplication(4, 5))

    def test_idempotent(self):
        # trivial case: where mod is 1 and alpha is 0
        # 0 * 0 = 0 + 0 + 0 mod 1 = 0
        self.assertTrue(self.props.HasSuperNumberIdempotentProperty(1, 0))
        # not idempotent:
        self.assertFalse(self.props.HasSuperNumberIdempotentProperty(3, 1))
        self.assertTrue(self.props.HasSuperNumberIdempotentProperty(2, 1))

    def test_super_roots_of_one(self):
        # trivial case: "Hint" from the spec: <0 mod 1 | 0> is a super root of one
        self.assertEqual(self.props.SuperRootsOfOne(1, 0), [SuperNumber(0, 1, 0)])

        self.assertEqual(self.props.SuperRootsOfOne(3, 2), [SuperNumber(1, 3, 2)])


class StandardPropsTests(PropsTests, unittest.TestCase):
    def setUp(self):
        self.props = props


class SuperNumbersPropsTests(PropsTests, unittest.TestCase):
    def setUp(self):
        self.props = props_supernumbers


class SpanTests(unittest.TestCase):
    def test_set_span_of_inconsistent_set(self):
        with self.assertRaises(ValueError):
            span.SuperNumberSetSpan({SuperNumber(1, 3, 2), SuperNumber(1, 3, 0)})

    def test_set_span_of_empty_set(self):
        with self.assertRaises(ValueError):
            span.SuperNumberSetSpan({})

    def test_set_span_of_simple_set(self):
        n = SuperNumber(2, 4, 0)
        self.assertEqual({n, SuperNumber(0, 4, 0)}, span.SuperNumberSetSpan({n}))

    def test_set_span_of_larger_set(self):
        generators = {
            SuperNumber(4, 13, 2),
            SuperNumber(6, 13, 2),
        }
        # Answers we're expecting:
        # 4, 6
        # 4 * 6 = 4 + 6 + (2*4*6) % 13 = 6
        # 4 * 4 = 4 + 4 + (2*4*4) % 13 = 1
        # 6 * 6 = 6 + 6 + (2*6*6) % 13 = 6
        # 1 * 4 = 1 + 4 + (2*1*4) % 13 = 0
        # (0 times anything is itself, so we don't need to test these further)
        # 1 * 6 = 1 + 6 + (2*1*6) % 13 = 6
        # 1 * 1 = 1 + 1 + (2*1*1) % 13 = 4
        expected_ns = {0, 1, 4, 6}
        expected = {SuperNumber(n, 13, 2) for n in expected_ns}

        self.assertEqual(expected, span.SuperNumberSetSpan(generators))


if __name__ == "__main__":
    unittest.main()
