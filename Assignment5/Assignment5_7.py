def Area(length, width):
    return length * width

def Perimeter(length, width):
    return 2 * (length + width)

def main():

    print("Enter length : ")
    length = int(input())

    print("Enter width : ")
    width = int(input())

    iRet = Area(length, width)
    print("Area : ", iRet)

    iRet = Perimeter(length, width)
    print("Perimeter : ", iRet)

if __name__ == "__main__":
    main()