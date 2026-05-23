import pandas as pd
data=({
        "name":["Ram","Sam"],
        "age":[20,20],
        "marks":[85.5,90.0],
})
df=pd.DataFrame(data)
result=df.select_dtypes(include=['int64'])
print(result)