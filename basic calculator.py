
import cmath
import numpy as np
while True:
        
        client=input("Type: (QF) for quadratic formula, (plus) for addition, (minus) for subtraction, (multiply) for multiplication, (divivde) for division, Type (exit) for exit: ")
        

        


        try:
            def solve(a,b,c):
                    D1=b**2-4*a*c
                    imaginary=cmath.sqrt(abs(-D1))/(2*a)
                    pos=-b+cmath.sqrt(D1)/(2*a)
                    neg=-b-cmath.sqrt(D1)/(2*a)
                    if D1==0:
                        print("x1, x2= ", str(-b/(2*a)))
                    elif D1>0:
                        print("x1= ", str(pos), "x2= ", str(neg))
                    else:
                        print("x1= ", str(-b/(2*a)),"+i",str(imaginary))
                        print("x2= ", str(-b/(2*a)),"-i",str(imaginary))

            if client=="QF":
                a=int(input("type value of a: "))
                b=int(input("type value of b: "))
                c=int(input("type value of c: "))
                print(solve(a,b,c))
                
               





            def minus(y):
                total1=y[0]
                for num in y[1:]:
                    total1-=num
                return total1

            def multiply(z):
                total2=z[0]
                for num in z[1:]:
                    total2=num*total2
                return total2
            def divide(o):
                total4=o[0]
                for num in o[1:]:
                    total4=total4/num
                return total4

            if client=="QF":
                a=int(input("type value of a: "))
                b=int(input("type value of b: "))
                c=int(input("type value of c: "))
                print(solve(a,b,c))

            elif client=="plus":
                ss=input("type numbers in a line with GAPS: ")
                s=ss.split()
                s=[int(num) for num in s]
                print(s)
                u=list(s)
                total=np.array(u).sum()
                print(total)

            elif client=="minus":
                ss=input("type numbers in a line with GAPS: ")
                s=ss.split()
                s=[int(num) for num in s]
                print(s)
                print(minus(s))

            elif client=="multiply":
                ss=input("type numbers in a line with GAPS: ")
                s=ss.split()
                s=[int(num) for num in s]
                print(s)
                print(multiply(s))

            elif client=="divide":
                ss=input("type numbers in a line with GAPS: ")
                s=ss.split()
                s=[int(num) for num in s]
                print(s)
                print(divide(s))
            elif input("You want to exitt? (y/n)").lower()=="y":
                break


    

            else:
                print("")
              
        except ValueError:
            print("ERROR")


    
    