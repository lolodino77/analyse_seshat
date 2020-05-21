import pandas
import os
print(os.getcwd())
print(get)
df = pandas.read_csv('socompindexe.csv')
print(df['Index'])
print(df.columns)
df[['Index', 'Date']] = df.Index.str.split("(",expand=True)

for date in df['Date']:
    date = date.strip(")")
df['Date'] = [date.strip(")") for date in df['Date']]

print(df)

df[['Date']] = columnSplit[1]
print(columnSplit[1])
print(df['A'])
print(df['B'])

df.to_csv(r'new.csv', index = False)

df = pandas.read_csv('new.csv')
print(df)
print(df.columns)
