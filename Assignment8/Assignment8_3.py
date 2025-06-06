import threading

def even(Data):
    EvenSum = 0
    for i in Data:
        if(i % 2 == 0):
            EvenSum = i + EvenSum
    print("Addition of all even elements : ",EvenSum)

def odd(Data):
    OddSum = 0
    for i in Data:
        if(i % 2 != 0):
            OddSum = i + OddSum
    print("Addition of all odd elements : ",OddSum)

def main():

    number = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements of list : ")
    for i in range(number):
        Data.append(int(input()))
    
    print(Data)

    evenlist = threading.Thread(target = even, args=(Data,))
    oddlist = threading.Thread(target = odd, args=(Data,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

if __name__ == "__main__":
    main()