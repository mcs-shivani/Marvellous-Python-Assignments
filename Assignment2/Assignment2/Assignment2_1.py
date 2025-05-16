import Arithmetic

def main():
    iNo1 = int(input("Enter First Number : "))
    iNo2 = int(input("Enter Second Number : "))

    if(iNo1 < 0):
        iNo1 = -iNo1
    if(iNo2 < 0):
        iNo2 = -iNo2

    Ret = Arithmetic.Add(iNo1, iNo2)
    print("Addition is : ", Ret)

    Ret = Arithmetic.Sub(iNo1, iNo2)
    print("Substraction is : ", Ret)

    Ret = Arithmetic.Mult(iNo1, iNo2)
    print("Multiplication is : ", Ret)

    Ret = Arithmetic.Div(iNo1, iNo2)
    print("Division is : ", Ret)


if __name__ == "__main__":
    main()