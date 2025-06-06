iSum = 0

def Sum_of_Digit(no):
    iDigit = 0
    global iSum
    if(no > 0):
        iDigit = no % 10
        iSum = iSum + iDigit
        no = no // 10
        Sum_of_Digit(no)
    return iSum

def main():
    number = int(input("Enter number : "))
    iRet = Sum_of_Digit(number)
    print("Sum of Digits : ",iRet)

if __name__ == "__main__":
    main()