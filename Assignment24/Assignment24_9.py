import pandas as pd
import numpy as np
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
    data['Gender'] = ['Male', 'Male', 'Female']
    data['Status'] = (data['Total'] > 250).map({True : 'Pass', False : 'Fail'})

    print(Line)
    print(data)
    print(Line)

    data = data.rename(columns= {'Math' : 'Mathmatics'})

    print("Data after rename math to mathmatics : ")
    print(Line)
    print(data)
    print(Line)
 
if __name__ == "__main__":
    main()