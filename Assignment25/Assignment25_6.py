import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {'Grade' : ['A+','B','A','C','B+']}

    data = pd.DataFrame(data)
    print(data)

    data['Grade'] = data['Grade'].replace('A+', 'Excellent')
    data['Grade'] = data['Grade'].replace('A', 'Very Good')
    data['Grade'] = data['Grade'].replace('B+', 'Good')
    data['Grade'] = data['Grade'].replace('B', 'Average')
    data['Grade'] = data['Grade'].replace('C', 'Poor')

    print(data)

    
if __name__ == "__main__":
    main()