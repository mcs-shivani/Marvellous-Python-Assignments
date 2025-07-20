import pandas as pd

def main():
    data = pd.DataFrame({'City' : ['Pune','Mumbai','Delhi','Pune','Delhi']})

    print(data)
    data = data['City'].map({'Pune' : 1, 'Mumbai' : 2,'Delhi' : 3})
    print(data)

if __name__ == "__main__":
    main()