import math




class Rational:
    def __init__(self, u, d):
        self.u = u
        self.d = d

    def __str__(self):
        return f"{self.u}/{self.d}"

    def __add__(self, other):
        tmp_u = self.u * other.d + other.u * self.d
        tmp_d = self.d*other.d
        return Rational(int(tmp_u/math.gcd(tmp_u, tmp_d)), int(tmp_d/math.gcd(tmp_u, tmp_d)))

    def __sub__(self, other):
        tmp_u = self.u * other.d - other.u * self.d
        tmp_d = self.d*other.d
        return Rational(int(tmp_u/math.gcd(tmp_u, tmp_d)), int(tmp_d/math.gcd(tmp_u, tmp_d)))

    def __mul__(self, other):
        tmp_u = self.u * other.u
        tmp_d = self.d * other.d
        return Rational(int(tmp_u/math.gcd(tmp_u, tmp_d)), int(tmp_d/math.gcd(tmp_u, tmp_d)))

    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.u*other.d < other.u*self.d

    def __le__(self, other):
        return self.u*other.d <= other.u*self.d

    def __gt__(self, other):
        return self.u*other.d > other.u*self.d

    def __ge__(self, other):
        return self.u*other.d >= other.u*self.d

    def __eq__(self, other):
        return self.u*other.d == other.u*self.d

    def __ne__(self, other):
         return self.u*other.d != other.u*self.d



        
"""


r1 = Rational(2,5)
r2 = Rational(1,3)
r3 = Rational(4,7)

print(f"\n+") #Перевірка складання
print(r1+r2)
print(r1+r2+r3)
print(f"\n-") #Перевірка віднімання
print(r3-r1)
print(Rational(6,7)-r3)
print(f"\n*") #Перевірка множення
print(r1*r2)
print(r1*r1)

print(f"\n>")  #Перевірка >
print(Rational(7,12)>Rational(5,12))
print(Rational(5,12)>Rational(7,12))

print(f"\n<")  #Перевірка <
print(Rational(5,12)>Rational(7,12))
print(Rational(7,12)>Rational(5,12))

print(f"\n>=")  #Перевірка >=
print(Rational(3,4)>=Rational(3,4))
print(Rational(3,4)>=Rational(1,4))
print(Rational(1,4)>=Rational(3,4))

print(f"\n<=")  #Перевірка <=
print(Rational(3,4)<=Rational(3,4))
print(Rational(3,4)<=Rational(1,4))
print(Rational(1,4)<=Rational(3,4))

print(f"\n==")  #Перевірка ==
print(Rational(17,35)==Rational(17,35))
print(Rational(13,35)==Rational(17,35))

print(f"\n!=")  #Перевірка !=
print(Rational(17,35)!=Rational(17,35))
print(Rational(13,35)!=Rational(17,35))



"""




