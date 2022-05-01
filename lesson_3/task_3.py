def thesaurus(*args):
    dict_name = {}
    for name in args:
        first_lit = name[0]
        dict_name[first_lit] = dict_name.get(first_lit, []) + [name]
    return dict_name


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
