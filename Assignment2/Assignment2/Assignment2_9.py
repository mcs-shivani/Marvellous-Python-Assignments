def Digit(iNo):
    iDigit = 0
    iCount = 0

    if(iNo < 0):
        iNo = (-iNo)
         
    while(iNo > 0):
        iDigit = int(iNo % 10)
        iCount = iCount + 1
        iNo = int(iNo / 10)
    
    return iCount

def main():
    print("Enter the number : ")
    iNum = int(input())

    iRet = Digit(iNum)
    print("Digits are : ", iRet)

if __name__ == "__main__":
    main()