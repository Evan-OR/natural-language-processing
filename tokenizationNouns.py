import spacy

nlp = spacy.load('en_core_web_sm')
file = open('data/Chapter 0.txt', 'r', encoding='utf-8')
chapter = nlp(file.read().replace('\n\n', ' ').replace('\n', ' '))
file.close()

sents = list(chapter.sents)

singleSentence = sents[1]


nouns = []
for token in singleSentence:
    if token.pos_ == 'NOUN':
        nouns.append(token.text)

print(nouns)

#NOUNS CHUNKS
chunks = (list(chapter.noun_chunks))

for chunk in chunks:
    if 'key' in chunk.text:
        print(chunk)