import pandas as pd
from sklearn.preprocessing import minmax_scale
def main():
    data = {'Age' : [18,22,25,30,35]}

    data = pd.DataFrame(data)

    print(data)

    data['Age'] = minmax_scale(data['Age'])

    print(data)

    
if __name__ == "__main__":
    main()