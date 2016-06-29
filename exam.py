import re
wiki = open('wiki.txt', 'r', encoding='utf8')
text = wiki.read()
wiki.close()
imena = re.findall(r'[А-Я]. [А-Я][а-я]+', text)
for result in imena:
    print(result)
    
