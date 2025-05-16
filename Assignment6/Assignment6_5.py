
def Prime(iNo):
    for i in range(2,iNo):
        if(iNo % i == 0):
            return False
        else :
            return True

def main():

    print("Enter a number : ")
    iNo = int(input())

    bRet = Prime(iNo)
    if(bRet == True):
        print(iNo, "is a prime number")
    else :
        print(iNo, "is not a prime number")

if __name__ == "__main__":
    main()