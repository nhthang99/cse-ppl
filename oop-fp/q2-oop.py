class Rational:
    def __init__(self, n=0, d=1):
        if d == 0:
            raise SystemExit("d == 0")
        else:
            self.n = n
            self.d = d
            self.__g = self.__gcd(n, d)
            self.numer = n // self.__g
            self.denom = d // self.__g

    def __gcd(self, a, b):
        if b == 0:
            return a
        return self.__gcd(b, a % b)

    def __add__(self, that):
        if isinstance(that, Rational):
            return Rational(self.numer * that.denom + that.numer * self.denom, self.denom * that.denom)
        elif isinstance(that, int):
            return self + Rational(that)
        else:
            return None

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

x = Rational(2, 5)
print("numer: " + str(x.numer))
print("denom: " + str(x.denom))
print("x + Rational(2, 3): " + str(x + Rational(2, 3)))
print("x + 2: " + str(x + 2))