import pandas as pd

def main():
   
    data = pd.DataFrame({
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82],
    })

    Line = "-"*85

    data['Total'] = data[['Math', 'Science', 'English']].sum(axis=1)

    data = data.sort_values(by='Total', ascending= False)
    print(Line)
    print("sorted Data by 'Total' in decending order : ")
    print(Line)
    print(data)
    print(Line)
    
if __name__ == "__main__":
    main()