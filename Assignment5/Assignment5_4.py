
def main():
    print("Enter three number : ")
    No1 = int(input())
    No2 = int(input())
    No3 = int(input())

    if(No1 > No2):
        print("Largest Number : ", No1)
    elif(No2 > No3):
        print("Largest Number : ", No2)
    elif(No3 > No1):
        print("Largest Number : ", No3)

if __name__ == "__main__":
    main()