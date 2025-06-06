iFact = 1

def Factorial(no):
    global iFact
    if(no >= 1):
        iFact = iFact * no
        no = no - 1
        Factorial(no)
    return iFact

def main():
    number = int(input("Enter Number : "))

    iRet = Factorial(number)
    print("Factorial : ",iRet)

if __name__ == "__main__":
    main()