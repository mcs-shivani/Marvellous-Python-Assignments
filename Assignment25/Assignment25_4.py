import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    data = pd.DataFrame({'Department' : ['HR','IT','Finance','HR','IT']})

    print(data)
    Encode = OneHotEncoder(sparse_output=False)
    Department = Encode.fit_transform(data[['Department']])
    EncodeData = pd.DataFrame(Department, columns=Encode.get_feature_names_out())
    data = pd.concat([data, EncodeData], axis=1)

    print()
    print("Data after OneHotEncode : ")
    print(data)

if __name__ == "__main__":
    main()