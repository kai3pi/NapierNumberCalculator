import sys
from decimal import Decimal, getcontext

def calculate_e(precision):
    getcontext().prec = precision + 1
    e = Decimal(0)
    factorial = Decimal(1)
    for i in range(precision):
        if i > 0:
            factorial *= i
        e += Decimal(1) / factorial
    return e

if __name__ == "__main__":
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])  #Get number of digits from command line
    else:
        digits = 10  #Default value when there are no command line arguments

    e = calculate_e(digits)
    print(str(e))
