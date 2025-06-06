from functools import reduce

Even = lambda no : no % 2 == 0
Square = lambda no : no * no
Addition = lambda A, B : A + B

def main():

    number = int(input("Enter number of elements : "))
    Data = []

    print("Enter list : ")
    for i in range(number):
        Data.append(int(input()))
    
    print("input list : ",Data)

    print()
    FData = list(filter(Even, Data))
    print("filter for even")
    print("list after filter : ",FData)

    print()
    MData = list(map(Square, FData))
    print("list after map : calculating square of elements : ",MData)

    print()
    RData = reduce(Addition, MData)
    print("Output of reduce : Additon of all elements : ",RData)

if __name__ == "__main__":
    main()