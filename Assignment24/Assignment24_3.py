import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

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
    print(Line)
    print(data)
    
    data['Average'] = np.average(data[['Math', 'Science', 'English']], axis=1)

    group = data.groupby('Gender')

    print(Line)
    print("Data After Adding Average : ")
    print(Line)
    print(data)
    print(Line)
    print("Data After Group : ")
    print(Line)
    print(group.sum())
    print(Line)

    
if __name__ == "__main__":
    main()