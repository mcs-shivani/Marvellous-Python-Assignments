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


    print(Line)
    print(data)
    print(Line)

    data2 = data[data['Name'] == 'Sagar']
    x = data2[['Math', 'Science', 'English']].values.flatten()

    print(Line)
    print("Data of Sagar : ")
    print(data2)
    print("Marks : ",x)
    print(Line)

    label = ('Math', 'Science', 'English')

    plt.figure(figsize= (8,5))
    plt.title("Sagar's marks pie chart")
    plt.pie(x, labels=label)
    plt.show()
    
if __name__ == "__main__":
    main()