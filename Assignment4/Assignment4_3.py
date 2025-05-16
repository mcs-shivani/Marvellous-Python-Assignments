from functools import reduce

Greater = lambda no : no >= 70 and no <= 90
Increase = lambda no : no + 10
Product = lambda A, B : A * B

def main():

    print("Enter Number of elements : ")
    size = int(input())

    Data = []

    print("Enter Numberic elements only : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input list : ", Data)

    FData = list(filter(Greater, Data))
    print("List after filter : ", FData)

    MData = list(map(Increase, FData))
    print("List after filter map :", MData)

    RData = reduce(Product, MData)
    print("Output of Reduce : ", RData)

if __name__ == "__main__":
    main()