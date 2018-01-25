from bs4 import BeautifulSoup

from util.code_text_process import get_main_contain_body, remove_all_comment_block
from util.relation import Relation


def __filter_code_element_in_link(tag):
    return tag.name == 'a' and len(tag.contents) == 1 and tag.contents[0].name == 'code'


def __filter_link_in_code_element(tag):
    return tag.name == 'code' and len(tag.contents) == 1 and tag.contents[0].name == 'a'


def __filter_links_in_code_element(tag):
    '''<code><b><a href="../../../com/google/gson/TypeAdapterFactory.html#create(com.google.gson.Gson, com.google.gson.reflect.TypeToken)">create</a></b>(<a href="../../../com/google/gson/Gson.html" title="class in com.google.gson">Gson</a>&nbsp;gson,
       <a href="../../../com/google/gson/reflect/TypeToken.html" title="class in com.google.gson.reflect">TypeToken</a>&lt;T&gt;&nbsp;type)</code>'''
    return tag.name == 'code' and len(tag.contents) > 1


def __extract_link_relation_from_link(code_element_link, base_url):
    result = []
    subject = code_element_link.get_text()
    if subject is None or subject is "":
        return result
    else:
        subject = subject.strip()
    link = code_element_link.get("href")
    if link is None:
        return result

    if link.startswith("http"):
        if '/guide/' in link or '/guides/' in link:
            r = Relation(subject=subject, relation='has guide in', object=link)
        else:
            r = Relation(subject=subject, relation='has hyperlink to', object=link)
        result.append(r)
    else:
        if base_url is not "" and link.startswith("../"):
            '''for
             <a href="../../../com/google/gson/JsonDeserializer.html#deserialize(com.google.gson.JsonElement, java.lang.reflect.Type, com.google.gson.JsonDeserializationContext)"><code>JsonDeserializer.deserialize(JsonElement, Type, JsonDeserializationContext)</code></a>'''
            link_string = link.replace("../", "")
            link_string = base_url + "/" + link_string
            r = Relation(subject=subject, relation='has hyperlink to', object=link_string)
            result.append(r)
    return result


def __extract_relation_in_title_attr_in_link(a_tag):
    '''example:<a href="../../java/awt/Container.html" title="class in java.awt">Container</a>'''
    title = a_tag.get("title")
    if title is None or title is "":
        return None
    value = " in "
    if value in title:
        words = title.split(value)
        r = words[0] + value
        text = a_tag.get_text()
        if text is None or text is "":
            return None
        else:
            return Relation(subject=text.strip(), relation=r.strip(), object=words[1].strip())
    else:
        return None


def extract_relation_from_html(html_text, base_url=""):
    soup = BeautifulSoup(html_text, "lxml")
    relations_set = set([])

    soup = get_main_contain_body(soup)
    remove_all_comment_block(soup)
    code_tag_list = soup.find_all(['code', 'pre'])



    for code_element in code_tag_list:
        '''
        for all <a> in <code>.
        <code><b><a href="../../../com/google/gson/TypeAdapterFactory.html#create(com.google.gson.Gson, com.google.gson.reflect.TypeToken)">create</a></b>(<a href="../../../com/google/gson/Gson.html" title="class in com.google.gson">Gson</a>&nbsp;gson,
       <a href="../../../com/google/gson/reflect/TypeToken.html" title="class in com.google.gson.reflect">TypeToken</a>&lt;T&gt;&nbsp;type)</code>
        
        example2:
        <pre>public &lt;T extends <a href="http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/annotation/Annotation.html?is-external=true" title="class or interface in java.lang.annotation">Annotation</a>&gt; T <b>getAnnotation</b>(<a href="http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/Class.html?is-external=true" title="class or interface in java.lang">Class</a>&lt;T&gt;&nbsp;annotation)</pre>
        '''
        a_link_list = code_element.find_all('a')
        for a_link in a_link_list:
            result = __extract_link_relation_from_link(a_link, base_url)
            for r in result:
                relations_set.add(r)
            r = __extract_relation_in_title_attr_in_link(a_link)
            if r is not None:
                relations_set.add(r)

    '''for <a> with one <code> in'''
    code_element_link_list = soup.find_all(__filter_code_element_in_link)
    for code_element_link in code_element_link_list:
        result = __extract_link_relation_from_link(code_element_link, base_url)

        for r in result:
            relations_set.add(r)

        r = __extract_relation_in_title_attr_in_link(code_element_link)
        if r is not None:
            relations_set.add(r)

    return relations_set
