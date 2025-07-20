import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
   
    data = pd.DataFrame({
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82],
    })

    Line = "-"*85

    data['Total'] = data[['Math', 'Science', 'English']].sum(axis=1)

    data['Gender'] = ['Male', 'Male', 'Female']
    print(Line)
    print(data)
    
    #data = data['Gender'].map({'Female' : 0, 'Male' : 1})

    Encode = OneHotEncoder(sparse_output=False)
    Gender = Encode.fit_transform(data[['Gender']])
    Encodedata = pd.DataFrame(Gender, columns=Encode.get_feature_names_out())
    data = pd.concat([data, Encodedata], axis=1)
    print(Line)
    print("Data After OneHotEncoding : ")
    print(Line)
    print(data)
    print(Line)

    
if __name__ == "__main__":
    main()