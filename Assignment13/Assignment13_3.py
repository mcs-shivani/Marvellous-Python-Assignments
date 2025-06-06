
class Numbers:
    def __init__(self, A):
        self.Value = A

    def ChkPrime(self):
        for  i in range(2,self.Value+1):
            if(self.Value % i == 0):
                return False
            else:
                return True


    def ChkPerfect(self):
        iSum = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                iSum = iSum + i

        if(iSum == self.Value):
            return True
        else:
            return False

    def SumFactors(self):
        iSum = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                iSum = iSum + i
        print("Sum of factors : ", iSum)
        #return iSum


    def Factors(self):
        print("Factors of",self.Value," : ") 
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i, end = " ")
        print()

def main():

    Obj1 = Numbers(11)
    iRet = Obj1.ChkPrime()
    if(iRet == True):
        print("11 is prime number")
    else:
        print("11 is not prime number")

    iRet = Obj1.ChkPerfect()
    if(iRet == True):
        print("11 is Perfect number")
    else:
        print("11 is not Perfect number")

    Obj1.Factors()
    Obj1.SumFactors()

    print()

    print("Enter a number : ")
    no = int(input())

    Obj2 = Numbers(no)
    iRet = Obj2.ChkPrime()
    if(iRet == True):
        print(no, "is prime number")
    else:
        print(no, "is not prime number")

    iRet = Obj2.ChkPerfect()
    if(iRet == True):
        print(no, "is Perfect number")
    else:
        print(no, "is not Perfect number")

    Obj2.Factors()
    Obj2.SumFactors()
    
if __name__ == "__main__":
    main()