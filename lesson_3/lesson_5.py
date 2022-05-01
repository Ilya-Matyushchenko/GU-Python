from random import randrange, choice


def get_jokes(n, repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes_list = []
    min_list = min(no, adv, adj)
    while n and len(min_list):
        number = randrange(len(min_list))
        if repeat:
            jokes_list.append(f'{no.pop(number)} {adv.pop(number)} {adj.pop(number)}')
        else:
            jokes_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return jokes_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(10, True))
print(get_jokes(10, False))


