import pandas as pd

def main():
   
    data = pd.DataFrame({
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82],
    })

    data['Total'] = data[['Math', 'Science', 'English']].sum(axis=1)

    Line = "-"*85

    #print(data['Science'] > 85)                          #showing boolean Values
    #print([data['Science'] > 85, 'Name'])                #showing boolean Values

    print(Line)
    print("Student names who scored more than 85 in Science : ")
    print(Line)
    print(data.loc[data['Science'] > 85, 'Name'])        #.loc method = to specify row/col
    print(Line)
    
if __name__ == "__main__":
    main()