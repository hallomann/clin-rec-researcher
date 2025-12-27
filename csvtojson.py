import json
import pandas as pd

data = pd.read_csv("out.csv")
ids = data["ID"].unique()
with open("data.json", "r", encoding="utf-8") as file:
    file_data = json.load(file)

for i in ids:
    d = data[data["ID"] == i]
    name = d["Имя"].unique()[0]
    link = d["link"].unique()[0]
    delpls = []
    for y in file_data:
        if y["ID"] == id:
            delpls.append(y)
    file_data = [item for item in file_data if item not in delpls]
    for str in d["МКБ-10"].values.tolist():
        jt = {"ID": i, "name": name, "link": link, "mcb": str}
        file_data.append(jt)
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(file_data, file, ensure_ascii=False)
