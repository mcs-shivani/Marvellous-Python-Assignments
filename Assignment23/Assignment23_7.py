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

    x = data['Name']
    y = data['Total']

    plt.figure(figsize= (8,6))
    plt.bar(x, y)
    plt.xlabel("Names")
    plt.ylabel("Total")
    plt.title("Bar Plot Student names vs total marks")
    plt.show()
    
if __name__ == "__main__":
    main()