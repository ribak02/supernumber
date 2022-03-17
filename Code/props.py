"""
Provides functions to test various properties of a set of supernumbers.
"""

from core import SuperNumber


def HasSuperNumberIdempotentProperty(n, alpha):
    """
    Checks for given n and alpha whether the equality x * x = x holds for all
    supernumbers
    """

    def is_idempotent(x):
        sn = SuperNumber(x, n, alpha)
        return sn * sn == sn

    return all(is_idempotent(x) for x in range(n))


def IsCommutativeSuperNumberMultiplication(n, alpha):
    """
    Checks for given n and alpha whether the equality x * y = y * x holds for
    all supernumbers
    """

    def is_commutative(x, y):
        snx = SuperNumber(x, n, alpha)
        sny = SuperNumber(y, n, alpha)
        return snx * sny == sny * snx

    return all((is_commutative(x, y) for x in range(n) for y in range(x)))


def IsAssociativeSuperNumberMultiplication(n, alpha):
    """
    Checks for given n and alpha whether the equality (x * y) * z = x * (y * z)
    hold for all supernumbers
    """

    def is_associative(x, y, z):
        snx = SuperNumber(x, n, alpha)
        sny = SuperNumber(y, n, alpha)
        snz = SuperNumber(z, n, alpha)
        return (snx * sny) * snz == snx * (sny * snz)

    return all(
        (
            is_associative(x, y, z)
            for z in range(n)
            for y in range(n)
            for x in range(n)
            if z >= y >= x
        )
    )


def SuperRootsOfOne(n, alpha):
    """
    Calculates for given n and alpha the list of all elements that satisfy x * x = 1
    """

    superRootsOfOne = []
    for i in range(n):
        x = SuperNumber(i, n, alpha)
        if (x * x) == SuperNumber(1, n, alpha):
            superRootsOfOne.append(x)
    return superRootsOfOne
