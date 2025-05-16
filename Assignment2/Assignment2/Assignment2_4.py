def Factors(iNo):
    iSum = 0
    for i in range(1, iNo):
        if((iNo % i) == 0):
            iSum = iSum + i
    return iSum

def main():
    print("Enter the number : ")
    iNum = int(input())

    iRet = Factors(iNum)
    print("Addition of Factors is : ", iRet)

if __name__ == "__main__":
    main()