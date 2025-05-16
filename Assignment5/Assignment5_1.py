def Sum(No1 , No2):
    return No1 + No2

def Difference(No1 , No2):
    return No1 - No2

def Product(No1 , No2):
    return No1 * No2

def Division(No1 , No2):
    return No1 / No2

def main():

    print("Enter First Number : ")
    iNo1 = int(input())

    print("Enter Second Number : ")
    iNo2 = int(input())

    iRet = Sum(iNo1, iNo2)
    print("Sum : ", iRet)

    iRet = Difference(iNo1, iNo2)
    print("Difference : ", iRet)

    iRet = Product(iNo1, iNo2)
    print("Product : ", iRet)

    iRet = Division(iNo1, iNo2)
    print("Division : ", iRet)

if __name__ == "__main__":
    main()