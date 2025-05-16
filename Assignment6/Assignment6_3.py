
def Table(No):

    for i in range(1,11):
        print(No ,"*", i ,"=", (No * i))

def main():

    print("Enter a number : ")
    iNo = int(input())

    Table(iNo)

if __name__ == "__main__":
    main()