"""
The core implementation of SuperNumber and SuperNumbers.
"""


class SuperNumber:
    """
    Represents a supernumber, a type of number definied by an integer, along
    with two other integers: a modulus (aka n), and a multiplier (aka alpha).
    """

    def __init__(self, obj, mod, mult):
        """
        Create a supernumber from the underlying integer, modulus, and
        multiplier. If the integer or multiplier are larger than the modulus,
        we instead use that value modulo the modulus.
        """
        if not type(obj) is int:
            raise TypeError("Num is not an int.")
        if obj < 0:
            raise Exception("Num is not greater than zero.")
        if not type(mod) is int:
            raise TypeError("Modulus is not an int.")
        if mod < 0:
            raise Exception("Modulus is not greater than zero.")
        if not type(mult) is int:
            raise TypeError("Multiplier is not an int.")
        if mult < 0:
            raise Exception("Multiplier is not greater than zero.")
        self.object = obj % mod
        self.multiplier = mult % mod
        self.modulus = mod

    def __repr__(self):
        """
        Formats and prints a readable supernumber.
        """
        return f"<{self.object} mod {self.modulus} | {self.multiplier}>"

    def __mul__(self, other):
        """
        Multiplies itself with another supernumber passed in as other.
        Multiplication between supernumbers is only defined for supernumbers
        with the same n and alpha, and is defined as follows (where x and y are
        the integer values of the two supernumbers):

        (x + y + alpha*x*y) % n
        """
        if self.multiplier == other.multiplier and self.modulus == other.modulus:
            return SuperNumber(
                (
                    self.object
                    + other.object
                    + (self.multiplier * self.object * other.object)
                )
                % self.modulus,
                self.modulus,
                self.multiplier,
            )
        else:
            raise Exception("Modulus and multiplier are not the same.")

    def __eq__(self, other):
        """
        Checks equality between itself and another supernumber passed in as other.
        """
        return (
            self.multiplier == other.multiplier
            and self.modulus == other.modulus
            and self.object == other.object
        )

    def __hash__(self):
        """
        Get a hash for this supernumber.
        """
        return hash((self.multiplier, self.modulus, self.object))


class SuperNumbers:
    """
    Create multiple SuperNumbers which are iterable.
    """

    def __init__(self, mod, mult):
        """
        Create a representation of the set of supernumbers with the given
        modulus and multiplier.
        """
        if not type(mod) is int:
            raise TypeError("Modulus is not an int.")
        if mod < 0:
            raise Exception("Modulus is not greater than zero.")
        if not type(mult) is int:
            raise TypeError("Multiplier is not an int.")
        if mult < 0:
            raise Exception("Multiplier is not greater than zero.")
        self.modulus = mod
        self.multiplier = mult % mod

    def __repr__(self):
        """
        Formats and prints a readable supernumber.
        """
        return f"<SuperNumbers mod {self.modulus} | {self.multiplier}>"

    def size(self):
        """
        Returns the amount of supernumbers.
        """
        return self.modulus

    def __iter__(self):
        """
        Creates n (modulus) amount of supernumbers
        """
        return (
            SuperNumber(x, self.modulus, self.multiplier) for x in range(self.modulus)
        )

    def __eq__(self, other):
        """
        Checks equality between itself and another supernumber passed in as other.
        """
        return self.modulus == other.modulus and self.multiplier == other.multiplier

    def iter_below(self, sn):
        """
        Return an iterator of every supernumber in this set up until sn.
        """
        if self.modulus != sn.modulus or self.multiplier != sn.multiplier:
            raise Exception(f"Supernumber {sn} is not compatible with {self}")

        return (SuperNumber(x, self.modulus, self.multiplier) for x in range(sn.object))
