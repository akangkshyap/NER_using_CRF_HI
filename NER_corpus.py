
from inltk.inltk import setup
setup("hi")

#Training data
separators = [u"।", u",", u"."] 
with open("E://7th sem CSE/internship/CRF_4_NER-master/hi/train.txt", "r",encoding="utf-8") as f:
    sents = [line.strip() for line in f.readlines()]


train_num = int((len(sents)//3))
with open("E://7th sem CSE/internship/CRF_4_NER-master/hi/train.data", "w",encoding="utf-8") as g:
    for i in range(train_num):
        separators = [u"।", u",", u"."] 
        words = sents[3*i].split('\t')
        postags = sents[3*i+1].split('\t')
        tags = sents[3*i+2].split('\t')
        for separator,word, postag, tag in zip(separators,words, postags, tags):
            g.write(separator+' '+word+' '+postag+' '+tag+'\n')
        g.write('\n')

#print('OK train!')





#Testing Data

with open("E://7th sem CSE/internship/CRF_4_NER-master/hi/test.txt", "r",encoding="utf-8") as f:
    sents = [line.strip() for line in f.readlines()]


test_num = int((len(sents)//3))
with open("E://7th sem CSE/internship/CRF_4_NER-master/hi/test.data", "w",encoding="utf-8") as g:
    for i in range(test_num):
        words = sents[3*i].split('\t')
        postags = sents[3*i+1].split('\t')
        tags = sents[3*i+2].split('\t')
        for word, postag, tag in zip(words, postags, tags):
            g.write(word+' '+postag+' '+tag+'\n')
        g.write('\n')

print('OK test!')

