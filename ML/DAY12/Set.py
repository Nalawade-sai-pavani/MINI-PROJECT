import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\HP\Desktop\hackathon\ML\data.csv")
print(df)


df['price_per_calorie']=df['Pulse']/df['Calories']
df['price_per_calorie']=df['price_per_calorie'].round(2)
print(df)

df['Date']=pd.to_datetime(df['Date'],errors='coerce')
df['Month']=df['Date'].dt.month
print(df)

df['is_high_pulse']=np.where(df['Pulse']>120, 1, 0)
print(df[['Pulse','is_high_pulse']])