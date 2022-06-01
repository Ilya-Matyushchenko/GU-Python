txt = '''скололазанье,охота
горные лыжи
рыбалка,бег
боулинг, выращивание кристаллов'''


with open('data/hobby.csv', 'w', encoding='utf-8') as f:
    f.write(txt)
