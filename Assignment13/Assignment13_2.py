
class BankAccount:
    ROI = 10.5

    def __init__(self, A, B):
        self.Name = A
        self.Amount = B

    def Deposit(self, Deposit):
        self.Amount = self.Amount + Deposit
        return self.Amount

    def Withdraw(self, withdraw):
        if(self.Amount < withdraw):
            print("Insufficient Balance!")
        else :
            self.Amount = self.Amount - withdraw
        return self.Amount

    def CalculateInterest(self):
        pass

    def Display(self):
        print("Name : "+self.Name)
        print("Available Balance : ",self.Amount)

def main():
    Obj1 = BankAccount("Shivani", 500)
    Obj1.Deposit(500)
    Obj1.Withdraw(400)
    Obj1.Display()

    print()

    Name = input("Enter Name : ")
    Amount = int(input("Enter Amount : "))

    Obj2 = BankAccount(Name, Amount)
    Obj2.Display()

    print()
    Deposit_Amt = int(input("Enter an Amount that you want to Deposit : "))
    Obj2.Deposit(Deposit_Amt)
    Obj2.Display()

    print()
    Withdraw_Amt = int(input("Enter an Amount that you want to Withdraw : "))
    Obj2.Withdraw(Withdraw_Amt)
    Obj2.Display()

    
if __name__ == "__main__":
    main()