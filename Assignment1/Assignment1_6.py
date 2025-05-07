def ChkNum(iValue):
    if(iValue == 0):
        print("Zero")
    elif(iValue < 0):
        print("Negative Number")
    else :
        print("Positive Number")

def main():
    print("Enter Number : ")
    iNumber = int(input())
    ChkNum(iNumber)

if __name__ == "__main__":
    main()