import os
import numpy as np
import fasttext

labels = [['原由'], ['疾病'], ['检验'], ['医疗资讯'], ['营养补充'], ['人物机构'], ['症状'], ['治疗']]
model = fasttext.load_model('./cc.zh.300.bin')

all = []
for label in labels:
    ad = [0] * 300
    for i in label:
        temp = model[i]
        ad = [sum(x) for x in zip(ad, temp)]
        print(i)
    
    all.append(np.array([x/len(label) for x in ad]))
    
with open('label_embed.npy', 'wb') as f:
    np.save(f, np.array(all))

print(len(all))