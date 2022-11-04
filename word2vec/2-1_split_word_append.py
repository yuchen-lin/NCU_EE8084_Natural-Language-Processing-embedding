# https://clay-atlas.com/blog/2020/01/17/python-chinese-tutorial-gensim-word2vec/
# coding: utf-8
from ckip_transformers.nlp import CkipWordSegmenter
import os

# Ckip
ws_driver = CkipWordSegmenter(level=3, device=0)
# ws_driver = CkipWordSegmenter(level=3, device=-1)

# Tokenize
data_folder = 'D:/College/4-2/NLP/MedNet/'
txt_num = len(os.listdir(data_folder))
times = 0
with open(f'wiki_text_seg.txt', 'a', encoding='utf-8') as new_f:
    for d in os.listdir(data_folder):
        with open(data_folder + d, 'r', encoding='utf-8') as f:
            txt = f.read()
            times += 1
            try:
                print(f'{times}/{txt_num}')
                data = ws_driver([txt])
                data = [word.strip() for word in data[0] if word != ' ']
                data = ' '.join(data)

                new_f.write(f'{data}\n')
            except:
                print('GPU memory overloaded, trying CPU...')
                ws_driver = CkipWordSegmenter(level=3, device=-1)
                print(f'{times}/{417370}')
                data = ws_driver(data)
                data = [word.strip() for word in data[0] if word != ' ']
                data = ' '.join(data)

                new_f.write(data)
                print('Going back to GPU...')
                ws_driver = CkipWordSegmenter(level=3, device=0)