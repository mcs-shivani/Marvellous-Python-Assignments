
import time
import threading
import multiprocessing

def Sum():
    sum = 0
    for i in range(1, 10000000+1):
        sum = sum + i
    print(sum)

def main():

    Start_Time = time.time()
    Sum()
    End_Time = time.time()

    print("Execution time of  Summing number from 1 to 10 million using normal function : ", End_Time - Start_Time)

    Start_Time2 = time.time()
    T1 = threading.Thread(target = Sum)
    T1.start()
    T1.join()
    End_Time2 = time.time()

    print("Execution time of  Summing number from 1 to 10 million using threading : ", End_Time2 - Start_Time2)

    Start_Time3 = time.time()
    p = multiprocessing.Process(target = Sum)
    p.start()
    p.join()
    End_Time3 = time.time()

    print("Execution time of  Summing number from 1 to 10 million using multiprocessing : ", End_Time3 - Start_Time3)

if __name__ == "__main__":
    main()