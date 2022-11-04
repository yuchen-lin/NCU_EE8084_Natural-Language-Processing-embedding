from inspect import EndOfBlock
import os
from opencc import OpenCC

inp_path = 'D:/College/4-2/NLP/MedNet/'
oup_path = 'D:/College/4-2/NLP/MedNet_simplify/'
try:
    os.makedirs(oup_path)
except:
    pass
cc = OpenCC('t2s')

print(os.listdir(inp_path))
count = 0

for f in os.listdir(inp_path):
    with open(inp_path + f, 'r', encoding='UTF-8') as file:
        txt = file.read()
        txt = cc.convert(txt)

    with open(oup_path + f, 'w', encoding='UTF-8') as file:
        print(txt, file=file)