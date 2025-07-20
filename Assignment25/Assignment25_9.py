import pandas as pd

def main():
    data = {'Marks': [45, 67, 88, 32, 76]}
    data = pd.DataFrame(data)
    print(data)
    
    data['Marks'] = data['Marks'].where(data['Marks'] > 50, 'Fail')
    
    print("Data after replace")
    print(data)

if __name__ == "__main__":
    main()