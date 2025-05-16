def Maximum(size):
    
    Data = []

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    iMax = Data[0]
    for i in range(size):
        if(Data[i] > iMax):
            iMax = Data[i]
    return iMax

def main():
    print("Enter number of element : ")
    size = int(input())

    iRet = Maximum(size)
    print("Maximum element is : ", iRet)

if __name__ == "__main__":
    main()