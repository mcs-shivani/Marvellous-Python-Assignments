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

    print("Enter the weather in int : [0 : Overcast], [1 : Rainy], [2 : Sunny]")
    wether = int(input())

    print("Enter the temperature in int : [0 : Cool], [1 : Hot], [2 : Mild]")
    temperature = int(input())

    #print("Result : ",model.predict([[wether,temperature]]))

    Result = model.predict(pd.DataFrame({'Whether': [wether], 'Temperature': [temperature]}))

    print("Result : ",Result)
    print(Line)

def CheckAccuracy(Datapath):

    df = pd.read_csv(Datapath)
    df = df.drop(columns= ['Unnamed: 0'])

    Encode = LabelEncoder()
    df['Whether'] = Encode.fit_transform(df["Whether"])
    df['Temperature'] = Encode.fit_transform(df['Temperature'])

    x = df.drop(columns= ['Play'])
    y = df['Play']


    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.5, random_state = 42)

    Accuracy_scores = []
    k_range = range(1,10)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors = k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        Accuracy = accuracy_score(y_test,y_pred)
        print("Accuracy is where Value of K ",k ," : ",Accuracy)
        Accuracy_scores.append(Accuracy)

    best_k = k_range[Accuracy_scores.index(max(Accuracy_scores))]
    print("Best value of k is : ", best_k)

def main():

    PlayPredictor("PlayPredictor.csv")
    CheckAccuracy('PlayPredictor.csv')

if __name__ == "__main__":
    main()