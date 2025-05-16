def Minimum(size):
    
    Data = []

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    iMin = Data[0]
    for i in range(size):
        if(Data[i] < iMin):
            iMin = Data[i]
    return iMin

def main():
    print("Enter number of element : ")
    size = int(input())

    iRet = Minimum(size)
    print("Minimum element is : ", iRet)

if __name__ == "__main__":
    main()