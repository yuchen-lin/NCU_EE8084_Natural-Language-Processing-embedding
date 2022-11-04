# https://clay-atlas.com/blog/2020/01/17/python-chinese-tutorial-gensim-word2vec/
from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    wiki_corpus = WikiCorpus('zhwiki-20220201-pages-articles-multistream.xml.bz2', dictionary={})
    text_num = 0

    with open('wiki_text.txt', 'w', encoding='utf-8') as f:
        for text in wiki_corpus.get_texts():
            f.write(' '.join(text)+'\n')
            text_num += 1
            if text_num % 10000 == 0:
                print('{} articles processed.'.format(text_num))

        print('{} articles processed.'.format(text_num))