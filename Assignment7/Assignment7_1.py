
Square = lambda No : No * No
Cube = lambda No : No ** No

def main():

    print("Enter a number : ")
    no = int(input())

    iRet = Square(no)
    print("Square : ")

    iRet = Cube(no)
    print("Cube : ")

if __name__ == "__main__":
    main()