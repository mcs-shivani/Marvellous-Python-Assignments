from functools import reduce

Product = lambda A, B : A * B

def main():
    
    print("Enter number of elements : ")
    size = int(input())

    Data = []

    print("Enter list : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    RData = reduce(Product, Data)
    print("Product : ", RData)

if __name__ == "__main__":
    main()