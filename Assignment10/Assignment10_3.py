from functools import reduce

Greater = lambda no : no >= 70 and no <= 90
Increase = lambda no : no + 10
Product = lambda A, B : A * B

def main():

    number = int(input("Enter number of elements : "))
    Data = []

    print("Enter elements of list  >=70 and <= 90 for FMR : ")
    for i in range(number):
        Data.append(int(input()))
    
    print("Input List : ",Data)

    print()
    FData = list(filter(Greater, Data))
    print("list after filter : ",FData)

    print()
    MData = list(map(Increase, FData))
    print("list after map : increase data by 10 : ",MData)

    print()
    RData = reduce(Product, MData)
    print("Output of reduce : Multiplying all Data : ",RData)

if __name__ == "__main__":
    main()