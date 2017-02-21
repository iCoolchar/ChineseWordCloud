# !/usr/bin/python2.7
# coding: UTF-8
from os import path
from collections import Counter
from scipy.misc import imread
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname('.')

STOPWORDS = [u'的',u'地',u'得',u'而',u'了',u'在',u'是',u'我',u'有',u'和',u'就',u'不',u'人',u'都',u'一',u'一个',u'上',u'也',u'很',u'到',u'说',u'要',u'去',u'你',u'会',u'着',u'没有',u'看',u'好',u'自己',u'这']
PUNCTUATIONS = set(u''' :!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻︽︿﹁﹃﹙﹛﹝（｛“‘-—_…\n''')

fp_text = open(path.join(d, 'corpus.txt'))
word_list = list(filter(lambda x: x not in STOPWORDS and x not in PUNCTUATIONS, jieba.cut(fp_text.read())))
fp_text.close()

word_freq = Counter(word_list)
word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

alice_coloring = imread(path.join(d, "background.png"))

wc = WordCloud(background_color="white",
               max_words=200,
               mask=alice_coloring,
               max_font_size=40,
               random_state=42,
               min_font_size=2,
               font_path="/Library/Fonts/华文黑体.ttf")

wc.generate_from_frequencies(word_freq)
image_colors = ImageColorGenerator(alice_coloring)
wc.recolor(color_func=image_colors)
wc.to_file(path.join(d, "word_cloud.png"))
