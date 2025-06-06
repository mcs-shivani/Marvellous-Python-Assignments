
class Book:
    def __init__(self,A):
        self.__price = A

    def get_Price(self):
        print("Price : ", self.__price)

    def set_Price(self, A):
        self.__price = A
        print("Updated Price : ", A)

def main():
    Obj1 = Book(1000)
    Obj1.get_Price()
    Obj1.set_Price(1500)
    Obj1.get_Price()

if __name__ == "__main__":
    main()