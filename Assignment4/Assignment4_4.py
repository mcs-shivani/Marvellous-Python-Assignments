from functools import reduce

CheckEven = lambda no : no % 2 == 0
Square = lambda no : no * no
Addition = lambda A, B : A + B

def main():

    print("Enter number of element : ")
    size = int(input())

    Data = []

    print("Enter Numeric(int) elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input list : ", Data)

    FData = list(filter(CheckEven, Data))
    print("List after filter : ", FData)

    MData = list(map(Square, FData))
    print("List After map : ", MData)

    RData = reduce(Addition, MData)
    print("Reduce Output : ", RData)

if __name__ == "__main__":
    main()