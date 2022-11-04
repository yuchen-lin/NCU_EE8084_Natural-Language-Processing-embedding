import os
import subprocess

splitter_loc = 'D:/College/4-2/NLP/embedding_5_fasttext/stanford-segmenter-2020-11-17/segment.bat'
inp_path = 'D:/College/4-2/NLP/combined.txt'
oup_path = 'D:/College/4-2/NLP/combined_split.txt'

# try:
#     os.makedirs(oup_path)
# except:
#     pass

subprocess.run(f'{splitter_loc} pku {inp_path} UTF-8 0 > {oup_path}')