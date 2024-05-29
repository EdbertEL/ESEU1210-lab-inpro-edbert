
class Fraction:
    def __init__(self, numerator = 0, denominator = 1) :
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer.") 
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer.") 

        if numerator == 0 :
            self._numerator = 0
            self._denominator = 1
        else :
            if (numerator < 0 and denominator >= 0 or numerator >= 0 and denominator < 0) :
                sign = -1
            else :
                sign = 1
            a = abs(numerator)
            b = abs(denominator)
            
            simplify = self._gcd(a, b)
            self._numerator = sign * (a // simplify)
            self._denominator = b // simplify

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"
    
    def to_float(self):
        return self._numerator / self._denominator



    # def __add__(self,rhs):
    #     lhs = self
    #     num = lhs.getNumerator() * rhs.getDenominator() + rhs.getDenominator() * lhs.getDenominator()
    #     den = lhs.getDenominator() * rhs.getDenominator()
    #     return Fraction(num,den)
    
    # def __sub__(self,rhs):
    #     lhs = self 
    #     num = lhs.getNumerator() * rhs.getDenominator() - rhs.getNumerator() * lhs.getDenominator()
    #     den = lhs.getDenominator() * rhs.getDenominator()
    #     return Fraction(num,den)
    
    # def __mult__(self,rhs):
    #     lhs = self
    #     num = lhs.getNumerator() * rhs.getDenominator()
    #     den = lhs.getDenominator() * rhs.getDenominator()
    #     return Fraction(num, den)
    
    # def __truediv__(self,rhs):
    #     lhs = self
    #     num = lhs.getNumerator() * rhs.getDenominator()
    #     den = lhs.getDenominator() * rhs.getNumerator()
    #     return Fraction(num, den)
    
    # def __floordiv__(self, rhs):
    #         lhs = self
    #         return lhs._numerator // lhs._denominator // (rhs._numerator // rhs._denominator)
    
    # def __eq__(self, rhs):
    #     lhs = self
    #     return (lhs.getNumerator == rhs.getNumerator()) and (lhs.getDenominator == rhs.getDenominator())

    # def __ne__(self,rhs):
    #     lhs = self
    #     return not lhs == rhs   
    
    # def __lt__(self,rhs):
    #     lhs = self
    #     return lhs.getNumerator() * rhs.getDenominator() < lhs.getNumerator() * rhs.getDenominator()
    
    # def __le__(self, rhs):
    #     lhs = self
    #     return not rhs < lhs
    
    # def __gt__(self,rhs):
    #     lhs = self
    #     return rhs < lhs
    
    # def __ge__(self,rhs):
    #     lhs = self 
    #     return not rhs > lhs

    
frac1 = Fraction(-2, 8)
print("Fraction in rational form:", frac1)
print("Fraction in floating-point form:", frac1.to_float())

frac2 = Fraction(45, 3)
print("Fraction in rational form:", frac2)
print("Fraction in floating-point form:", frac2.to_float())


# Demonstrating arithmetic operations
f1 = Fraction(2, -2)
f2 = Fraction(3, -4)

f3 = f1.__add__(f2)

f4 = f1.__sub__(f2)

f5 = f1.__mult__(f2)

f6 = f1.__truediv__(f2)

print(f3.__repr__())
print(f4.__repr__())
print(f5.__repr__())
print(f6.__repr__())
print (f1)  

