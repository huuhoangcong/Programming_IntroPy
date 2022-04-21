class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        try:
            numerator/denominator
        except:
            print("Error")
            exit()

    def __add__(self, f1):
        if self.denominator == f1.denominator:
            t = self.numerator + f1.numerator
            m = self.denominator
        else:
            t = self.numerator*f1.denominator + f1.numerator*self.denominator
            m = self.denominator*f1.denominator
        
        return Fraction(t,m)

    def __add__(self, f1):
        if self.denominator == f1.denominator:
            t = self.numerator + f1.numerator
            m = self.denominator
        else:
            t = self.numerator*f1.denominator + f1.numerator*self.denominator
            m = self.denominator*f1.denominator
        
        return Fraction(t,m)

    def __mul__(self, f1):
        t = self.numerator * f1.numerator
        m = self.denominator * f1.denominator

        return Fraction(t,m)
    
    def __truediv__(self, f1):
        t = self.numerator * f1.denominator
        m = self.denominator * f1.numerator

        return Fraction(t,m)

    def simplify(self):
        gcd = [] 
        for i in range(1, self.numerator+1):
            if self.numerator%i==0 and self.denominator%i==0:
                gcd.append(i)

        t = int(self.numerator/max(gcd))
        m = int(self.denominator/max(gcd))

        return Fraction(t,m)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def equal(self, f1):
        if self.simplify().numerator == f1.simplify().numerator and self.simplify().denominator == f1.simplify().denominator:
            return True
        else:
            False


f1 = Fraction(45,0)
f2 = Fraction(45,32)

print(f1.equal(f2))