import pandas as pd

def main():
   
    data = pd.DataFrame({
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    })

    Line = "-"*85

    print(Line)
    print("Statistical Information of Data : ")
    print(Line)
    print(data.describe())
    print(Line)

if __name__ == "__main__":
    main()