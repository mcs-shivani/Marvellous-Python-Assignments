import threading

def Digit():
    for i in range(1, 51, 1):
        print(i)

def DigitRev():
    for i in range(50, 0, -1):
        print(i)

def main():

    thread1 = threading.Thread(target = Digit)
    thread1.start()
    thread1.join()
    
    thread2 = threading.Thread(target = DigitRev)
    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()