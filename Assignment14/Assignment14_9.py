
class Product:
    def __init__(self, A, B):
        self.name = A
        self.price = B

    def __eq__(self, C):
        if(self.price == C):
            return True
        return False

def main():
    Pobj = Product("ABC", 500)
    
    iRet = Pobj.__eq__(500)
    if(iRet == True):
        print("Equal in price")
    else:
        print("Not Equal in price")

if __name__ == "__main__":
    main()