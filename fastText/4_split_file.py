import os
from opencc import OpenCC

cc = OpenCC('s2t')

inp_path = 'D:/College/4-2/NLP/combined_split.txt'
oup_path = 'D:/College/4-2/NLP/MedNet_simplify_split/'
oup_path2 = 'D:/College/4-2/NLP/MedNet_traditional_split/'

try:
    os.makedirs(oup_path)
except:
    pass
try:
    os.makedirs(oup_path2)
except:
    pass

with open(inp_path, 'r', encoding='utf-8') as f:
    txt = f.read()
    for t in txt.split('split')[1:]:
        to_save = t
        file_name = t.split('\n')[0]
        to_save = to_save.replace(file_name + '\n', '')
        file_name = file_name.replace(' ', '')
        with open(oup_path + file_name, 'w', encoding='utf-8') as save:
            save.write(to_save)
        with open(oup_path2 + file_name, 'w', encoding='utf-8') as save:
            save.write(cc.convert(to_save))
        