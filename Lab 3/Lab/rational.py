class Rational:
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