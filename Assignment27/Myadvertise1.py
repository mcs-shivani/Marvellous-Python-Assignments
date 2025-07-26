import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def Advertise(Datapath):

    # Step : 1 
    # Load Data
    df = pd.read_csv(Datapath)
    print("Dataset Imported Sucessfully")
    print("Sample Data is : ")
    print(df.head())


    # Step : 2 
    # Clean Data
    print("Cleaning Data :")
    df.drop(columns=['Unnamed: 0'], inplace=True)
    print("Updated data is : ")
    print(df.head())

    print("Statistical Summary : ")
    print(df.describe())

    print("Correlation Matrix : ")
    print(df.corr())

    # Step : 3 
    # Train/Test
    x = df[['TV','newspaper','radio']]
    y = df['sales']

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state=42)

    Model = LinearRegression()

    Model.fit(x_train, y_train)
    y_pred = Model.predict(x_test)

    MSE = metrics.mean_squared_error(y_pred,y_test)
    RMSE = np.sqrt(MSE)
    r2 = metrics.r2_score(y_test,y_pred)

    print("Mean Square Error : ", MSE)
    print("Root Mean Square Error : ", RMSE)
    print("r2 value : ", r2)

    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.show()

def main():
    Advertise("Advertising.csv")

if __name__ == "__main__":
    main()