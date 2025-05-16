def Digit(iNo):
    iDigit = 0
    iSum = 0

    if(iNo < 0):
        iNo = (-iNo)
         
    while(iNo > 0):
        iDigit = int(iNo % 10)
        iSum = iSum + iDigit
        iNo = int(iNo / 10)
    
    return iSum

def main():
    print("Enter the number : ")
    iNum = int(input())

    iRet = Digit(iNum)
    print("Addition of Digits are : ", iRet)

if __name__ == "__main__":
    main()