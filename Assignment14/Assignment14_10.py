
class Employee :
    def __init__(self, A, B, C):
        self.__salary = A
        self._department = B
        self.name = C

    def Display(self):
        print("Private (__salary) : ", self.__salary)
        print("Protected (_department) : ", self._department)
        print("Public (name) : ", self.name)

def main():
    Eobj = Employee(25000, "IT", "Amit")
    Eobj.Display()

    print()
    print("In main Function : ")
    print("Name : "+Eobj.name)
    print("Department : "+Eobj._department)
    print("Salary : ", Eobj.__salary)

if __name__ == "__main__":
    main()