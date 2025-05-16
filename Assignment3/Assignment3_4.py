def Frequency(size):
    iFreq = 0
    
    Data = []

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Enter element to search : ")
    iNo = int(input())
    
    for i in range(size):
        if(Data[i] == iNo):
            iFreq = iFreq + 1
    return iFreq

def main():
    print("Enter number of element : ")
    size = int(input())

    iRet = Frequency(size)
    print("Frequency of element is : ", iRet)

if __name__ == "__main__":
    main()