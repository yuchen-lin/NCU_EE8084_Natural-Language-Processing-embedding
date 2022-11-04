import os

inp_path = 'D:/College/4-2/NLP/MedNet_simplify/'
oup_path = 'D:/College/4-2/NLP/combined.txt'
target_file = inp_path + '18.txt'

with open(oup_path, 'a', encoding='utf-8') as out:
    for f in os.listdir(inp_path):
        out.write('split ')
        out.write(f'{f}\n')
        with open(inp_path + f, 'r', encoding='utf-8') as file:
            out.write(file.read())