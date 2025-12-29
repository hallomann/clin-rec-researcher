import pandas as pd
from readclinrec import readclinrec
import json
link=input()

data=readclinrec(link)
id=data[0]
name=data[1]
link=data[2]

df1=pd.DataFrame({'МКБ-10':[], 'ID':[],'Имя':[],'link':[]})

with open('data.json', 'r', encoding='utf-8') as file:
    file_data = json.load(file)
delpls=[]
for y in file_data:
    if y['ID']==id:
        delpls.append(y)
file_data= [item for item in file_data if item not in delpls]

for i in data[3]:
    df1=pd.concat(
        [
            df1,
            pd.DataFrame(
                {'МКБ-10':[i], 'ID':[id],'Имя':[name],'link':[link]}
            ),
        ],
        ignore_index=True,
    )

    file_data.append({'ID':id,'name':name,'link':link,'mcb':i})

df2=pd.read_csv('data/out.csv')
df2 = df2[df2.ID != data[0]]
ndf=pd.concat([df2,df1])
ndf=ndf.sort_values(by='МКБ-10')
ndf.to_csv('data/out.csv',index=False)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(file_data, file, ensure_ascii=False)
