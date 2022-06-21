# Accuracy of NER

with open("E://7th sem CSE/internship/CRF_4_NER-master/hi/result.txt", "r",encoding="utf-8") as f:
    sents = [line.strip() for line in f.readlines() if line.strip()]

total = len(sents)
print(total)

count = 0
for sent in sents:
    words = sent.split()
    
    if words[-1] == words[-2]:
        count += 1

print("Accuracy: %.4f" %(count/total))
