# Vinícius Brito Bastos Antunes: COMP-22

import numpy as num
import math
import turtle as tr

# Exercício 1

tr.pensize(3)
tr.bgcolor("light green")
tr.color("hotpink", "hotpink")
for a in range(0, 5):
    tr.down()
    for i in range(0, 4):
        tr.forward(20*(a+1))
        tr.left(90)
    tr.up()
    tr.right(90)
    tr.forward(10)
    tr.right(90)
    tr.forward(10)
    tr.left(180)
tr.done()

# Exercício 2
# Obs.: não entendi o que é o tess, mas o desenho é feito corretamente

def draw_poly(t, n, sz):
    tr.pensize(3)
    tr.bgcolor("light green")
    tr.color("hotpink", "hotpink")
    for i in range(0, n):
        tr.forward(sz)
        tr.left(360/n)
    tr.done()

# Exercício 3

def sum_to(n):
    return sum(list(range(1, n+1)))

# Exercício 4
    
def sum_til_even(x):
    S = 0
    for i in x:
        if i&1:
            S+=i
        else:
            break
    return S

# Exercício 5

def sam_count(x):
    ct = 0
    for i in x:
        if type(i)==str:
            ct+=1
        if i=="sam":
            break
    return ct

# Exercício 6
    
def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    if n==1:
        return False
    return True

# Exercício 7

def sum_of_squares(x):
    return num.dot(x, x)

# Exercício 8

print('{:>9}'.format(1), end='')
for i in range(2, 13):
    print('{:>4}'.format(i), end='')
    
print("\n  :--------------------------------------------------")

for i in range(1, 13):
    print('{:>2}'.format(i), end=':')
    print('{:>6}'.format(i), end='')
    for j in range(2, 13):
        print('{:>4}'.format(i*j), end='')
    print('')

# Exercício 9
    
def is_palindrome(x):
    return x==x[::-1]

# Exercício 10
    
def complex_sum(a, b):
    print(a[0]+b[0],"+",str(a[1]+b[1])+"i")