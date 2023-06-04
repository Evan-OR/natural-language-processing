import spacy

nlp = spacy.load('en_core_web_sm')
file = open('data/Chapter 0.txt', 'r', encoding='utf-8')
chapter = nlp(file.read().replace('\n\n', ' ').replace('\n', ' '))
file.close()

sents = list(chapter.sents)

singleSentence = sents[2]
ents = list(chapter.ents)

people = []
for ent in ents:
    if ent.label_ == 'PERSON':
        people.append(ent)

print(people)
