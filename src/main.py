import pandas as pd
def load_data(filepath="data/IBM_Churn.csv"):

 df = pd.read_csv(filepath)
 return df
