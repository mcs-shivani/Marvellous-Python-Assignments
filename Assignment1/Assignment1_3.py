def Add(iValue1, iValue2):
    iAns = 0
    iAns = iValue1 + iValue2
    return iAns

def main():
    print("Enter First Number : ")
    iNo1 = int(input())
    print("Enter Second Number : ")
    iNo2 = int(input())

    iRet = Add(iNo1, iNo2)
    print("Addition is : ", iRet)

if __name__ == "__main__":
    main()