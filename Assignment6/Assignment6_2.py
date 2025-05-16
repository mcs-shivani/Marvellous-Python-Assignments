def Sum():

    iSum = 0
    for i in range(1,101):
        if(i % 2 == 0):
            iSum = iSum + i

    print("Sum of even numbers between 1 to 100 is : ", iSum)


def main():

    Sum()

if __name__ == "__main__":
    main()