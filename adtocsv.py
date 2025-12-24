import pandas as pd
from readclinrec import readclinrec
link=input()
data=readclinrec(link)
df1=pd.DataFrame({'ID':[data[0]],'Имя':[data[1]],'link':[data[2]],'МКБ-10':[data[3]]})
df2=pd.read_csv('output.csv')
df2 = df2[df2.ID != data[0]]
ndf=pd.concat([df2,df1])
ndf=ndf.sort_values(by='МКБ-10')
ndf.to_csv('output.csv',index=False)