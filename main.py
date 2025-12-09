import cmath


def resolver(a,b,c):
    D= b**2 -4*a*c
    x1=(-b-cmath.sqrt(D))/(2*a)
    x2=(-b+cmath.sqrt(D))/(2*a)
    return x1,x2


a=1
b=2
c=1

print("Equação: %d*x**2+ %d*x +%d=0"%(a,b,c))
solução= resolver(a,b,c)
print("respota:")
print("x1 = %s" %solução[0])
print("x2 = %s" %solução[1])