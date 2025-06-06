
class Rectangle:
    def __init__(self, A, B):
        self.length = A
        self.width = B

    def Area(self):
        print("Area of Rectangle : ",self.length * self.width)

    def Perimeter(self):
        print("Perimeter of Rectangle : ",2 * (self.length + self.width))


def main():

    Obj1 = Rectangle(11,21)
    Obj1.Area()
    Obj1.Perimeter()

    print()

    print("Enter the length : ")
    length = int(input())

    print("Enter the width : ")
    width = int(input())

    Obj2 = Rectangle(length, width)
    Obj2.Area()
    Obj2.Perimeter()
    

if __name__ == "__main__":
    main()