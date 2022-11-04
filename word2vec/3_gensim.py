from gensim.models import word2vec

# Settings
seed = 666
sg = 0
window_size = 10
vector_size = 300
min_count = 1
workers = 8
epochs = 5
batch_words = 10000

train_data = word2vec.LineSentence('wiki_text_seg.txt')

model = word2vec.Word2Vec(
    train_data,
    min_count=min_count,
    vector_size=vector_size,
    workers=workers,
    epochs=epochs,
    window=window_size,
    sg=sg,
    seed=seed,
    batch_words=batch_words
)

model.save('word2vec.model')