def Prime(no):
    for i in range(2,no):
        if(no % i == 0):
            return False
    return True

def main():
    
    print("Enter number of elements : ")
    size = int(input())

    Data = []

    print("Enter list : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    FData = list(filter(Prime, Data))
    print("Prime : ", FData)

if __name__ == "__main__":
    main()