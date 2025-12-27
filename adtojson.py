import json
from readclinrec import readclinrec

link = input()
data = readclinrec(link)
id = data[0]
name = data[1]
link = data[2]
with open("data.json", "r", encoding="utf-8") as file:
    file_data = json.load(file)
delpls = []
for y in file_data:
    if y["ID"] == id:
        delpls.append(y)
file_data = [item for item in file_data if item not in delpls]
for i in data[3]:
    jt = {"ID": id, "name": name, "link": link, "mcb": i}

    file_data.append(jt)
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(file_data, file, ensure_ascii=False)
