
def CheckVowel(char):
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
       char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        
        print(char , " is a vowel.")
    else:
        print(char , " is a consonant.")

def main():
    print("Enter a character : ")
    char = input()

    CheckVowel(char)

if __name__ == "__main__":
    main()