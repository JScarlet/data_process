#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

import nltk
from bs4 import BeautifulSoup, Comment

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
pattern = re.compile(r'\s+')


def sentence_split(text):
    return tokenizer.tokenize(text)


def clean_format(text):
    '''
    clean text format for text extract from html
    :param text:
    :return:
    '''
    return re.sub(pattern, " ", text.replace('\n', ' ').replace(u'\u00a0', " "))


def clean_html_text(html_text):
    if html_text is None or html_text == "":
        return ""
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

    soup = get_main_contain_body(soup)

    remove_all_comment_block(soup)

    replace_code_tag(soup)

    replace_li_tag(soup)

    # todo: the sentence may lack of Punctuation mark in every <p> tag end. it will be

    cleanText = soup.get_text()
    cleanText = clean_format(cleanText)

    return cleanText


def replace_li_tag(soup):
    list_groups = soup.find_all(name=["ol", "ul"])
    for list_group in list_groups:
        list_items = list_group.find_all("li")
        num = 1
        for item in list_items:
            item.string = "{0}.{1}\n.".format(str(num), item.string)
            num = num + 1


def replace_code_tag(soup):
    codeTags = soup.find_all(name=["pre", 'blockquote'])
    for tag in codeTags:
        tag.string = "@C@ . "


def remove_all_comment_block(soup):
    all_comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in all_comments:
        comment.extract()


def get_main_contain_body(soup):
    contain_tags = soup.find_all("div", class_="contentContainer")
    if contain_tags and len(contain_tags) >= 1:
        for contain_tag in contain_tags:
            soup = contain_tag
    jd_content = soup.find('div', id="jd-content")
    if contain_tags:
        soup = jd_content
    return soup
