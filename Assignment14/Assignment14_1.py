
class Employee:
    def __init__(self, A, B, C):
        self.name = A
        self.emp_id = B
        self.salary = C

    def Display(self):
        print("Name : "+self.name, ", ID : ",self.emp_id,", Salary : ",self.salary)

def main():
    Obj = Employee("Rohit", 101, 50000)
    Obj.Display()

    Obj1 = Employee("Virat", 111, 150000)
    Obj1.Display() 

if __name__ == "__main__":
    main()