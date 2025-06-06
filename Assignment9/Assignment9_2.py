import multiprocessing
import os

def square(no):
    print(no * no)

def main():

    number = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements of list : ")
    for i in range(number):
        Data.append(int(input()))

    for i in Data:
        p = multiprocessing.Process(target=square, args=(i,))

        p.start()
        p.join()


if __name__ == "__main__":
    main()