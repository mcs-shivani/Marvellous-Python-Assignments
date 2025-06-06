iSum = 0

def Sum_n(No):  
    global iSum
    if(No > 0):
        iSum = iSum + No
        No = No - 1
        Sum_n(No)
    return iSum


def main():
    number = int(input("Enter number : "))
    iRet = Sum_n(number)
    print("Sum from 1 to" ,number,"is : ",iRet)

if __name__ == "__main__":
    main()