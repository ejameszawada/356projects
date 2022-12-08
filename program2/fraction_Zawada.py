# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 2
# Due Date: 2/11/22
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: This program takes input from the user to make two fractions, and then it
# calculates the value of the two fractions added, subtracted, multiplied, and divided.

class Fraction:
    def __init__(self, numerator, denominator):
        # create numerator and denominator variables
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        # return just the numerator because anything / 1 is itself
        if self.denominator == 1:
            return str(self.numerator)
        # otherwise return both the num and den
        else:
            return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, obj):
        # calc the numerator result
        numresult = self.numerator * obj.denominator + self.denominator * obj.numerator
        # calc the denominator
        denresult = self.denominator * obj.denominator
        # get common divisor
        common = gcd(numresult, denresult)
        return Fraction(numresult // common, denresult // common)

    def __sub__(self, obj):
        # calc the num
        numresult = self.numerator * obj.denominator - self.denominator * obj.numerator
        # calc the den
        denresult = self.denominator * obj.denominator
        # get common divisor
        common = gcd(numresult, denresult)
        return Fraction(numresult // common, denresult // common)

    def __mul__(self, obj):
        # calc the num
        numresult = self.numerator * obj.numerator
        # calc the den
        denresult = self.denominator * obj.denominator
        # get common divisor
        common = gcd(numresult, denresult)
        return Fraction(numresult // common, denresult // common)

    def __truediv__(self, obj):
        # calc the num
        numresult = self.numerator * obj.denominator
        # calc the den
        denresult = self.denominator * obj.numerator
        # get common divisor
        common = gcd(numresult, denresult)
        return Fraction(numresult // common, denresult // common)

# gcd helper function
def gcd(x, y):
    # when the numerator divide by the den, then it finds the gcd
    while x % y != 0:
        tempx = x
        tempy = y
        x = tempy
        y = tempx % tempy
    return y


def main():
    # input
    num1 = int(input("Enter numerator of the first fraction: "))
    num2 = int(input("Enter denominator of the first fraction: "))
    num3 = int(input("Enter numerator of the second fraction: "))
    num4 = int(input("Enter denominator of the second fraction: "))
    # create fraction class objects
    frac1 = Fraction(num1, num2)
    frac2 = Fraction(num3, num4)
    # display
    print("\nFirst fraction:", frac1)
    print("Second fraction:", frac2,)
    print(frac1, "+", frac2, "=", frac1 + frac2)
    print(frac1, "-", frac2, "=", frac1 - frac2)
    print(frac1, "*", frac2, "=", frac1 * frac2)
    print(frac1, "/", frac2, "=", frac1 / frac2)

# run main
main()