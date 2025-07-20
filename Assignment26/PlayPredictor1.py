import pandas as pd

def PlayPredictor(Datapath):

    df = pd.read_csv(Datapath)
    print("Dataset is sucessfully imported")
    print(df.head())

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()