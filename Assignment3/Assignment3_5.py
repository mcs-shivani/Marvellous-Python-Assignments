from MarvellousNum import ChkPrime

def ListPrime(size):
    iSum = 0
    Data = []

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    for i in range(size):
        bRet = ChkPrime(Data[i])
        
        if(bRet == True):
            iSum = iSum + Data[i]
    
    return iSum

def main():
    print("Enter number of element : ")
    size = int(input())

    iRet = ListPrime(size)
    print("Addition of prime element is : ", iRet)

if __name__ == "__main__":
    main()