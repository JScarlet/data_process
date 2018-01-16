#!/usr/bin/python
# -*- coding: UTF-8 -*-
from unittest import TestCase

import nltk

from util.code_text_process import clean_html_text, clean_html_text_with_replacement, sentence_split
from util.html_relation_extractor import extract_relation_from_html


class TestRemove_all_tags(TestCase):
    def test_remove_all_tags(self):
        text_html = '''<div class="post-text" itemprop="text">

<p>I want to show a simple pop-up banner based on if a cookie is present or not. This is the python code I have</p>

<pre class="lang-py prettyprint prettyprinted" style=""><code><span class="pln">consent_cookie_str </span><span class="pun">=</span><span class="pln"> self</span><span class="pun">.</span><span class="pln">request</span><span class="pun">.</span><span class="pln">cookies</span><span class="pun">.</span><span class="pln">get</span><span class="pun">(</span><span class="str">'consent'</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> consent_cookie_str</span><span class="pun">:</span><span class="pln">
            </span><span class="pun">//</span><span class="pln"> show banner here</span></code></pre>

<p>What is the best way to show the banner if the cookie isn't present? Passing parameters into my jinja template?</p>

<p>Thanks</p>
    </div>'''
        text = clean_html_text(text_html)
        print text

        description_list = sentence_split(text)
        print description_list

        text = clean_html_text_with_replacement(text_html)
        print text

        description_list = sentence_split(text)
        print description_list

        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r

    def test_remove_all_tags_1(self):
        text_html = '''<pre><a href="../../java/applet/Applet.html" title="class in java.applet">Applet</a> getApplet(<a href="../../java/lang/String.html" title="class in java.lang">String</a> name)</pre>'''
        text = clean_html_text(text_html)
        print text

        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r

    def test_remove_all_tags_2(self):
        text_html = '''<div class="block">Returns an <code>Image</code> object that can then be painted on
  the screen. The <code>url</code> argument that is
  passed as an argument must specify an absolute URL.
  <p>
  This method always returns immediately, whether or not the image
  exists. When the applet attempts to draw the image on the screen,
  the data will be loaded. The graphics primitives that draw the
  image will incrementally paint on the screen.</p></div>'''
        text = clean_html_text(text_html)
        description_list = sentence_split(text)
        print description_list
        print text

        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r

    def test_remove_all_tags_3(self):
        text_html = '''<div class="post-text" itemprop="text">

<p>I made a simple typescript component with a html page that has a ListView and I wanted to get the item that i just tapped in a console log, but it doesn't even trigger the event when debugging. Tested it with the an emulator for the android version 7.1.1.</p>

<p>home.component.ts:</p>

<pre class="default prettyprint prettyprinted" style=""><code><span class="kwd">import</span><span class="pln"> </span><span class="pun">{</span><span class="typ">ChangeDetectionStrategy</span><span class="pun">,</span><span class="pln"> </span><span class="typ">Component</span><span class="pun">,</span><span class="pln"> </span><span class="typ">OnInit</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">from</span><span class="pln"> </span><span class="str">'@angular/core'</span><span class="pun">;</span><span class="pln">
</span><span class="kwd">import</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span><span class="typ">RouterExtensions</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">from</span><span class="pln"> </span><span class="str">'nativescript-angular/router'</span><span class="pun">;</span><span class="pln">
</span><span class="kwd">import</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="kwd">as</span><span class="pln"> </span><span class="typ">LabelModule</span><span class="pln"> </span><span class="kwd">from</span><span class="pln"> </span><span class="str">"tns-core-modules/ui/label"</span><span class="pun">;</span><span class="pln">
</span><span class="kwd">var</span><span class="pln"> </span><span class="typ">SQLite</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">require</span><span class="pun">(</span><span class="str">'nativescript-sqlite'</span><span class="pun">);</span><span class="pln">


</span><span class="lit">@Component</span><span class="pun">({</span><span class="pln">
    moduleId</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">module</span><span class="pun">.</span><span class="pln">id</span><span class="pun">,</span><span class="pln">
    selector</span><span class="pun">:</span><span class="pln"> </span><span class="str">'ns-home'</span><span class="pun">,</span><span class="pln">
    templateUrl</span><span class="pun">:</span><span class="pln"> </span><span class="str">'home.component.html'</span><span class="pun">,</span><span class="pln">
    styleUrls</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[</span><span class="str">'home.component.css'</span><span class="pun">],</span><span class="pln">
    changeDetection</span><span class="pun">:</span><span class="pln"> </span><span class="typ">ChangeDetectionStrategy</span><span class="pun">.</span><span class="typ">OnPush</span><span class="pln">
</span><span class="pun">})</span><span class="pln">


</span><span class="kwd">export</span><span class="pln"> </span><span class="kwd">class</span><span class="pln"> </span><span class="typ">HomeComponent</span><span class="pln"> </span><span class="kwd">implements</span><span class="pln"> </span><span class="typ">OnInit</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
    </span><span class="kwd">public</span><span class="pln"> myItems</span><span class="pun">:</span><span class="pln"> </span><span class="typ">Array</span><span class="str">&lt;any&gt;</span><span class="pun">;</span><span class="pln">
    </span><span class="kwd">public</span><span class="pln"> database</span><span class="pun">:</span><span class="pln"> any</span><span class="pun">;</span><span class="pln">
    </span><span class="kwd">public</span><span class="pln"> input</span><span class="pun">:</span><span class="pln"> any</span><span class="pun">;</span><span class="pln">

    </span><span class="kwd">public</span><span class="pln"> </span><span class="kwd">constructor</span><span class="pun">(</span><span class="kwd">private</span><span class="pln"> router</span><span class="pun">:</span><span class="pln"> </span><span class="typ">RouterExtensions</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">myItems </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span><span class="pln">
        </span><span class="pun">(</span><span class="kwd">new</span><span class="pln"> </span><span class="typ">SQLite</span><span class="pun">(</span><span class="str">'MeasureIt.db'</span><span class="pun">)).</span><span class="kwd">then</span><span class="pun">(</span><span class="pln">db </span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
            db</span><span class="pun">.</span><span class="pln">execSQL</span><span class="pun">(</span><span class="str">'CREATE TABLE IF NOT EXISTS measures (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, unit TEXT, today INTEGER, total INTEGER)'</span><span class="pun">).</span><span class="kwd">then</span><span class="pun">(</span><span class="pln">id</span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
                </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">database </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">;</span><span class="pln">
                </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">fetch</span><span class="pun">();</span><span class="pln">
            </span><span class="pun">},</span><span class="pln"> error </span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
                console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'Create table error'</span><span class="pun">,</span><span class="pln"> error</span><span class="pun">);</span><span class="pln">
            </span><span class="pun">});</span><span class="pln">
        </span><span class="pun">},</span><span class="pln"> error </span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
            console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'Open db error: '</span><span class="pun">,</span><span class="pln"> error</span><span class="pun">);</span><span class="pln">
        </span><span class="pun">});</span><span class="pln">
    </span><span class="pun">}</span><span class="pln">

    </span><span class="kwd">public</span><span class="pln"> ngOnInit</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">myItems</span><span class="pun">.</span><span class="pln">length </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
            </span><span class="kwd">const</span><span class="pln"> label </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">LabelModule</span><span class="pun">.</span><span class="typ">Label</span><span class="pun">();</span><span class="pln">
            </span><span class="kwd">const</span><span class="pln"> expectedValue </span><span class="pun">=</span><span class="pln"> </span><span class="str">"No Measures Found!"</span><span class="pun">;</span><span class="pln">
            label</span><span class="pun">.</span><span class="pln">text </span><span class="pun">=</span><span class="pln"> expectedValue</span><span class="pun">;</span><span class="pln">
        </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
            console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Measures found!"</span><span class="pun">);</span><span class="pln">
        </span><span class="pun">}</span><span class="pln">
    </span><span class="pun">}</span><span class="pln">

    </span><span class="kwd">public</span><span class="pln"> onItemTap</span><span class="pun">(</span><span class="pln">args</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Item Tapped: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> args</span><span class="pun">.</span><span class="pln">index</span><span class="pun">);</span><span class="pln">
    </span><span class="pun">}</span><span class="pln">

    </span><span class="kwd">public</span><span class="pln"> onPlusTap</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">router</span><span class="pun">.</span><span class="pln">navigate</span><span class="pun">([</span><span class="str">'/createMeasure'</span><span class="pun">]);</span><span class="pln">
    </span><span class="pun">}</span><span class="pln">
    </span><span class="kwd">public</span><span class="pln"> addMesurement</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">router</span><span class="pun">.</span><span class="pln">navigate</span><span class="pun">([</span><span class="str">'/newMeasure'</span><span class="pun">]);</span><span class="pln">
    </span><span class="pun">}</span><span class="pln">

    </span><span class="kwd">public</span><span class="pln"> fetch</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">database</span><span class="pun">.</span><span class="pln">all</span><span class="pun">(</span><span class="str">'SELECT * FROM measures'</span><span class="pun">).</span><span class="kwd">then</span><span class="pun">(</span><span class="pln">rows </span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
            </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">myItems </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span><span class="pln">
            </span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">let</span><span class="pln"> row </span><span class="kwd">in</span><span class="pln"> rows</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
                </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">myItems</span><span class="pun">.</span><span class="pln">push</span><span class="pun">({</span><span class="pln">
                    </span><span class="str">'id'</span><span class="pun">:</span><span class="pln"> rows</span><span class="pun">[</span><span class="pln">row</span><span class="pun">][</span><span class="lit">0</span><span class="pun">],</span><span class="pln">
                    </span><span class="str">'name'</span><span class="pun">:</span><span class="pln"> rows</span><span class="pun">[</span><span class="pln">row</span><span class="pun">][</span><span class="lit">1</span><span class="pun">],</span><span class="pln">
                    </span><span class="str">'unit'</span><span class="pun">:</span><span class="pln"> rows</span><span class="pun">[</span><span class="pln">row</span><span class="pun">][</span><span class="lit">2</span><span class="pun">],</span><span class="pln">
                    </span><span class="str">'today'</span><span class="pun">:</span><span class="pln"> rows</span><span class="pun">[</span><span class="pln">row</span><span class="pun">][</span><span class="lit">3</span><span class="pun">],</span><span class="pln">
                    </span><span class="str">'total'</span><span class="pun">:</span><span class="pln"> rows</span><span class="pun">[</span><span class="pln">row</span><span class="pun">][</span><span class="lit">4</span><span class="pun">]</span><span class="pln">
                </span><span class="pun">});</span><span class="pln">
            </span><span class="pun">}</span><span class="pln">
        </span><span class="pun">});</span><span class="pln">
    </span><span class="pun">}</span><span class="pln">
</span><span class="pun">}</span></code></pre>

<p>And here's the simple home.component.html:</p>

<pre class="default prettyprint prettyprinted" style=""><code><span class="tag">&lt;ActionBar&gt;</span><span class="pln">
    </span><span class="tag">&lt;ActionItem</span><span class="pln"> *</span><span class="atn">ngIf</span><span class="pun">=</span><span class="atv">"authentication"</span><span class="pln"> </span><span class="atn">text</span><span class="pun">=</span><span class="atv">"Logout"</span><span class="pln"> </span><span class="atn">ios</span><span class="pln">.</span><span class="atn">position</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> (</span><span class="atn">tap</span><span class="pln">)</span><span class="pun">=</span><span class="atv">"logout()"</span><span class="tag">&gt;&lt;/ActionItem&gt;</span><span class="pln">
    </span><span class="tag">&lt;ActionItem</span><span class="pln"> </span><span class="atn">text</span><span class="pun">=</span><span class="atv">"Create Measure"</span><span class="pln"> </span><span class="atn">ios</span><span class="pln">.</span><span class="atn">position</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> (</span><span class="atn">tap</span><span class="pln">)</span><span class="pun">=</span><span class="atv">"onPlusTap()"</span><span class="tag">&gt;&lt;/ActionItem&gt;</span><span class="pln">
</span><span class="tag">&lt;/ActionBar&gt;</span><span class="pln">
</span><span class="tag">&lt;ListView</span><span class="pln"> [</span><span class="atn">items</span><span class="pln">]</span><span class="pun">=</span><span class="atv">"myItems"</span><span class="pln"> (</span><span class="atn">itemTap</span><span class="pln">)</span><span class="pun">=</span><span class="atv">"onItemTap($event)"</span><span class="tag">&gt;</span><span class="pln">
    </span><span class="tag">&lt;ng-template</span><span class="pln"> </span><span class="atn">let-item</span><span class="pun">=</span><span class="atv">"item"</span><span class="pln"> </span><span class="atn">let-i</span><span class="pun">=</span><span class="atv">"index"</span><span class="pln"> </span><span class="atn">let-odd</span><span class="pun">=</span><span class="atv">"odd"</span><span class="pln"> </span><span class="atn">let-even</span><span class="pun">=</span><span class="atv">"even"</span><span class="tag">&gt;</span><span class="pln">
        </span><span class="tag">&lt;StackLayout</span><span class="pln"> [</span><span class="atn">class</span><span class="pln">.</span><span class="atn">odd</span><span class="pln">]</span><span class="pun">=</span><span class="atv">"odd"</span><span class="pln"> [</span><span class="atn">class</span><span class="pln">.</span><span class="atn">even</span><span class="pln">]</span><span class="pun">=</span><span class="atv">"even"</span><span class="pln"> </span><span class="atn">orientation</span><span class="pun">=</span><span class="atv">"horizontal"</span><span class="tag">&gt;</span><span class="pln">
            </span><span class="tag">&lt;Label</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="kwd">vertical-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="pln"> </span><span class="kwd">text-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="atv">"</span><span class="pln"> [</span><span class="atn">text</span><span class="pln">]</span><span class="pun">=</span><span class="atv">'"ID: " + item.id'</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"10%"</span><span class="tag">&gt;&lt;/Label&gt;</span><span class="pln">
            </span><span class="tag">&lt;Label</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="kwd">vertical-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="pln"> </span><span class="kwd">text-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="atv">"</span><span class="pln"> [</span><span class="atn">text</span><span class="pln">]</span><span class="pun">=</span><span class="atv">'item.name'</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"20%"</span><span class="tag">&gt;&lt;/Label&gt;</span><span class="pln">
            </span><span class="tag">&lt;Label</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="kwd">vertical-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="pln"> </span><span class="kwd">text-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="atv">"</span><span class="pln"> [</span><span class="atn">text</span><span class="pln">]</span><span class="pun">=</span><span class="atv">'"Today: " + item.today + item.unit'</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"28.5%"</span><span class="tag">&gt;&lt;/Label&gt;</span><span class="pln">
            </span><span class="tag">&lt;Label</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="kwd">vertical-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="pln"> </span><span class="kwd">text-align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span><span class="atv">"</span><span class="pln"> [</span><span class="atn">text</span><span class="pln">]</span><span class="pun">=</span><span class="atv">'"Total: " + item.total + item.unit'</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"28.5%"</span><span class="tag">&gt;&lt;/Label&gt;</span><span class="pln">
            </span><span class="tag">&lt;Button</span><span class="pln"> </span><span class="atn">text</span><span class="pun">=</span><span class="atv">"+"</span><span class="pln"> (</span><span class="atn">tap</span><span class="pln">)</span><span class="pun">=</span><span class="atv">"addMesurement($event)"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"13%"</span><span class="pln"> </span><span class="tag">&gt;&lt;/Button&gt;</span><span class="pln">
        </span><span class="tag">&lt;/StackLayout&gt;</span><span class="pln">
    </span><span class="tag">&lt;/ng-template&gt;</span><span class="pln">
</span><span class="tag">&lt;/ListView&gt;</span></code></pre>
    </div>'''
        text = clean_html_text_with_replacement(text_html)
        print text

        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        description_list = tokenizer.tokenize(text)
        print description_list

        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r

    def test_remove_all_tags_4(self):
        text_html = '''<div class="block">Returns an <code>Image</code> object that can then be painted on
  the screen. The <code>url</code> argument that is
  passed as an argument must specify an absolute URL.
  <p>
  This method always returns immediately, whether or not the image
  exists. When the applet attempts to draw the image on the screen,
  the data will be loaded. The graphics primitives that draw the
  image will incrementally paint on the screen.</p></div>'''
        text = clean_html_text(text_html)
        description_list = sentence_split(text)
        print description_list
        print text

        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r

    def test_remove_all_tags_5(self):
        text_html = '''<div class="post-text" itemprop="text">

<p>I have search page that searches for Job Openings.</p>

<p>it has this filters in it:</p>

<ol>
<li>Location (country)</li>
<li>Gender</li>
<li>Job Type</li>
<li>Sector Category</li>
<li>Nationality</li>
</ol>

<p>What is the most efficient way to tally how many on the search results fall into these filters?</p>

<p>say for example I search Job Openings for "web developer" that gives me 150 search results.</p>

<p>How can I tally how many in that 150 are located in the US, or Philippines, how many are Male exclusive jobs or open to any, or how many are for Americans, Germans, Filipinos?</p>
    </div>'''
        text = clean_html_text_with_replacement(text_html)
        print text

        description_list = sentence_split(text)
        print description_list
        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r

    def test_remove_all_tags_6(self):
        text_html = '''<li class="blockList">
<h4>removeLayoutComponent</h4>
<pre>void&nbsp;removeLayoutComponent(<a href="../../java/awt/Component.html" title="class in java.awt">Component</a>&nbsp;comp)</pre>
<div class="block">Removes the specified component from the layout.</div>
<dl>
<dt><span class="paramLabel">Parameters:</span></dt>
<dd><code>comp</code> - the component to be removed</dd>
</dl>
</li>'''
        text = clean_html_text_with_replacement(text_html)
        print text

        text = clean_html_text(text_html)
        print text

        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r

    def test_remove_all_tags_7(self):
        text_html = '''<body>
    <script type="text/javascript"><!--
        if (location.href.indexOf('is-external=true') == -1) {
            parent.document.title="javax.print.event (Java Platform SE 7 )";
        }
    //-->
    </script>
    <noscript>
    <div>JavaScript is disabled on your browser.</div>
    </noscript>
    <!-- ========= START OF TOP NAVBAR ======= -->
    <div class="topNav"><a name="navbar_top">
    <!--   -->
    </a><a href="#skip-navbar_top" title="Skip navigation links"></a><a name="navbar_top_firstrow">
    <!--   -->
    </a>
    <ul class="navList" title="Navigation">
    <li><a href="../../../overview-summary.html">Overview</a></li>
    <li class="navBarCell1Rev">Package</li>
    <li>Class</li>
    <li><a href="package-use.html">Use</a></li>
    <li><a href="package-tree.html">Tree</a></li>
    <li><a href="../../../deprecated-list.html">Deprecated</a></li>
    <li><a href="../../../index-files/index-1.html">Index</a></li>
    <li><a href="../../../help-doc.html">Help</a></li>
    </ul>
    <div class="aboutLanguage"><em><strong>Java™ Platform<br>Standard Ed. 7</strong></em></div>
    </div>
    <div class="subNav">
    <ul class="navList">
    <li><a href="../../../javax/print/attribute/standard/package-summary.html">Prev Package</a></li>
    <li><a href="../../../javax/rmi/package-summary.html">Next Package</a></li>
    </ul>
    <ul class="navList">
    <li><a href="../../../index.html?javax/print/event/package-summary.html" target="_top">Frames</a></li>
    <li><a href="package-summary.html" target="_top">No Frames</a></li>
    </ul>
    <ul class="navList" id="allclasses_navbar_top">
    <li><a href="../../../allclasses-noframe.html">All Classes</a></li>
    </ul>
    <div>
    <script type="text/javascript"><!--
      allClassesLink = document.getElementById("allclasses_navbar_top");
      if(window==top) {
        allClassesLink.style.display = "block";
      }
      else {
        allClassesLink.style.display = "none";
      }
      //-->
    </script>
    </div>
    <a name="skip-navbar_top">
    <!--   -->
    </a></div>
    <!-- ========= END OF TOP NAVBAR ========= -->
    <div class="header">
    <h1 title="Package" class="title">Package javax.print.event</h1>
    <div class="docSummary">
    <div class="block">Package javax.print.event contains event classes  and listener interfaces.</div>
    </div>
    <p>See: <a href="#package_description">Description</a></p>
    </div>
    <div class="contentContainer">
    <ul class="blockList">
    <li class="blockList">
    <table class="packageSummary" border="0" cellpadding="3" cellspacing="0" summary="Interface Summary table, listing interfaces, and an explanation">
    <caption><span>Interface Summary</span><span class="tabEnd"> </span></caption>
    <tr>
    <th class="colFirst" scope="col">Interface</th>
    <th class="colLast" scope="col">Description</th>
    </tr>
    <tbody>
    <tr class="altColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintJobAttributeListener.html" title="interface in javax.print.event">PrintJobAttributeListener</a></td>
    <td class="colLast">
    <div class="block">Implementations of this interface are attached to a
     <a href="../../../javax/print/DocPrintJob.html" title="interface in javax.print"><code>DocPrintJob</code></a> to monitor
     the status of attribute changes associated with the print job.</div>
    </td>
    </tr>
    <tr class="rowColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintJobListener.html" title="interface in javax.print.event">PrintJobListener</a></td>
    <td class="colLast">
    <div class="block">Implementations of this listener interface should be attached to a
     <a href="../../../javax/print/DocPrintJob.html" title="interface in javax.print"><code>DocPrintJob</code></a> to monitor the status of
     the printer job.</div>
    </td>
    </tr>
    <tr class="altColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintServiceAttributeListener.html" title="interface in javax.print.event">PrintServiceAttributeListener</a></td>
    <td class="colLast">
    <div class="block">Implementations of this listener interface are attached to a
     <a href="../../../javax/print/PrintService.html" title="interface in javax.print"><code>PrintService</code></a> to monitor
     the status of the print service.</div>
    </td>
    </tr>
    </tbody>
    </table>
    </li>
    <li class="blockList">
    <table class="packageSummary" border="0" cellpadding="3" cellspacing="0" summary="Class Summary table, listing classes, and an explanation">
    <caption><span>Class Summary</span><span class="tabEnd"> </span></caption>
    <tr>
    <th class="colFirst" scope="col">Class</th>
    <th class="colLast" scope="col">Description</th>
    </tr>
    <tbody>
    <tr class="altColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintEvent.html" title="class in javax.print.event">PrintEvent</a></td>
    <td class="colLast">
    <div class="block">Class PrintEvent is the super class of all Print Service API events.</div>
    </td>
    </tr>
    <tr class="rowColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintJobAdapter.html" title="class in javax.print.event">PrintJobAdapter</a></td>
    <td class="colLast">
    <div class="block">An abstract adapter class for receiving print job events.</div>
    </td>
    </tr>
    <tr class="altColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintJobAttributeEvent.html" title="class in javax.print.event">PrintJobAttributeEvent</a></td>
    <td class="colLast">
    <div class="block">Class PrintJobAttributeEvent encapsulates an event a PrintService
     reports to let the client know that one or more printing attributes for a
     PrintJob have changed.</div>
    </td>
    </tr>
    <tr class="rowColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintJobEvent.html" title="class in javax.print.event">PrintJobEvent</a></td>
    <td class="colLast">
    <div class="block">Class <code>PrintJobEvent</code> encapsulates common events a print job
     reports to let a listener know of progress in the processing of the
     <a href="../../../javax/print/DocPrintJob.html" title="interface in javax.print"><code>DocPrintJob</code></a>.</div>
    </td>
    </tr>
    <tr class="altColor">
    <td class="colFirst"><a href="../../../javax/print/event/PrintServiceAttributeEvent.html" title="class in javax.print.event">PrintServiceAttributeEvent</a></td>
    <td class="colLast">
    <div class="block">Class PrintServiceAttributeEvent encapsulates an event a
     Print Service instance reports to let the client know of
     changes in the print service state.</div>
    </td>
    </tr>
    </tbody>
    </table>
    </li>
    </ul>
    <a name="package_description">
    <!--   -->
    </a>
    <h2 title="Package javax.print.event Description">Package javax.print.event Description</h2>
    <div class="block">Package javax.print.event contains event classes  and listener interfaces.
    <p>
    They may be used to monitor both print services (such as printers going
    on-line &amp; off-line), and the progress of a specific print job.
    </p><p>
    Please note: In the javax.print APIs, a null reference parameter to methods 
    is incorrect unless explicitly documented on the method as having a meaningful
    interpretation. Usage to the contrary is incorrect coding and may result
    in a run time exception either immediately or at some later time.
    IllegalArgumentException and NullPointerException are examples of
    typical and acceptable run time exceptions for such cases.
    </p><p></p></div>
    <dl><dt><span class="strong">Since:</span></dt>
      <dd>1.4</dd></dl>
    </div>
    <!-- ======= START OF BOTTOM NAVBAR ====== -->
    <div class="bottomNav"><a name="navbar_bottom">
    <!--   -->
    </a><a href="#skip-navbar_bottom" title="Skip navigation links"></a><a name="navbar_bottom_firstrow">
    <!--   -->
    </a>
    <ul class="navList" title="Navigation">
    <li><a href="../../../overview-summary.html">Overview</a></li>
    <li class="navBarCell1Rev">Package</li>
    <li>Class</li>
    <li><a href="package-use.html">Use</a></li>
    <li><a href="package-tree.html">Tree</a></li>
    <li><a href="../../../deprecated-list.html">Deprecated</a></li>
    <li><a href="../../../index-files/index-1.html">Index</a></li>
    <li><a href="../../../help-doc.html">Help</a></li>
    </ul>
    <div class="aboutLanguage"><em><strong>Java™ Platform<br>Standard Ed. 7</strong></em></div>
    </div>
    <div class="subNav">
    <ul class="navList">
    <li><a href="../../../javax/print/attribute/standard/package-summary.html">Prev Package</a></li>
    <li><a href="../../../javax/rmi/package-summary.html">Next Package</a></li>
    </ul>
    <ul class="navList">
    <li><a href="../../../index.html?javax/print/event/package-summary.html" target="_top">Frames</a></li>
    <li><a href="package-summary.html" target="_top">No Frames</a></li>
    </ul>
    <ul class="navList" id="allclasses_navbar_bottom">
    <li><a href="../../../allclasses-noframe.html">All Classes</a></li>
    </ul>
    <div>
    <script type="text/javascript"><!--
      allClassesLink = document.getElementById("allclasses_navbar_bottom");
      if(window==top) {
        allClassesLink.style.display = "block";
      }
      else {
        allClassesLink.style.display = "none";
      }
      //-->
    </script>
    </div>
    <a name="skip-navbar_bottom">
    <!--   -->
    </a></div>
    <!-- ======== END OF BOTTOM NAVBAR ======= -->
    <p class="legalCopy"><small><font size="-1"> <a href="http://bugreport.sun.com/bugreport/">Submit a bug or feature</a> <br>For further API reference and developer documentation, see <a href="http://docs.oracle.com/javase/7/docs/index.html" target="_blank">Java SE Documentation</a>. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples.<br> <a href="../../../../legal/cpyr.html">Copyright</a> © 1993, 2016, Oracle and/or its affiliates.  All rights reserved. Use is subject to <a href="http://download.oracle.com/otndocs/jcp/java_se-7-mrel-spec/license.html">license terms</a>. Also see the <a target="_blank" href="http://www.oracle.com/technetwork/java/redist-137594.html">documentation redistribution policy</a>. </font></small></p>
    <!-- Start SiteCatalyst code   -->
    <script type="application/javascript" src="https://www.oracleimg.com/us/assets/metrics/ora_docs.js"></script>
    <!-- End SiteCatalyst code -->
    <noscript>
    <p>Scripting on this page tracks web page traffic, but does not change the content in any way.</p>
    </noscript>
    </body>'''
        text = clean_html_text_with_replacement(text_html)
        print text

        text = clean_html_text(text_html)
        print text

        relation_set = extract_relation_from_html(text_html, "https://docs.oracle.com/javase/8/docs/api")
        for r in relation_set:
            print r
