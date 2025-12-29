# -*- codecs: utf-8 -*-
import codecs
import ast

def adtodict(name):
    with codecs.open('clindict.py', 'r', "utf-8") as file:
        e=file.read()
    
    ind=name.find(' ')
    mydict=ast.literal_eval(e[9:])
    mydict.update({name[:ind]:name})
    e=f'thisdict={mydict}'

    with codecs.open('clindict.py','w', "utf-8") as file:
        file.write(e)
