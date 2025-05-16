from functools import reduce

def Prime(no):
    for i in range(2, no):
        if(no % i == 0):
            return False
    return True

def Multiplicaton(no):
    return no * 2

def Maximum(A, B):
    return A if A > B else B      

def main():

    print("Enter the number of elements : ")
    size = int(input())

    Data = []

    print("Enter Numeric(int) elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input list : ", Data)

    FData = list(filter(Prime, Data))
    print("list after filter : ", FData)

    MData = list(map(Multiplicaton, FData))
    print("list after map : ", MData)
    
    RData = reduce(Maximum, MData)
    print("Output of reduce : ", RData)

if __name__ == "__main__":
    main()