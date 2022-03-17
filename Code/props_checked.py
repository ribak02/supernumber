"""
Versions of the property functions that compute the answer both ways, and make
sure they're equal, before returning them.
"""

import props as props_std
import props_supernumbers as props_sns


def _makeCheckedFunction(name):
    """
    Given the name of a function in props and props_supernumbers, return a
    version of that function that calls both functions, asserts the result is
    equal and returns it.
    """

    def fn(n, alpha):
        """
        Given n and alpha, call both versions of the function, check the
        result, and return it.
        """
        std = getattr(props_std, name)(n, alpha)
        sns = getattr(props_sns, name)(n, alpha)
        assert std == sns
        return std

    return fn


HasSuperNumberIdempotentProperty = _makeCheckedFunction(
    "HasSuperNumberIdempotentProperty"
)
IsCommutativeSuperNumberMultiplication = _makeCheckedFunction(
    "IsCommutativeSuperNumberMultiplication"
)
IsAssociativeSuperNumberMultiplication = _makeCheckedFunction(
    "IsAssociativeSuperNumberMultiplication"
)
SuperRootsOfOne = _makeCheckedFunction("SuperRootsOfOne")