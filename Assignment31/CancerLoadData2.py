from sklearn.datasets import load_breast_cancer
import pandas as pd

def Cancer(Datapath):

    Line = '-'*80

    Data = pd.read_csv(Datapath)
    print("Dataset imported sucessfully")
    print(Line)
    print("Sample Dataset is : ")
    print(Line)
    print(Data.head())
    print(Line)
    print("Checking Null Value : ")
    print(Line)
    print(Data.isnull().sum())
    print(Line)
def main():
   
    Cancer('breast_cancer.csv')
    
if __name__ == "__main__":
    main()