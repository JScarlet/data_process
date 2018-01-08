#!/usr/bin/python
# -*- coding: UTF-8 -*-
import nltk
from bs4 import BeautifulSoup

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


def sentence_split(text):
    return tokenizer.tokenize(text)


def clean_format(text):
    '''
    clean text format for text extract from html
    :param text:
    :return:
    '''
    return text.replace('\n', ' ').replace("  ", ' ').replace(u'\u00a0', " ")


def clean_html_text(html_text):
    soup = BeautifulSoup(html_text, "lxml")
    cleanText = soup.get_text()
    cleanText = clean_format(cleanText)
    return cleanText


def clean_html_text_with_replacement(html_text):
    '''
    clean the html text with consider <pre> and <li> tag.
    :param html_text:
    :return:
    '''
    if html_text is None or len(html_text) == 0:
        return ""

    soup = BeautifulSoup(html_text, "lxml")
    codeTags = soup.find_all(name=["pre", 'blockquote'])

    for tag in codeTags:
        tag.string = "@C@ . "

    list_groups = soup.find_all(name=["ol", "ul"])
    for list_group in list_groups:
        list_items = list_group.find_all("li")
        num = 1
        for item in list_items:
            item.string = "{0}.{1}\n.".format(str(num), item.string)
            num = num + 1

    # todo: the sentence may lack of Punctuation mark in every <p> tag end. it will be

    cleanText = soup.get_text()
    cleanText = clean_format(cleanText)
    return cleanText
