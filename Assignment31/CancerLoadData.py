from sklearn.datasets import load_breast_cancer
import pandas as pd

def main():
   
    data = load_breast_cancer()
    
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    df['target_name'] = df['target'].apply(lambda x: data.target_names[x])

    df.to_csv('breast_cancer.csv', index=False)
    
if __name__ == "__main__":
    main()