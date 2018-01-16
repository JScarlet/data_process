#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

from gensim.models.fasttext import FastText as FT_gensim
from gensim.models.word2vec import LineSentence

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) <= 1:
    print "must specific the json file for training fastText word embedding"
    sys.exit(1)
corpus_file_name = sys.argv[1]
lee_data = LineSentence(corpus_file_name)
model_gensim = FT_gensim(size=100, min_count=2)
model_gensim.build_vocab(lee_data)
model_gensim.train(lee_data, total_examples=model_gensim.corpus_count, epochs=model_gensim.iter)
model_gensim.save('saved_model_for_jdk_corpus')
