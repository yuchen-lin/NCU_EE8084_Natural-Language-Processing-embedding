# https://clay-atlas.com/blog/2020/01/17/python-chinese-tutorial-gensim-word2vec/
# coding: utf-8
from ckip_transformers.nlp import CkipWordSegmenter
from opencc import OpenCC


# Initial
cc = OpenCC('s2t')

# Ckip
ws_driver = CkipWordSegmenter(level=3, device=0)
# ws_driver = CkipWordSegmenter(level=3, device=-1)

# Tokenize
with open(f'wiki_text_seg.txt', 'w', encoding='utf-8') as new_f:
    with open('wiki_text.txt', 'r', encoding='utf-8') as f:
        for times, data in enumerate(f, 1):
            try:
                print(f'{times}/{417370}')
                data = [cc.convert(data)]
                data = ws_driver(data)
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