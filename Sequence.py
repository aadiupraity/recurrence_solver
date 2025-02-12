import cmath
import math
import sympy as sp


def first_order():
    print("Let the equation be x_n = a*x_{n-1},  n starting from 1 ")
    a = float(input("a = ? "))
    x_i = (input('Whats a value in the sequence you know? [in "x_k=c" format]'))
    x_i = x_i.strip().split('=')
    c = float(x_i[1])
    sub = x_i[0].split('_')
    k = float(sub[1])
    x_0 = c/(a**k)
    print(f"General term: x_n = {a}^n*{x_0}")

    

def second_order():
    print("Let the equation be x_n = a_1*x_{n-1} + a_2*x_{n-2}")
    
    try:
        a_1 = -float(input("a_1 = "))
        a_2 = -float(input("a_2 = "))
    except ValueError:
        print("Please enter numbers")
        return
    
    # Discrimnant
    D = (a_1**2) - 4*(a_2)

    print('What are 2 values in the sequence you know? [in "x_k=c" and "x_l=d" format]')
    
    try:
        k = int(input("k = "))
        c = float(input("c = "))
        l = int(input("l = "))
        d = float(input("d = "))
    except ValueError:
        print("Indices must be integers and values must be numbers.")
        return
    
    if k == l:
        print("Please input values of 2 *different* indices")
        return

    if D > 0:
        x = (-a_1 + math.sqrt(D))/(2)
        y = (-a_1 - math.sqrt(D))/(2)

        
        A1 = (c*(y**(l)) - d*(y**(k)))/((x**(k))*(y**(l)) - (x**(l))*(y**(k)))
        A2 = (d - A1*(x**l))/(y**l)

        print(f"The general terms of this sequence are x_n = {A1}*({x}^n) + ({A2}*({y}^n))")

    if D == 0:
        x = -a_1/2 

        A2 = ((c*(x**l) - d*(x**k))/((k-l)*(x**(k+l))))
        A1 = ((c - A2*k*(x**k))/(x**k))
        print(A1, A2)
        print(f"The general terms of this sequence are x_n = {x}^n * ({A1} + ({A2}*n))")

    if D < 0:
        x = sp.Symbol('x')
        eq = sp.Eq(x**2 + a_1*x + a_2,0)
        roots = sp.solve(eq,x)
        psi, phi = roots  

        A1, A2 = sp.symbols('A1 A2')

        eq1 = sp.Eq(A1 * (psi**k) + A2 * (phi**k), c)
        eq2 = sp.Eq(A1 * (psi**l) + A2 * (phi**l), d)

        solution = sp.solve((eq1, eq2), (A1, A2))

        A1_val = solution[A1]
        A2_val = solution[A2]

        # General term formula
        general_term = f"x_n = ({A1_val} * ({psi})^n) + ({A2_val} * ({phi})^n)"
        print(f"General solution: {general_term}")


def homo():
    ans = input("Is it a first, second, third or fourth order sequence? [F/S/T/Q]").strip().upper()
    
    if ans == "F":
        first_order()
        return 0
    elif ans == "S":
        second_order()
        return 0
    elif ans == "T":
        third_order()
        return 0
    elif ans == "Q":
        fourth_order()
        return 0
    else:
        print("Please input [F/S/T/Q]")
    homo()

def third_order():
    print("Third-order recurrence selected.")

def fourth_order():
    print("Fourth-order recurrence selected.")



def non_homo():
    print("Non-homogeneous recurrence selected.")    

def main():
    ans = input("What type of recurrence relation doy you have in mind? Homogeneous or Non Homogeneous [H/N]").strip().upper()
    if ans == "H":
        homo()
    elif ans == "N":
        non_homo()

main()