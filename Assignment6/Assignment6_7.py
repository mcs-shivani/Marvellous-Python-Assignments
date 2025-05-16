
def Maximum(Values):
    iMax = Values[0]

    for i in range(5):
        if(iMax < Values[i] ):
            iMax = Values[i]
    
    print("Maximun number is : ", iMax)

def main():

    print("Enter Five Numbers : ")

    Data = []

    for i in range(5):
        no = int(input())
        Data.append(no)

    print(Data)
    Maximum(Data)

if __name__ == "__main__":
    main()