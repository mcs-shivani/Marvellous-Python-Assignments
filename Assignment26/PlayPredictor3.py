import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

    x = df.drop(columns= ['Play'])
    y = df['Play']

    x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 42)

    model = KNeighborsClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy is : ",Accuracy)
    print(Line)

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()