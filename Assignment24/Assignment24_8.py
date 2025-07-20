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

    MathMarks = data['Math']
    print("Column of Math : ")
    print(MathMarks)
    print(Line)

    plt.figure(figsize= (8, 6))
    plt.hist(MathMarks)
    plt.xlabel('Marks in Math')
    plt.ylabel('Student')
    plt.title("Histogram of Column Math")
    plt.show() 
    
if __name__ == "__main__":
    main()