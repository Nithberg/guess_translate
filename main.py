easy = {'cat': 'кошка', 'dog': 'собака', 'lion': 'лев', 'home': 'дом', 'man': 'мужчина'}
medium = {}
hard = {}

levels = {
    0: 'Нулевой',
    1: 'Так себе',
    2: 'Можно лучше',
    3: 'Нормально',
    4: 'Хорошо',
    5: 'Отлично',
}

answers = {}
words = {}
lap = 1
user_level = 0

choose_level = input('Введине уровень сложности (легкий, средний, сложный): ')
print(f'Вы выбрали {choose_level} уровень сложности, мы предложим 5 слов, подберите их перевод')
if choose_level == 'легкий':
    words = easy

for word, translate in words.items():
    print(f'Раунд {lap} - FIGHT!')
    print()
    question = input(f'{word}, {len(translate)} букв, начинается на {translate[0]}...\nВведите ваш ответ: ')
    if question == translate:
        print(f'Вы угадали, {word} это {translate}')
        print()
        answers[word] = True
        user_level += 1
        lap += 1
    else:
        print(f'Вы не угадали, {word} это {translate}')
        print()
        answers[word] = False
        lap += 1

print(f'Вы правильно угадали {user_level} слова')
if user_level in levels:
    print(f'Ваш ранг: {levels[user_level]}')

print('Правильно отвечены слова:')
for answer, correct in answers.items():
    if correct:
        print(answer)

print('Неправильно отвечены слова:')
for answer, correct in answers.items():
    if not correct:
        print(answer)
