
def main():

    print("Enter temprature in Celcius : ")
    celcius = int(input())

    F = 0
    F = (celcius * 9/5) + 32

    print("Temperature in Fahrenheit : ", F, "F")

if __name__ == "__main__":
    main()