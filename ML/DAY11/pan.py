#Example 1: Grouping by a Single Column

import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
team = df.groupby('Team')
print(team.first()) # Let's print the first entries in all the groups formed.
print(" Grouping by a Single Column")

#Example 2: Grouping by Multiple Columns

import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
grouping = df.groupby(['Team', 'Position'])
print(grouping.first())
print("Grouping by Multiple Columns")

#Example 3 : Applying Aggregation with GroupBy

import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
aggregated_data = df.groupby(['Team', 'Position']).agg(
   total_salary=('Salary', 'sum'),
   avg_salary=('Salary', 'mean'),
   player_count=('Name', 'count')
)
print(aggregated_data)
print("Applying Aggregation with GroupBy")

#Example 4: How to Apply Transformation Methods?

import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
# Rank players within each team by Salary
df['Rank within Team'] = df.groupby('Team')['Salary'].transform(lambda x: x.rank(ascending=False))
print(df)

#Example 5 : Filtering Groups Using Filtration Methods
import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
# Filter groups where the average Salary is >= 5 million
filtered_df = df.groupby('Team').filter(lambda x: x['Salary'].mean() >= 1000000)
print(filtered_df)

#merge()

import pandas as pd

# Create DataFrame for Dataset 1
data1 = [[1, 'Raj', 25], 
         [2, 'Sharma', 42], 
         [3, 'Saroj', 22], 
         [4, 'Raja', 51], 
         [5, 'Kajal', 26]]
df1 = pd.DataFrame(data1, columns=['ID', 'Name', 'Age'])

# Create DataFrame for Dataset 2
data2 = [[1, 'Male', 25000], 
         [2, 'Male', 42500], 
         [3, 'Female', 22300], 
         [4, 'Male', 51400], 
         [5, 'Female', 26800]]
df2 = pd.DataFrame(data2, columns=['ID', 'Gender', 'Salary'])


#Method 1: Inner Merge

# Perform an inner merge on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)

#Method 2: Left Merge
# Perform a left merge on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='left')
print(merged_df)

#Method 3: Right Merge
# Perform a right merge on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='right')
print(merged_df)

#Method 4: Outer Merge
# Perform an outer merge on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='outer')
print(merged_df)

#Method 5: Merging on Multiple Columns

# Example with additional columns
df1['Country'] = ['USA', 'Canada', 'USA', 'Canada', 'USA']
df2['Country'] = ['USA', 'Canada', 'USA', 'Canada', 'Mexico']

# Merge on 'ID' and 'Country'
merged_df = pd.merge(df1, df2, on=['ID', 'Country'], how='inner')
print(merged_df)

#Method 6: Merging with Different Column Names

# Rename 'ID' in df2 to 'EmployeeID' for demonstration
df2.rename(columns={'ID': 'EmployeeID'}, inplace=True)

# Merge using different column names
merged_df = pd.merge(df1, df2, left_on='ID', right_on='EmployeeID', how='inner')
print(merged_df)


#Pandas.pivot()

#Creating a Sample DataFrame

# importing pandas as pd
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'A': ['John', 'Boby', 'Mina'],
                   'B': ['Masters', 'Graduate', 'Graduate'],
                   'C': [27, 23, 21]})

print(df)

#Creating and Pivot a DataFrame

# values can be an object or a list
pivot_df = df.pivot(index='A', columns='B', values='C')
print(pivot_df)


#Creating a Multi-level Pivot Table with Pandas DataFrame

# value is a list
pivot_df=df.pivot(index='A', columns='B', values=['C', 'A'])
print(pivot_df)


#ValueError Raised in Pivoting a DataFrame

import pandas as pd

# creating a dataframe

import pandas as pd

df = pd.DataFrame({
    'A': ['John', 'John', 'Mina'],
    'B': ['Masters', 'Masters', 'Graduate'],
    'C': [27, 23, 21]
})

pivot_df = df.pivot_table(
    index='A',
    columns='B',
    values='C',
    aggfunc='mean'
)

print(pivot_df)