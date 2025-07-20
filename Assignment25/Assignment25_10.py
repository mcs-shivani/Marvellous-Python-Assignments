import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {'Age': [25, 30, 45, 35, 22],
            'Salary' : [50000,60000,80000,65000,45000],
            'Purchased' : [1,0,1,0,1]}

    data = pd.DataFrame(data)
    print(data)

    data = data.drop('Age', axis=1)
    print("Data after removing Age : ")
    print(data)

    x = data['Salary']
    y = data['Purchased']

    X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state=42)

    print("X_train : ")
    print(X_train)
    print("X_test")
    print(X_test)
    print("Y_train : ")
    print(Y_train)
    print("Y_test")
    print(Y_test)

if __name__ == "__main__":
    main()