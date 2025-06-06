from functools import reduce

Multiply = lambda no : no * 2

def Prime(no):
    for i in range(2, no):
        if(no % i == 0):
            return False
    return True

def Maximum(A, B):
    return A if A > B else B


def main():

    number = int(input("Enter number of elements : "))
    Data = []

    print("Enter list : ")
    for i in range(number):
        Data.append(int(input()))
    
    print("input list : ",Data)

    print()
    FData = list(filter(Prime, Data))
    print("filter for prime numbers")
    print("list after filter : ",FData)

    print()
    MData = list(map(Multiply, FData))
    print("list after map : multiplying each element by 2 : ",MData)

    print()
    RData = reduce(Maximum, MData)
    print("Output of reduce : Maximum number of list : ",RData)

if __name__ == "__main__":
    main()