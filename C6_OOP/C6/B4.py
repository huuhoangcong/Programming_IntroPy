class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def getReal(self):
        return self.real
    def getImg(self):
        return self.img

    def module(self):
        return pow(self.real**2+self.img**2,0.5)

    def conjugate(self):
        return Complex(self.real,-self.img)

    def __add__(self, z):
        return Complex(self.real+z.real, self.img+z.img)

    def __sub__(self, z):
        return Complex(self.real-z.real, self.img-z.img)

    def __mul__(self, z):
        return Complex(self.real*z.real-self.img*z.img,self.real*z.img+self.img*z.real)

    def __truediv__(self, z):
        r = (self*(z.conjugate())).real/z.module()**2
        i = (self*(z.conjugate())).img/z.module()**2
        
        return Complex(r,i)  
    
    def __str__(self):
        return f'{self.real}+{self.img}j'

    def equal(self, z):
        if self.real == z.real and self.img == z.img:
            return True
        else:
            return False

z1 = Complex(1,2)
z2 = Complex(3,4)
print(z1/z2)