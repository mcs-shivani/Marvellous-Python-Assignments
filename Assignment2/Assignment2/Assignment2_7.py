def Pattern(iNo):
    for i in range(iNo):
        for j in range(1, iNo + 1):
            print(j, end = " ")
        print()

def main():
    print("Enter the number : ")
    iNum = int(input())

    Pattern(iNum)

if __name__ == "__main__":
    main()