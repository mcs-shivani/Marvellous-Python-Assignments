def ChkNum(iValue):
    if (iValue % 2 == 0) :
        print("Even Number")
    else :
        print("Odd Number") 

def main():
    print("Enter number : ")
    iNumber = int(input())

    ChkNum(iNumber)

if __name__ == "__main__":
    main()
