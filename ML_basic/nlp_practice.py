from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.corpus import kolaw
from konlpy.corpus import kobill


okt = Okt()

text = '한글 자연어 처리는 재밌다. 열심히 해야겠다 정말 열심히 해야겠다!! ㅎㅎㅎ '

#print(okt.morphs(text))
#print(okt.morphs(text, stem=True))

#print(okt.nouns(text))
#print(okt.phrases(text))
#print(okt.pos(text))
print(okt.pos(text,join=True))
print(okt.pos(text))

#print(kolaw.open('constitution.txt').read()[:])
#print(kobill.open('1809890.txt').read())