iSum = 0

def Power(number, power):
    if power == 0:
        return 1
    else:
        return number * Power(number, power - 1)


def main():
    number = int(input("Enter number : "))
    power = int(input("Enter power : "))
 
    iRet = Power(number, power)
    print(iRet)

if __name__ == "__main__":
    main()