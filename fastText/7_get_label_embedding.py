import os
import numpy as np
import fasttext

labels = [['医疗', '资讯'], ['疾病'], ['症状'], ['原由'], ['检验'], ['治疗'], ['营养', '补充'], ['人物', '机构']]
model = fasttext.load_model('./cc.zh.300.bin')

all = []
for label in labels:
    ad = [0] * 300
    for i in label:
        temp = model[i]
        ad = [sum(x) for x in zip(ad, temp)]
        # print(ad)
    
    all.append(np.array([x/len(label) for x in ad]))
    
with open('label_embed.npy', 'wb') as f:
    np.save(f, np.array(all))

print(len(all))