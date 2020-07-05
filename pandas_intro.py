
pd.head()
df = pd.read_csv('path/to/file.csv')

#get column
df['column']

#get single row
df.iloc[2]
#get row range
df.loc[2:5]

#get column and row
#df.iloc [[rows],[column]]
df.iloc[[0,1,],['A']] #get row 0 and 1 under column A

