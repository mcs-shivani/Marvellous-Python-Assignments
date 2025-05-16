
def main():
    print("Enter a number : ")
    Num = int(input())

    if((Num % 2) == 0):
        print(Num , "is an even number")
    else:
        print(Num , "is an odd number")

if __name__ == "__main__":
    main()