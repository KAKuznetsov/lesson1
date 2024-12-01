phones = ['раз телефон', 'два теелфон', 'три телефон']

print(phones[-3:])

phones.append('раз телефон')
print(phones)

print(phones.count('раз телефон'))

print(phones.index('два теелфон'))
print('два теелфон' in phones)
del phones[1]
print(phones)
