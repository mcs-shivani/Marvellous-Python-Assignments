
def ChkPrime(iNo):
    if(iNo > 1):
        for i in range(2, iNo):
            if(iNo % i == 0):
                return False
        return True
    else :
        return False
