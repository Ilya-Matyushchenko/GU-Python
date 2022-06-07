import os

settings = {}
with open('data/config.yaml') as f:
    lines = dict(map(str.split, f.readlines()))

basedir = lines.pop('base')
for key, val in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, key), exist_ok=True)
    print(f'Создан каталог: {key}')
    for i in val.split(','):
        with open(os.path.join(os.curdir, basedir, key, i), 'w') as f:
            print(f'Создан файл: {i} в каталоге {key}')
