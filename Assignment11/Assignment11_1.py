i = 1

def Display(no):
    global i
    if(i <= no):
        print(i, end = " ")
        i = i + 1
        Display(no)

def main():
    number = int(input("Enter Number : "))
    Display(number)

if __name__ == "__main__":
    main()