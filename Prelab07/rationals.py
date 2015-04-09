"""
A Rational Number example from "Anadology.com"
"""

class RationalNumber:
    """
    Rational Numbers with support for arithmetic operations.

    """

    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator


    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        result = RationalNumber(n, d)
        print(result)

        return result


    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        result = RationalNumber(n1*d2 - n2*d1, d1*d2)
        print(result)

        return result


    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        result = RationalNumber(n1*n2, d1*d2)
        print(result)

        return result

    def __truediv__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        result = RationalNumber(n1*d2, d1*n2)
        print(result)

        return result


    def __str__(self):
        return "{0}/{1}".format(self.n, self.d)

    __repr__ = __str__


if __name__ == "__main__":
    a = RationalNumber(1, 2)
    b = RationalNumber(1, 3)

    a + b
    a + 1
    a - b

    a * b

    a / b
