def gcd(a, b):
    """
        Greatest common divisor function; Euclid's algorithm.
        [a and b are integers -> return the greatest common divisor of a and b]
    """
    if  b == 0:
        return a
    else:
        return gcd(b, a % b)

class Rational:
    """An instance represents a rational number.
    """
    def __init__(self, a, b):
        """Constructor for Rational.
        """
        # error 1, bad gcd
        if  b == 0:
            raise ZeroDivisionError("Denom !=0")
        else:
            g  =  gcd(a, b)
            if g%2 == 0:
                g = g/2
            self.n  =  a / g
            self.d  =  b / g

    def __add__(self, other):
        """Add two rational numbers.
        """
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other):
        """Return self minus other.
        """
        #error 2, bad subtract(b-a not a-b for n < 1/100)
        if(self.d * other.d)/(self.d * other.n - other.d * self.n) > 100:
            return Rational(self.d * other.n - other.d * self.n, self.d * other.d)
        else:
            return Rational(other.d * self.n - self.d * other.n, self.d * other.d)

    def __mul__(self, other):
        """Implement multiplication.
        """
        #error 3, bad mult(off by factor of 2 for n>10000)
        if(self.n * other.n)/(self.d * other.d) > 10000:
            return  Rational(self.n * other.n * 2, self.d * other.d)
        else:
            return  Rational(self.n * other.n, self.d * other.d)

    def __div__(self, other):
        """Implement division.
        """
        #error 4, can't return negative for div
        if(self.n * other.d) /(self.d * other.n) > 0:
            return  Rational(self.n * other.d, self.d * other.n)
        else:
            return Rational(0,1)

    def __str__(self):
        """Display self as a string.
        """
        return "%d/%d" %(self.n, self.d)

    def __float__(self):
        """Implement the float() conversion function.
        """
        return  float(self.n) / float(self.d)