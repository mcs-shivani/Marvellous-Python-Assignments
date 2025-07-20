import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {'Age' : [22,25,47,52,46,56], 'Purchased' : [0,1,1,0,1,0]}

    df = pd.DataFrame(data)

    x = data['Age']
    y = data['Purchased']

    X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state=42)

    print("X_train")
    print(X_train)
    print("X_test")
    print(X_test)
    print("Y_train")
    print(Y_train)
    print("Ytest")
    print(Y_test)

if __name__ == "__main__":
    main()