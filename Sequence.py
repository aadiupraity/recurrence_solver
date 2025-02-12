import math
import sympy as sp


def first_order():
    print("Let the equation be x_n = a*x_{n-1},  n starting from 1 ")
    
    try:
        a = float(input("a = "))
    except ValueError:
        print("Please enter a number")
        return
    
    print('What is a value in the sequence you know? [in "x_k=c" format]')
    
    try:
        k = int(input("k = "))
        c = float(input("c = "))
    except ValueError:
        print("Indices must be integers and values must be numbers.")
        return
    
    x_0 = c/(a**k)
    print(f"General term: x_n = {sp.nsimplify(a)}^n * {sp.nsimplify(x_0)}")

    

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

        print(f"The general terms of this sequence are x_n = ({sp.nsimplify(A1)}) * ({sp.nsimplify(x)})^n + ({sp.nsimplify(A2)}) * ({sp.nsimplify(y)})^n")

    if D == 0:
        x = -a_1/2 
        A2 = ((c*(x**l) - d*(x**k))/((k-l)*(x**(k+l))))
        A1 = ((c - A2*k*(x**k))/(x**k))
        print(A1, A2)
        print(f"The general terms of this sequence are x_n = {x}^n * ({A1} + ({A2}*n))")

    if D < 0:
        x = sp.Symbol('x')
        eq = sp.Eq((x**2) + (a_1*x) + a_2,0)
        roots = sp.solve(eq,x)
        psi, phi = roots  

        A1, A2 = sp.symbols('A1 A2')

        eq1 = sp.Eq(A1 * (psi**k) + A2 * (phi**k), c)
        eq2 = sp.Eq(A1 * (psi**l) + A2 * (phi**l), d)

        solution = sp.solve((eq1, eq2), (A1, A2))

        A1_val = sp.nsimplify(solution[A1])     
        A2_val = sp.nsimplify(solution[A2])

        general_term = f"x_n = ({A1_val} * ({sp.nsimplify(psi)})^n) + ({A2_val} * ({sp.nsimplify(phi)})^n)"
        print(f"General solution: {general_term}")


def homo():
    ans = input("Is it a first, second or third order linear recurrence relation? [F/S/T]").strip().upper()
    
    if ans == "F":
        first_order()
        return 0
    elif ans == "S":
        second_order()
        return 0
    elif ans == "T":
        third_order()
        return 0
    else:
        print("Please input [F/S/T]")
    homo()

def third_order():
    print("Let the equation be x_n = a_1*x_{n-1} + a_2*x_{n-2} + a_3*x_{n-2}")
    
    try:
        a_1 = float(input("a_1 = "))
        a_2 = float(input("a_2 = "))
        a_3 = float(input("a_3 = "))
    except ValueError:
        print("Please enter numbers")
        return

    x = sp.Symbol('x')
    eq = sp.Eq((x**3) - a_1*(x**2) - a_2*x - a_3,0)
    roots = sp.solve(eq,x)
    
    D = 0

    # Checking for duplicate roots 
    if len(roots) == 2:
        D = 1  
    if roots[0] == roots[1] == roots[2]:
        D = 4

    print('What are 3 values in the sequence you know? [in "x_k=c" , "x_l=d" and "x_m=e" format]')
    
    try:
        k = int(input("k = "))
        c = float(input("c = "))
        l = int(input("l = "))
        d = float(input("d = "))
        m = int(input("m = "))
        e = float(input("e = "))
        
    except ValueError:
        print("Indices must be integers and values must be numbers.")
        return
    
    if k == l or l == m or k==m:
        print("Please input values of 3 *different* indices")
        return
    
    if D == 0:
        alp, bet, gam = roots
        A1, A2, A3 = sp.symbols('A1 A2 A3')

        eq1 = sp.Eq(A1 * (alp**k) + A2 * (bet**k) + A3 * (gam**k), c)
        eq2 = sp.Eq(A1 * (alp**l) + A2 * (bet**l) + A3 * (gam**l), d)
        eq3 = sp.Eq(A1 * (alp**m) + A2 * (bet**m) + A3 * (gam**m), e)

        solution = sp.solve((eq1,eq2,eq3),(A1,A2,A3))
        
        A1_val = sp.nsimplify(solution[A1])     
        A2_val = sp.nsimplify(solution[A2])
        A3_val = sp.nsimplify(solution[A3])

        general_term = f"x_n = ({A1_val} * ({alp})^n) + ({A2_val} * ({bet})^n) + ({A3_val} * ({gam})^n)"
        print(f"General solution: {general_term}")
    
    if D == 1:
        alp, gam = roots
        A1, A2, A3 = sp.symbols('A1 A2 A3')

        eq1 = sp.Eq((alp**k)*(A1+ (k*A2)) + A3 * (gam**k), c)
        eq2 = sp.Eq((alp**l)*(A1+ (l*A2)) + A3 * (gam**l), d)
        eq3 = sp.Eq((alp**m)*(A1+ (m*A2)) + A3 * (gam**m), e)

        solution = sp.solve((eq1,eq2,eq3),(A1,A2,A3))
        
        A1_val = sp.nsimplify(solution[A1])     
        A2_val = sp.nsimplify(solution[A2])
        A3_val = sp.nsimplify(solution[A3])

        general_term = f"x_n = ({sp.nsimplify(alp)}^n * ( {A1_val}  + (n * {A2_val}))) + ({A3_val} * ({sp.nsimplify(gam)})^n)"
        print(f"General solution: {general_term}")





def non_homo():
    print("Non-homogeneous recurrence selected.")    

def main():
    ans = input("What type of recurrence relation doy you have in mind? Linear Homogeneous or Non Homogeneous [H/N]").strip().upper()
    if ans == "H":
        homo()
    elif ans == "N":
        non_homo()

main()