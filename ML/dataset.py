import pandas as pd
df=pd.DataFrame({
    'customer_id':[1,2,3],
    'customer_name':['Alice','Bob','Charalie'],
    'product_name':['Weight','Gadeget','Thingamjig'],
    'product_price':[19.99,29.99,39.99],
    'product_data':[pd.Timestamp('2024-01-01'),pd.Timestamp('2024-01-02'),pd.Timestamp('2024-01-03')],

})
print(df)