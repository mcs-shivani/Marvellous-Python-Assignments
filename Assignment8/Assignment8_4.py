import threading

def SmallCount(iostr):
    iCount = 0
    for i in iostr:
        if(i >= "a" and i <= "z"):
            iCount = iCount + 1
    print("Small : ",iCount)

def CapitalCount(iostr):
    iCount = 0
    for i in iostr:
        if(i >= "A" and i <= "Z"):
            iCount = iCount + 1
    print("Capital : ",iCount)

def DigitCount(iostr):
    iCount = 0
    for i in iostr:
        if(i >= "0" and i <= "9"):
            iCount = iCount + 1
    print("Digit : ",iCount)

def main():
    print("Enter string : ")
    iostr = input()

    small = threading.Thread(target = SmallCount, args = (iostr,))
    capital = threading.Thread(target = CapitalCount, args = (iostr,))
    digit = threading.Thread(target = DigitCount, args = (iostr,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

if __name__ == "__main__":
    main()