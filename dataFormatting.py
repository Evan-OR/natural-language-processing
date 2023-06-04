import spacy

with open ('data/alice.txt', 'r', encoding='utf8') as f:
    text = f.read()
    chapters = text.split('CHAPTER ')[1:]
    
    # for i in range(len(chapters)):
    #     file_path = f'data/Chapter {i}.txt'
    #     new_file = open(file_path, 'w', encoding="utf8")
    #     new_file.write(chapters[i])
    #     new_file.close()

nlp = spacy.load('en_core_web_sm')
doc = nlp(chapters[0])
sents = list(doc.sents)
print(sents[1])

