
class Calculator:
    def __init__(self, A, B):
        self.Value1 = A
        self.Value2 = B

    def Addition(self):
        print("Addition : ", self.Value1 + self.Value2)

    def Substraction(self):
        print("Substraction : ", self.Value1 - self.Value2)

    def Multiplication(self):
        print("Multiplication : ", self.Value1 * self.Value2)

    def Division(self):
        print("Division : ", self.Value1 / self.Value2)

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    Obj1 = Calculator(no1, no2)
    Obj1.Addition()
    Obj1.Substraction()
    Obj1.Multiplication()
    Obj1.Division()

if __name__ == "__main__":
    main()