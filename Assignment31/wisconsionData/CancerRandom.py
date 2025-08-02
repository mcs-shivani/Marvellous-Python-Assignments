import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns


def Cancer(Datapath):

    Line = '-'*80
    # Importing Data from CSV
    Data = pd.read_csv(Datapath)
    print("Dataset imported Sucessfully")
    print(Line)
    print("Sample Dataset : ")
    print(Line)
    print(Data.head())
    print(Line)
    
    # Cleaning Data from Dataframe
    Data.drop(columns=['CodeNumber'] , inplace=True)
    print("Sample Dataset After Cleaning : ")
    print(Line)
    print(Data.head())
    print(Line)
    print("Column Names : ")
    print(Line)
    print(Data.columns)
    print(Line)

    # Replace '?' with NaN
    Data['BareNuclei'] = Data['BareNuclei'].replace('?', np.nan)
    
    # Convert 'BareNuclei' to numeric
    Data['BareNuclei'] = pd.to_numeric(Data['BareNuclei'], errors='coerce')
    mean_BareNuclei = Data['BareNuclei'].mean()
    
    # Replace NaN with mean
    Data['BareNuclei'] = Data['BareNuclei'].fillna(mean_BareNuclei)

    # Caheacking dataset NULL values
    print("Checking NULL values : ")
    print(Line)
    print(Data.isnull().sum())
    Data.dropna(inplace=True)
    print(Line)

    # Encoding the Data
    Encode = LabelEncoder()
    Data["CancerType"] = Encode.fit_transform(Data["CancerType"])
    print("Data after Encoding : ")
    print(Line)
    print(Data.head())
    print(Line)
    
    # Splitting the Data
    X = Data.drop(columns=['CancerType'], axis=1)
    Y = Data["CancerType"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    Model = RandomForestClassifier(n_estimators=15,max_depth=17,random_state=42)

    Model.fit(X_train,Y_train)
    Y_pred = Model.predict(X_test)

    # Calculate Confusion Matrix
    Corr = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix : ")
    print(Line)
    print(Corr)
    print(Line)

    # Calculate Receiver Operating Characteristic (ROC)
    Y_pred_proba = Model.predict_proba(X_test)
    Roc = roc_curve(Y_test, Y_pred_proba[:, 1])

    print("ROC Value : ")
    print(Line)
    print(Roc)
    print(Line)

    # Area Under the Curve (AUC)
    Auc = roc_auc_score(Y_test, Y_pred_proba[:, 1])
    print("AUC Value : ")
    print(Line)
    print(Auc)
    print(Line)

    # Plot ROC Curve
    plt.plot(Roc[0], Roc[1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show()

    # Calculate Confusion Matrix
    Accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy : ", Accuracy*100)
    print(Line)

    # Visual Representation 
    sns.pairplot(Data, hue='CancerType', palette='Blues')
    plt.title("Pairplot of CancerType")
    plt.show()

    x = Data.drop(columns=['CancerType'], axis=1)
    y = Data['CancerType']

    sns.heatmap(Corr, annot=True, color='red')
    plt.title("HeatMap of Confusion Matrix")
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.show()

    # Histograms for each feature
    for column in x.columns:
        plt.hist(x[column], bins=10, edgecolor = 'black')
        plt.title(column)
        plt.show()

    # Feature Importance Displaying
    importance = pd.Series(Model.feature_importances_, index=X.columns)
    importance = importance.sort_values(ascending=False)

    importance.plot(kind='bar', figsize=(8,6), title='Feature Importance')
    plt.show()

def main():
    Cancer("breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()