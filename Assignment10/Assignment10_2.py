
Multiplication = lambda no1, no2 : no1 * no2

def main():

    number1 = int(input("Enter 1st Number : "))
    number2 = int(input("Enter 2nd Number : "))

    iRet = Multiplication(number1, number2)
    print("Multiplication : ",iRet)

if __name__ == "__main__":
    main()