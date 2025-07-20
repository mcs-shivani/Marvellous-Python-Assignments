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

    x = ['Math', 'Science', 'English']
    y = data[data['Name'] == 'Amit'][['Math', 'Science', 'English']].values[0]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit across all subjects")
    plt.show()
    
if __name__ == "__main__":
    main()