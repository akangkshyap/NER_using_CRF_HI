# Testing the NER

with open("E://7th sem CSE/internship/CRF_4_NER-master/hi/valid.txt", "r",encoding="utf-8") as f:
    sents = [line.strip() for line in f.readlines() if line.strip()]

word = []
predict = []

for sent in sents:
    words = sent.split()
    word.append(words[0])
    predict.append(words[-1])


ner_reg_list = []
for word, tag in zip(word, predict):
    if tag != 'O':
        ner_reg_list.append((word, tag))


print("NER：")
if ner_reg_list:
    for i, item in enumerate(ner_reg_list):
        if item[1].startswith('B'):
            end = i+1
            while end <= len(ner_reg_list)-1 and ner_reg_list[end][1].startswith('I'):
                end += 1

            ner_type = item[1].split('-')[1]
            ner_type_dict = {'PER': 'PERSON: ',
                            'LOC': 'LOCATION: ',
                            'ORG': 'ORGANIZATION: ',
                            'MISC': 'MISC: '
                            }
            print(ner_type_dict[ner_type],\
                ' '.join([item[0] for item in ner_reg_list[i:end]]))