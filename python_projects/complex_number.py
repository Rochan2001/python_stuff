from math import pow


class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real+other.real, self.imag+other.imag)

    def __sub__(self, other):
        return complex(self.real-other.real, self.imag-other.imag)

    def __mul__(self, other):
        return complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)

    def __truediv__(self, other):
        try:
            return self.__mul__(complex(other.real, -1*other.imag)).__mul__(complex(1.0/(other.mod().real)**2, 0))
        except Exception as e:
            print(e)
            return None

    def mod(self):
        return pow(self.real**2+self.imag**2, 0.5)

    def __str__(self, precision=2):
        return str(("%."+"%df" % precision) % float(self.real))+('+' if self.imag >= 0 else '-')+str(("%."+"%df" % precision) % float(abs(self.imag)))+'i'


print ("Enter real and imaginary part of complex No - 1(separeated by space)")
A = complex(*map(float,input().strip().split()))
print ("Enter real and imaginary part of complex No - 2(separeated by space)")
B = complex(*map(float,input().strip().split()))

print( "Addition: " + str(A+B))
print( "Subtraction: " + str(A-B))
print( "Multiplication: " + str(A*B))
print( "Division: " + str(A/B))
print( "Modulas of complex Number A: " + str(A.mod()))
