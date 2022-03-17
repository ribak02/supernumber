"""
Provides the same functions as props, but uses the SuperNumbers abstraction.
"""


from core import SuperNumber, SuperNumbers


def HasSuperNumberIdempotentProperty(n, alpha):
    """
    Checks for given n and alpha whether the equality x * x = x holds for all
    supernumbers
    """

    return all(x * x == x for x in SuperNumbers(n, alpha))


def IsCommutativeSuperNumberMultiplication(n, alpha):
    """
    Checks for given n and alpha whether the equality x * y = y * x holds for
    all supernumbers
    """
    sns = SuperNumbers(n, alpha)
    return all((x * y == x * y for x in sns for y in sns.iter_below(x)))


def IsAssociativeSuperNumberMultiplication(n, alpha):
    """
    Checks for given n and alpha whether the equality (x * y) * z = x * (y * z)
    hold for all supernumbers
    """

    sns = SuperNumbers(n, alpha)
    return all(
        (x * y) * z == x * (y * z)
        for x in sns
        for y in sns.iter_below(x)
        for z in sns.iter_below(y)
    )


def SuperRootsOfOne(n, alpha):
    """
    Calculates for given n and alpha the list of all elements that satisfy x * x = 1
    """

    sns = SuperNumbers(n, alpha)
    return [x for x in sns if x * x == SuperNumber(1, n, alpha)]
