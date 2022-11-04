import os
import numpy as np
import csv
from mxnet.contrib import text
import torch.utils.data as data_utils
import torch
import re

#https://www.kaggle.com/datasets/jefferyhe168/mednet-chinese-multilabel-text-classification
data_path = 'D:/College/4-2/NLP/MedNet_traditional_split/'
sheet = 'D:/College/4-2/NLP/label_5folds(Lin).csv'

cv1=[]
cv2=[]
cv3=[]
cv4=[]
cv5=[]

total_num = len(os.listdir(data_path))

#https://www.kaggle.com/datasets/linycyuchen/fasttext
embed = text.embedding.CustomEmbedding('./word_embed.txt')

with open(sheet, newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows)
    for row in rows:
        try:
            with open(data_path + row[0] + '.txt', 'r', encoding='utf-8') as f:
                paragraph = []
                count = 0
                txt = f.read()
                split_txt_list = re.split(' |\n', txt)
                for i in split_txt_list:
                    if count >= 500:
                        break
                    try:
                        paragraph.append(embed.token_to_idx[i])
                        count += 1
                    except:
                        print('indecipherable word:', i, ' from file:', row[0])

                while(1):
                    if count < 500:
                        paragraph.append(1)
                        count += 1
                    else:
                        break
            
            if row[9] == '1':
                cv1.append({'id': int(row[0]), 'content': paragraph, 'label': [float(i) for i in row[1:9]]})
            elif row[9] == '2':
                cv2.append({'id': int(row[0]), 'content': paragraph, 'label': [float(i) for i in row[1:9]]})
            elif row[9] == '3':
                cv3.append({'id': int(row[0]), 'content': paragraph, 'label': [float(i) for i in row[1:9]]})
            elif row[9] == '4':
                cv4.append({'id': int(row[0]), 'content': paragraph, 'label': [float(i) for i in row[1:9]]})
            elif row[9] == '5':
                cv5.append({'id': int(row[0]), 'content': paragraph, 'label': [float(i) for i in row[1:9]]})

        except:
            print('missing file:', row[0])

with open('X_train_cv1.npy', 'wb') as f:
    np.save(f, np.array([x['content'] for x in cv1]))
with open('y_train_cv1.npy', 'wb') as f:
    np.save(f, np.array([x['label'] for x in cv1]))
with open('X_train_cv2.npy', 'wb') as f:
    np.save(f, np.array([x['content'] for x in cv2]))
with open('y_train_cv2.npy', 'wb') as f:
    np.save(f, np.array([x['label'] for x in cv2]))
with open('X_train_cv3.npy', 'wb') as f:
    np.save(f, np.array([x['content'] for x in cv3]))
with open('y_train_cv3.npy', 'wb') as f:
    np.save(f, np.array([x['label'] for x in cv3]))
with open('X_train_cv4.npy', 'wb') as f:
    np.save(f, np.array([x['content'] for x in cv4]))
with open('y_train_cv4.npy', 'wb') as f:
    np.save(f, np.array([x['label'] for x in cv4]))
with open('X_train_cv5.npy', 'wb') as f:
    np.save(f, np.array([x['content'] for x in cv5]))
with open('y_train_cv5.npy', 'wb') as f:
    np.save(f, np.array([x['label'] for x in cv5]))

print('cv1第1篇：')
x = cv1[0]
content = [list(embed.token_to_idx.keys())[x] for x in x['content']]
print('id=', x['id'])
print('label=', x['label'])
print('content = ')
print(content)