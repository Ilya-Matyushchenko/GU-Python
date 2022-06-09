import re


def email_parse(email_address):
    parse = re.match(r'\w+\@\w+\.\w+', email_address)
    print(parse)
    if parse:
        pars = re.split(r'@', email_address)
        print({'username': pars[0], 'domain': pars[1]})
    else:
        raise ValueError(f'wrong email: {email_address}')


email_parse(input('Введите email:'))
