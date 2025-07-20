import pandas as pd

def main():
   
   data = pd.DataFrame({
       'Name' : ['Amit', 'Sagar', 'Pooja'],
       'Math' : [85,90,78],
       'Science' : [92,88,80],
       'English' : [75,85,82]
   })

   Line = "-"*85

   print(Line)
   print("Data from file is : ")
   print(Line)
   print(data)
   print(Line)
   print("Shape of the Data : ", data.shape)
   print("Columns of Data : ", data.columns)
   print(Line)

if __name__ == "__main__":
    main()