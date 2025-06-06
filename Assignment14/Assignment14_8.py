
class Vehicle:
    def Start(self):
        print("In vehicle start")

class Car(Vehicle):
    def Start(self):
        print("In Car start")

def main():
    Obj1 = Vehicle()
    Obj2 = Car()
    
    Obj1.Start()
    Obj2.Start()

if __name__ == "__main__":
    main()