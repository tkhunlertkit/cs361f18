def verify(func):
    def return_func(func):
        @wraps(func)
        def check_other(self, other):
        if not isinstance(other, Rational):
            raise Exception("wrong type")
        return func(self, other)

    return check_other

class Rational(object):
    """
        An instance represents a rational number.
        Numerator and denominator reduced to lowest terms.
        Denominator must be positive.
    """

    def __init__(self, a=0, b=1):
        """
            Constructor for Rational.
        """
        if b == 0:
            raise(ZeroDivisionError("Denom may not be zero."))
        else:
            self.n = a
            self.d = b

        self.simplify()

    @verify
    def __eq__(self, other):
        if not isinstance(other, Rational):
            return False

        return self.n == other.n and self.d == other.d

    def add(self, other):
        """
            Add two rational numbers.
        """

        return Rational()

    def sub(self, other):
        """
            Return self minus other.
        """
        return Rational()

    def mul(self, other):
        """
            Implement multiplication.
        """
        return Rational()

    def div(self, other):
        """
            Implement division.
        """
        return Rational()

    def str(self):
        """
            Display self as a string.
        """
        return "0/1"

    def float(self):
        """
            Implement the float() conversion function.
        """
        return 0.0

    def simplify(self):
        x = self.n
        y = self.d

        # Find gcd
        while y:
            x, y = y, x % y

        self.n /= x
        self.d /= x

    def verify(func):
        def check_other(*args, **keqrgs):
            if not isinstance(other, Rational):
                raise Exception("wrong type")
            return func(self, other)

        return check_other