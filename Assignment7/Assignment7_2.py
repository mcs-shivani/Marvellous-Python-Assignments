def Double(no):
    return 2 * no

def main():

    print("Number of elements :")
    size = int(input())

    Data = []

    print("Enter list : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    MData = list(map(Double, Data))
    print("Doubled list : ", MData)


if __name__ == "__main__":
    main()