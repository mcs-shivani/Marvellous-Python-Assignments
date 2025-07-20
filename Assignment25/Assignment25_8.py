import pandas as pd
import numpy as np

def main():
    data = {'Marks' : [85,np.nan,90,np.nan,95]}

    data = pd.DataFrame(data)
    print("DataFrame : ")
    print(data)

    data = data['Marks'].interpolate()
    print("DataFrame after interpolate() :")
    print(data)

    
if __name__ == "__main__":
    main()