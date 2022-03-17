"""
Provides a function to calculate the span of a set of supernumbers.
"""

from math import prod

from supernumber import SuperNumber
from props_checked import (
    IsAssociativeSuperNumberMultiplication,
    IsCommutativeSuperNumberMultiplication,
)


def SuperNumberSetSpan(generators):
    """
    Calculate the span of a set of "generator" supernumbers, that is, the set
    of all supernumbers that can be obtained by multiplying together elements
    of the set.
    """

    if len(generators) == 0:
        raise ValueError("SuperNumberSetSpan called on empty set")

    # Make sure sns all have the same n and alpha
    first = next(iter(generators))
    if not all(
        gen.modulus == first.modulus and gen.multiplier == first.multiplier
        for gen in generators
    ):
        raise ValueError("Mismatched set passed to SuperNumberSetSpan")

    # The implementation assumes this is true. We think this is always the
    # case (and have verified it for n ≤ 50), but since it's not been formally
    # proven let's make sure.
    assert IsCommutativeSuperNumberMultiplication(first.modulus, first.multiplier)

    # All of the generators can be obtained by not multiplying them by anything, of course.
    results = set(generators)

    # Now, take all of the results we know we can obtain, and try multiplying
    # them by each of the generators to see if we get anything new. Stop once
    # we stop finding new things.
    while True:
        last_len = len(results)

        for gen in generators:
            # n.b. create an intermediate set, instead of passing the
            # comprehension directly as an iterator, so we don't try to update
            # results while we're iterating it
            results.update({gen * result for result in results})

        if last_len == len(results):
            break

    return results