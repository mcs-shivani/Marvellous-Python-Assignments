def CheckPrime(iNo):
    if iNo > 1 :
        for i in range(2, iNo):
            if(iNo % i == 0):
                return False
        return True
    else :
        return False

def main():
    print("Enter the number : ")
    iNum = int(input())

    bRet = CheckPrime(iNum)
    if(bRet == True):
        print("Prime Number")
    else :
        print("Not Prime Number")

if __name__ == "__main__":
    main()