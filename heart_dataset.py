import pandas as pd

# Loading the dataset
heart_train = pd.read_csv('dataset/heart_train.tsv', sep='\t')
heart_test = pd.read_csv('dataset/heart_test.tsv', sep='\t')

# Checking for missing values
missing_values = heart_train.isna().sum()
print(missing_values)

# No missing values found
# Taking the predictions from the dataframe
heart_disease = heart_train.iloc[:,heart_train.shape[1]-1]
print(heart_train.head())

for i in range(heart_train.shape[1]-1):
    column = heart_train.iloc[:,i]
