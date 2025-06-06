import threading

def EvenFact(no):

    iSum = 0
    for i in range(2,no + 1, 2):
        if(no % i == 0):
            iSum = iSum + i
    print("Addition of EvenFactors : ",iSum)

def OddFact(no):
    iSum = 0
    for i in range(1,no + 1,2):
        if(no % i == 0):
            iSum = iSum + i
    print("Addition of OddFactors : ",iSum)

def main():

    number = int(input("Enter Number : "))
    print()

    evenfactor = threading.Thread(target = EvenFact, args=(number,))
    oddfactor = threading.Thread(target = OddFact, args=(number,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()
    

if __name__ == "__main__":
    main()