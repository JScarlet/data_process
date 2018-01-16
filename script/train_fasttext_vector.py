#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import sys

from gensim.models.fasttext import FastText as FT_gensim
from gensim.models.word2vec import LineSentence

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) <= 1:
    print "must specific the json file for training fastText word embedding"
    sys.exit(1)
corpus_file_name = sys.argv[1]
with codecs.open(corpus_file_name, 'r', 'utf-8') as corpus_file:
    lee_data = LineSentence(corpus_file)
    model_gensim = FT_gensim(size=100, min_count=2)
    # train the model
    model_gensim.train(lee_data, total_examples=model_gensim.corpus_count, epochs=model_gensim.iter)
    model_gensim.save('saved_model_for_jdk_corpus')
