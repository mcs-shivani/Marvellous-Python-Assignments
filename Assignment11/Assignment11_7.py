i = 1

def Display():  
    global i 
    if(i <= 4):
        for j in range(i):
            print("*", end = " ")
        i = i + 1
        print()
        Display()

def main():
    Display()

if __name__ == "__main__":
    main()