from math import gcd

class Fraction:
    def __init__(self, numerator=1, denominator=None):
        if denominator is None:
            self.numerator = numerator
            self.denominator = 1
        else:
            if denominator == 0:
                raise ValueError("Denominator cannot be zero.")
            self.numerator = numerator
            self.denominator = denominator
        
        self._reduce()

    def _reduce(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    # חיבור
    def __add__(self, other):
        if isinstance(other, Fraction):
            n = self.numerator*other.denominator + other.numerator*self.denominator
            d = self.denominator*other.denominator
            return Fraction(n, d)
        else:
            return Fraction(self.numerator + other*self.denominator, self.denominator)

    __radd__ = __add__

    # חיסור
    def __sub__(self, other):
        if isinstance(other, Fraction):
            n = self.numerator*other.denominator - other.numerator*self.denominator
            d = self.denominator*other.denominator
            return Fraction(n, d)
        else:
            return Fraction(self.numerator - other*self.denominator, self.denominator)

    def __rsub__(self, other):
        return Fraction(other*self.denominator - self.numerator, self.denominator)

    # כפל
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
        else:
            return Fraction(self.numerator*other, self.denominator)

    __rmul__ = __mul__

    # חילוק
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)
        else:
            return Fraction(self.numerator, self.denominator*other)

    def __rtruediv__(self, other):
        return Fraction(other*self.denominator, self.numerator)

    # השוואות
    def __eq__(self, other):
        return self.numerator*other.denominator == self.denominator*other.numerator

    def __lt__(self, other):
        return self.numerator*other.denominator < self.denominator*other.numerator

    def __le__(self, other):
        return self.numerator*other.denominator <= self.denominator*other.numerator

    def __gt__(self, other):
        return self.numerator*other.denominator > self.denominator*other.numerator

    def __ge__(self, other):
        return self.numerator*other.denominator >= self.denominator*other.numerator

# דוגמאות
a = Fraction(2, 4)
b = Fraction(3, 6)
c = Fraction(5)

print(a)
print(b)
print(c)

print(a + b)
print(a * c)
print(c - a)
print(c / a)
print(a == b)
print(a < c)
