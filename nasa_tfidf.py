from __future__ import unicode_literals
import json
import os
from textblob import TextBlob
from gensim.models.tfidfmodel import TfidfModel
from gensim.corpora import Dictionary


class JsonCorpus(object):
    def __iter__(self):
        data = json.load(open('../data/nasa.json'))

        desc = [TextBlob(dataset['description'].lower()).tokens for dataset in data['dataset']]

        self.dictionary = Dictionary(desc)

        for d in desc:
            yield self.dictionary.doc2bow(d)


def score(text, tfidf, dictionary):
    return tfidf[dictionary.doc2bow(TextBlob(text.lower()).tokens)]


if __name__ == '__main__':
    if os.path.exists('../data/tfidf.pkl') and os.path.exists('../data/nasa_dictionary.pkl'):
        tfidf = TfidfModel.load('../data/tfidf.pkl')
        dictionary = Dictionary.load('../data/nasa_dictionary.pkl')
    else:
        corpus = JsonCorpus()
        corpus.dictionary.save(self, '../data/nasa_dictionary.pkl')
        dictionary = corpus.dictionary
        tfidf = TfidfModel(corpus, dictionary=corpus.dictionary)
        tfidf.save('../data/tfidf.pkl')

    print score('project completed', tfidf=tfidf, dictionary=dictionary)