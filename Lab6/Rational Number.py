#1 Because if the reset function is not there, self value is not declared, has null value.

# class CashRegister():
#     def __init__(self):
#         self.itemCount = 0
#         self.totalPrice = 0
#     def addItem(self, price):
#         self.itemCount += 1
#         self.totalPrice += price
#     def getCount(self):
#         return self.itemCount
#     def getTotal(self):
#         return self.totalPrice 
#     def clear(self):
#         self.itemCount = 0
#         self.totalPrice = 0

# register1 = CashRegister()
# register1.addItem(1.95)
# register1.addItem(0.95)
# register1.addItem(2.50)
# register2 = CashRegister()
# register2.addItem(3.75)
# register2.addItem(0.15)
# register2.addItem(2.25)
# register2.addItem(1.80)

# print("Register 1 sells", register1.getCount(),"items, with the total amount of $", register1.getTotal())
# print("Register 2 sells", register2.getCount(),"items, with the total amount of $", register2.getTotal())


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            print("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def to_float(self):
        return self.numerator / self.denominator


frac1 = Fraction(1, 3)
print("Fraction in rational form:", frac1)
print("Fraction in floating-point form:", frac1.to_float())

frac2 = Fraction(3, 6)
print("Fraction in rational form:", frac2)
print("Fraction in floating-point form:", frac2.to_float())

