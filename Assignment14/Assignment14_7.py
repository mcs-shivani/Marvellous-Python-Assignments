
class Person :
    def __init__(self, A, B):
        self.name = A
        self.age = B

class Teacher(Person):
    def __init__(self, A, B, C, D):
        super().__init__(A, B)
        self.subject = C
        self.salary = D
    
    def Display(self):
        print("Name : "+self.name)
        print("Age : ", self.age)
        print("Subject : "+self.subject)
        print("Salary : ", self.salary)

def main():
    #Obj1 = Person()
    Obj1 = Teacher("Amit", 25, "IT", 50000)
    Obj1.Display()

if __name__ == "__main__":
    main()