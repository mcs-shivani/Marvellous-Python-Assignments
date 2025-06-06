
class Circle :
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, A):
        self.Radius = A

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        return self.Circumference

    def Display(self):
        print("Radius : ", self.Radius)
        print("Area of Circle : ", self.CalculateArea())
        print("Circumference of Circle : ", self.CalculateCircumference())
    
def main():

    print()
    obj1 = Circle()
    obj1.Accept(10.5)
    obj1.Display()

    print()
    obj2 = Circle()
    obj2.Accept(12.7)
    obj2.Display()
    
    print()
    obj3 = Circle()
    obj3.Accept(7.7)
    obj3.Display()

    print()
    radius = float(input("Enter radius : "))
    obj4 = Circle()
    obj4.Accept(radius)
    obj4.Display()

if __name__ == "__main__":
    main()