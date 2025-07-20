import pandas as pd
import numpy as np
from scipy import stats

def main():
    data = pd.DataFrame({'Salary' : [25000,27000,29000,31000,50000,100000]})

    print(data)
    q1 = np.percentile(data['Salary'], 25)
    q2 = np.percentile(data['Salary'], 50)
    q3 = np.percentile(data['Salary'], 75)

    IQR = q3 - q1

    print("IQR of Data : ",IQR)

    print("IQR of Data  using stat.iqr() : ",stats.iqr(data['Salary']))

if __name__ == "__main__":
    main()