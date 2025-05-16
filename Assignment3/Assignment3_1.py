
def Addition(size):
    Data = []

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    iSum = 0
    for i in range(size):
        iSum = iSum + Data[i]
    return iSum

def main():
    print("Enter Number of elements : ")
    size = int(input())

    iRet = Addition(size)
    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()