import pandas as pd
from sklearn.preprocessing import minmax_scale

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
    data['Normal_Math'] = minmax_scale(data['Math'])
    print(data)
    print(Line)

    
if __name__ == "__main__":
    main()