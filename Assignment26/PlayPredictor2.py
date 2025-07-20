import pandas as pd
from sklearn.preprocessing import LabelEncoder

def PlayPredictor(Datapath):

    Line = "-"*85
    df = pd.read_csv(Datapath)
    print("Dataset is sucessfully imported")
    print(Line)
    print(df.head())
    print(Line)

    df = df.drop(columns= ['Unnamed: 0'])
    print("Dataset After Cleaning : ")
    print(Line)
    print(df.head())
    print(Line)

    Encode = LabelEncoder()
    df['Whether'] = Encode.fit_transform(df["Whether"])
    df['Temperature'] = Encode.fit_transform(df['Temperature'])

    print("Dataset After Encoding : ")
    print(Line)
    print(df.head())
    print(Line)

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()