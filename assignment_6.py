import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Amit'],
    'Marks': [85, 90, None, 85],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

print("\nStudents scoring above 80:")
print(df.loc[df['Marks'] > 80])
