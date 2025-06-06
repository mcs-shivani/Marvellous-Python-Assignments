import multiprocessing

def Fact(Data):  
        Fact = 1
        for i in range(1,Data+1):
            Fact = Fact * i
        return Fact

def main():
    number = int(input("Enter number of elements : "))
    Data = []

    print("Enter elements of list : ")
    for i in range(number):
        Data.append(int(input()))

    Result = []

    p = multiprocessing.Pool()
    print("Factorial of a numbers in a list : ")
    Result = p.map(Fact, Data)
    
    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()