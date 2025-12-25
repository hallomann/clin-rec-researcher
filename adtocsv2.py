import pandas as pd
from readclinrec import readclinrec

link = input()

data = readclinrec(link)
df1 = pd.DataFrame({"МКБ-10": [], "ID": [], "Имя": [], "link": []})
for i in data[3]:
    df1 = pd.concat(
        [
            df1,
            pd.DataFrame(
                {"МКБ-10": [i], "ID": [data[0]], "Имя": [data[1]], "link": [data[2]]}
            ),
        ],
        ignore_index=True,
    )
df2 = pd.read_csv("out.csv")
df2 = df2[df2.ID != data[0]]
ndf = pd.concat([df2, df1])
ndf = ndf.sort_values(by="МКБ-10")
ndf.to_csv("out.csv", index=False)
