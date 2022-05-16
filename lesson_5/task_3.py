import itertools


def mag(a, b):
    for i in itertools.zip_longest(a, b):
        yield i


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
stud = mag(tutors, classes)
num = len(tutors)
if num < len(classes):
    num = len(classes)
counter = 0
while counter < num:
    print(next(stud))
    counter += 1
