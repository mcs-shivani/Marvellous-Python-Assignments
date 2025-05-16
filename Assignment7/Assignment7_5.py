
def Reverse(string):
    strrev = ""
    for i in string:
        strrev = i + strrev
    return strrev

def main():
    
    print("Enter string : ")
    string = input()

    
    bRet = Reverse(string)

    if(bRet == string):
        print(string, "is a Palindrome")
    else :
        print(string, "is not a Palindrome")

if __name__ == "__main__":
    main()