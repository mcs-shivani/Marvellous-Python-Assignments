import pandas as pd
import numpy as np

def main():
   
    data2 = pd.DataFrame({
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [np.nan,76,88],
        'Science' : [91,np.nan,85],
    })

    Line = "-" * 85

    print(Line)
    print(data2)
    print(Line)

    meanMath = data2['Math'].mean()  
    meanSci = data2['Science'].mean()

    print(meanMath)
    print(meanSci)
    
    data2['Math'] = data2['Math'].fillna(meanMath)
    data2['Science'] = data2['Science'].fillna(meanSci)
    print(data2)

    
if __name__ == "__main__":
    main()