# coding: utf-8

import string

text = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

for i in string.punctuation:
    text = text.replace(i, '')

text.lower()
text = text.split()
pythonLetters = []

for i in text:
    if len(i) > 4:
        for j in "python":
            if j in i:
                if i not in pythonLetters:
                    pythonLetters.append(i)

print("Existem {} palavras com as letras de 'python' no texto".format(len(pythonLetters)))
