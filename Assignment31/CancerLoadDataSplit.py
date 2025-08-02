from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, roc_auc_score, roc_curve

def Cancer(Datapath):

    Line = '-'*80

    df = pd.read_csv(Datapath)
    print("Dataset imported sucessfully")
    print(Line)
    print("Sample Dataset is : ")
    print(Line)
    print(df.head())
    print(Line)
    print("Checking Null Value : ")
    print(Line)
    print(df.isnull().sum())
    print(Line)
    print(df.shape)
    print(df.columns)

    X = df.drop(columns=['target', 'target_name'], axis=1)
    Y = df['target']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    Model = DecisionTreeClassifier()

    Model.fit(X_train,Y_train)
    Y_pred = Model.predict(X_test)


def main():
   
    Cancer('breast_cancer.csv')
    
if __name__ == "__main__":
    main()