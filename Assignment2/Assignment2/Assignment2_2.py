
def main():
    iNo = int(input("Enter Number : ")) 

    for i in range(iNo):
        for j in range(iNo):
            print("*", end = " ")
        print()

if __name__ == "__main__":
    main()