iCount = 0

def Count_Zeros(no):
   
    global iCount
    if(no > 0):
        digit = no % 10
        if(digit == 0):
            iCount = iCount + 1
        no = no // 10
        Count_Zeros(no)
    return iCount

def main():
    number = int(input("Enter number : "))

    iRet = Count_Zeros(number)
    print("Zero in number : ",iRet)

if __name__ == "__main__":
    main()