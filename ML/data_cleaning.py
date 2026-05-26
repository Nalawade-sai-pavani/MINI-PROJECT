import pandas as pd
import numpy as np

data = {
    'House_id':[101,102,103,104,105,106,107],
    'Price':['25000','30000',np.nan,'14000','35000','50000',np.nan],
    'Bedrooms':[3,4,5,np.nan,4,3,2],
    'Area_sqft':['1500','2000','unknown','2500','2000','3000','1800']
}

df = pd.DataFrame(data)

print("RAW DATA:")
print(df)
print("Data Type:\n",df.dtypes)
print("\n Missing values count :\n",df.isnull().sum())
print("\n Duplicates Rows:",df.duplicated().sum())
print("\n--CLEANING TYPES--")
df['Price']=pd.to_numeric(df['Price'])
df['Area_sqft']=pd.to_numeric(df['Area_sqft'],errors='coerce')
print(df.dtypes)
print("\n--HANDLING MISSING VALUES--")
Price_Median=df['Price'].median()
df['Price']=df['Price'].fillna(Price_Median)
Area_Mean=df['Area_sqft'].mean()
df['Area_sqft']=df['Area_sqft'].fillna(Area_Mean)
Bedrooms_Mean=df['Bedrooms'].mean()
df['Bedrooms']=df['Bedrooms'].fillna(Bedrooms_Mean)
print(df.dtypes)
print(df)