def Divisible5(iValue):
    if (iValue % 5 == 0):
        print("True")
    else :
        print("False")

def main():
    print("Enter Number : ")
    iNumber = int(input())

    Divisible5(iNumber)

if __name__ == "__main__":
    main()