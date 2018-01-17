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
model_gensim = FT_gensim(size=100, min_count=1)
model_gensim.build_vocab(lee_data)
print model_gensim
model_gensim.train(lee_data, total_examples=model_gensim.corpus_count, epochs=model_gensim.iter)
print model_gensim
print "done training"
test_vector = model_gensim.word_vec('JDK_corpus')
print model_gensim
model_gensim.save('saved_model_for_jdk_corpus')
