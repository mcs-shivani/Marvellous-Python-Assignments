
class Arithmetic:
    def __inin__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self, A, B):
        self.Value1 = A
        self.Value2 = B
    
    def Addition(self):
        #return self.Value1 + self.Value2
        print("Addition : ",self.Value1 + self.Value2)
    
    def Substraction(self):
        #return self.Value1 - self.Value2
        print("Substraction : ",self.Value1 - self.Value2)
    
    def Multiplication(self):
        print("Multiplication : ",self.Value1 * self.Value2)
    
    def Division(self):
        print("Division : ",self.Value1 / self.Value2)

def main():
    obj1 = Arithmetic()
    obj1.Accept(10,11)

    #iRet = obj1.Addition()
    #print("Addition : ", iRet)
    print("Object 1 passed values 10,11 : ")
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()

    print()

    obj2 = Arithmetic()
    obj2.Accept(50, 25)
    print("Object 2 passed values 50,25 : ")
    obj2.Addition()
    obj2.Substraction()
    obj2.Multiplication()
    obj2.Division()

    print()

    obj3 = Arithmetic()
    obj3.Accept(11,7)
    print("Object 2 passed values 11,7 : ")
    obj3.Addition()
    obj3.Substraction()
    obj3.Multiplication()
    obj3.Division()

    print()
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    print()
    obj4 = Arithmetic()
    obj4.Accept(no1,no2)
    obj4.Addition()
    obj4.Substraction()
    obj4.Multiplication()
    obj4.Division()

if __name__ == "__main__":
    main()