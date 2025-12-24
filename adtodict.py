# -*- codecs: utf-8 -*-
import codecs
def adtodict(name):
    with codecs.open('clindict.py', 'r', "utf-8") as file:
        e=file.readlines()
    ind=name.find(' ')
    e.insert(-1,f"          '{name[:ind]}' : '{name}',\n")
    e=''.join(e)
    with codecs.open('clindict.py','w', "utf-8") as file:
        file.write(e)