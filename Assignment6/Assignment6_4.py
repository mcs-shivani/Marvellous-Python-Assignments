
def Factorial(Num):

    iFact = 1

    for i in range(1, Num + 1):
        iFact = iFact * i
    return iFact


def main():
    print("Enter a number : ")
    iNo = int(input())

    iRet = Factorial(iNo)
    print("Factorial of", iNo, "is : ",iRet)

if __name__ == "__main__":
    main()