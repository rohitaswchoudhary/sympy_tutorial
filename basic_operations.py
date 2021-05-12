from sympy import *

x,y,z = symbols('x y z')

expr = cos(x)+1

print(expr)

print(expr.subs(x,y))

print(expr.subs(x,0))

print("*******************************************************************************************************")
expr_2 = x**y

print(expr_2)

