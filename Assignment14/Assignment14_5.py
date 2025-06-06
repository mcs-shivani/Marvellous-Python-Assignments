
class BankAccount:
    def __init__(self, A, B, C):
        self.account_number = A
        self.name = B
        self.balance = C

    def Deposit(self, deposit):
        self.balance = self.balance + deposit
        print("Deposited : ",deposit)  
        print()   

    def Withdraw(self, withdraw):
        self.balance = self.balance - withdraw
        print("Withdrawl : ", withdraw)
        print()

    def Display(self):
        print("Name : "+self.name)
        print("Balance : ", self.balance)
        print()

def main():
    Obj1 = BankAccount(101, "Shivani", 1000)
    Obj1.Display()
    Obj1.Deposit(500)
    Obj1.Display()
    Obj1.Withdraw(700)
    Obj1.Display()

if __name__ == "__main__":
    main()