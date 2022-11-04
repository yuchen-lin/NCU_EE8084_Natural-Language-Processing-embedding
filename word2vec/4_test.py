from gensim.models import word2vec

model = word2vec.Word2Vec.load('word2vec.model')
words = ['原由', '疾病', '檢驗', '醫療', '資訊', '營養', '補充', '人物', '機構', '症狀', '治療']
# embedding = model.wv[word]
# print('shape = ', embedding.shape)
# print('embedding = ', [x for x in embedding.tolist()])

print('Loading...')
for w in words:
    print('-------------------')
    print(w)
    for item in model.wv.most_similar(w):
        print(item)