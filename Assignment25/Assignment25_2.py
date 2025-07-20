import numpy as np
from scipy import stats
import pandas as pd

def main():
    data = pd.DataFrame({'Name' : ['A','B','C'], 'Age' : [21.0,22.0,23.0]})

    print(data)
    
    data['Age'] = list(map(int, data['Age']))

    print("Data after Converting float into int : ")
    print(data)

if __name__ == "__main__":
    main()