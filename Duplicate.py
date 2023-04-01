import pandas as pd
import os
final=pd.DataFrame()
# r"C:\Users\pavan\Downloads
path = './Downloads/Telegram Desktop/Pandas'
for file in os.listdir(path):
    if 'data2' in file:
        p=path+'/'+file
        print(p)
        d=pd.read_csv(p)
        df=pd.DataFrame(d)
df1=df[['Registration Number','Student Name']].value_counts()
df1
