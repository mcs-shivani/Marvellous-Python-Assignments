import threading
import time

def Digit():
    for i in range(1, 51, 1):
        print(i)


def main():

    thread1 = threading.Thread(target = Digit)
    thread1.start()

    time.sleep(1)

    thread2 = threading.Thread(target = Digit)
    thread2.start()

    time.sleep(1)

    thread3 = threading.Thread(target = Digit)
    thread3.start()

if __name__ == "__main__":
    main()