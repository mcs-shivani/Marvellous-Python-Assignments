import threading

def EvenNum():
    for i in range(2,22,2):
        print("Even number thread",i)

def OddNum():
    for i in range(1,20,2):
        print("Odd number thread", i)

def main():

    even = threading.Thread(target = EvenNum)
    odd = threading.Thread(target = OddNum)

    even.start()
    odd.start()
    
    even.join()
    odd.join()
    

if __name__ == "__main__":
    main()