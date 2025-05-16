
Power = lambda iNo : 2**iNo

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = Power(iNo)
    print("Power of 2 : ", Ret)

if __name__ == "__main__":
    main()