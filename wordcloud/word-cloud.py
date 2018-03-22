from wordcloud import WordCloud
text = open("C:\\Users\\Shuai\\Desktop\\scrolldepth.txt", 'r').read()
wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
