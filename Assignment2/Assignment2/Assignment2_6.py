def Pattern(iNo):
    for i in range(iNo):
        for j in range(iNo):
            print("*", end = " ")
        iNo = iNo - 1
        print()

def main():
    print("Enter the number : ")
    iNum = int(input())

    Pattern(iNum)

if __name__ == "__main__":
    main()