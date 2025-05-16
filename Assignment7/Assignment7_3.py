
def Even(no):
    return no % 2 == 0

def main():
    
    print("Enter number of element : ")
    size = int(input())

    Data = []

    print("Enter list : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    FData = list(filter(Even, Data))
    print("Even : ", FData)

if __name__ == "__main__":
    main()