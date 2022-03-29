class Rational:
    """ Class implements rational numbers (ratio of integers)."""

    def __init__(self, num, dnm):
        """Intializes Rational number object; assigning numerator and denominator in appropriate fields.

        Args:
            num (int): Numerator of Rational Number
            dnm (int): Denominator of Rational Number
        """

        assert isinstance(num, int), "Check whether numerator is integer or not"
        assert isinstance(dnm, int), "Check whether denominator is integer or not"

        self.num = num
        self.dnm = dnm

    def __repr__(self):
        if self.dnm != 1:
            return f"{self.num}/{self.dnm}"
        else:
            return f"{self.num}"

    def compute_hcf(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def simplest_form(self, rat):

        assert isinstance(rat, Rational), " Check whether the class of rat is Rational"

        hcf = self.compute_hcf(min(rat.num, rat.dnm), max(rat.num, rat.dnm))
        rat.num //= hcf
        rat.dnm //= hcf

        return rat

    def __float__(self):
        return self.num / self.dnm

    def __int__(self):
        return self.num // self.dnm

    def __neg__(self):
        self.num = -1 * self.num
        return self

    def __mul__(self, other):

        if isinstance(other, Rational):
            return Rational(self.num * other.num, self.dnm * other.dnm)
        else:
            assert isinstance(other, int), " Check whether the other is int or not."
            return self.simplest_form(Rational(self.num * other, self.dnm))

    def __rmul__(self, other):

        if isinstance(other, Rational):
            return Rational(self.num * other.num, self.dnm * other.dnm)
        else:
            assert isinstance(other, int), " Check whether the other is int or not."
            return self.simplest_form(Rational(self.num * other, self.dnm))

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return self.simplest_form(
                Rational(self.num * other.dnm, self.dnm * other.num)
            )
        else:
            assert isinstance(other, int), " Check whether the other is int or not."
            assert other != 0, "Division by zero not allowed."
            return self.simplest_form(Rational(self.num, other * self.dnm))

    def __rtruediv__(self, other):
        assert isinstance(other, int), " Check whether the 2nd operand is int or not."
        return Rational(other * self.dnm, self.num)

    def __add__(self, other):
        if isinstance(other, Rational):
            num_new = (self.num * other.dnm) + (other.num * self.dnm)
            dnm_new = self.dnm * other.dnm
        else:
            assert isinstance(
                other, int
            ), " Check whether the 2nd operand is int or not."
            return self.__add__(Rational(other, 1))

        return self.simplest_form(Rational(num_new, dnm_new))

    def __sub__(self, other):
        if isinstance(other, Rational):
            num_new = (self.num * other.dnm) - (other.num * self.dnm)
            dnm_new = self.dnm * other.dnm
        else:
            assert isinstance(
                other, int
            ), " Check whether the 2nd operand is int or not."
            return self.__sub__(Rational(other, 1))

        return self.simplest_form(Rational(num_new, dnm_new))

    def __lt__(self, other):
        return (self.num * other.dnm) < (other.num * self.dnm)

    def __le__(self, other):
        return (self.num * other.dnm) <= (other.num * self.dnm)

    def __gt__(self, other):
        return (self.num * other.dnm) > (other.num * self.dnm)

    def __ge__(self, other):
        return (self.num * other.dnm) >= (other.num * self.dnm)

    def __eq__(self, other):

        assert isinstance(
            other, Rational
        ), "Check whether the 2nd operand is Rational or not."
        assert isinstance(
            self, Rational
        ), "Check whether the 1st operand is Rational or not."

        s1 = self.simplest_form(self)
        s2 = self.simplest_form(other)

        return s1.num == s2.num and s1.dnm == s2.dnm
