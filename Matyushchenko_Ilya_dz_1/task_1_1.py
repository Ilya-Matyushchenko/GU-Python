duration = int(input())

seconds = duration % 60
minutes = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // 86400

if duration < 60:
    print(seconds, 'сек')
elif 60 <= duration < 3600:
    print(minutes, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    print(hour, 'час', minutes, 'мин', seconds, 'сек')
else:
    print(day, 'дн', hour, 'час', minutes, 'мин', seconds, 'сек.')
