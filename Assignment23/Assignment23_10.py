import pandas as pd
import matplotlib.pyplot as plt

def main():
   
    data = pd.DataFrame({
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82],
    })

    Line = "-"*85

    data['Total'] = data[['Math', 'Science', 'English']].sum(axis=1)

    print(Line)
    print(data)
    print(Line)

    data.drop(columns='English', inplace=True)
    print(Line)
    print("Data after drop English column")
    print(Line)
    print(data)
    print(Line)
    
if __name__ == "__main__":
    main()