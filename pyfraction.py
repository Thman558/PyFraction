import psutil
import datetime

last_reboot = psutil.boot_time()
print(datetime.datetime.fromtimestamp(last_reboot))

from fractions import Fraction

chooseoperand = input("What operation would you like to use? Eg: x, /, +, - ")

if chooseoperand == "x":
        timesfraction1 = input("What is the first fraction you would like to multiply? ")
        timesfraction2 = input("What is the 2nd fraction you would like to multiply? ")
        print(Fraction(timesfraction1)*Fraction(timesfraction2))
        quit()


if chooseoperand == "+":    
        fraction1 = input("What Is The First Fraction Would You Like to Add? ")
        fraction2 = input("What is the 2nd fraction you wanna add?: ")
        print(Fraction(fraction1)+Fraction(fraction2))
        quit()

if chooseoperand == "-":    
        fraction1 = input("What Is The First Fraction Would You Like to subtract? ")
        fraction2 = input("What is the 2nd fraction you wanna subtract?: ")
        print(Fraction(fraction1)-Fraction(fraction2))
        quit()

if chooseoperand == "/":    
        fraction1 = input("What Is The First Fraction Would You Like to Divide?: ")
        fraction2 = input("What is the 2nd fraction you wanna Divide?: ")
        print(Fraction(fraction1)/Fraction(fraction2))
else:
            print("ERROR: Invalid Command Please enter x, /, +, -: ")