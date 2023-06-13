"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число 
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может 
состоять из одного слова, если во фразе несколько слов, то они 
разделяются дефисами. Фразы отделяются друг от друга пробелами.
Написать функцию, которая принимает строку текста и проверяет ее ритм 
(по Винни-Пуху) Если ритм есть, функция возвращает True, иначе 
возвращает False
"""


def find_rhythm(verse: str, return_vowels: bool = True):
    if verse == "":
        return -1
    vowels = ('а','е','ё','и','о','у','ы','э','ю','я')
    phrases = tuple(verse.split())
    has_rhythm = True
    if return_vowels:
        phrase_vowels = list()
        phrase_vowels.append({val: phrases[0].count(val) for val in vowels if phrases[0].count(val) > 0})
    vowels_count = sum(phrases[0].count(val) for val in vowels)
    for phrase in phrases[1:]:
        if sum(phrase.count(val) for val in vowels) != vowels_count:
            has_rhythm = False
        if return_vowels:
            phrase_vowels.append({val: phrase.count(val) for val in vowels if phrase.count(val) > 0})
            
    if return_vowels:
        return (has_rhythm, phrase_vowels)
    return has_rhythm

print(find_rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", False))
print(find_rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
print(find_rhythm("пара-ра-рам рам-пум-пупам па-ре-по-дам"))
print(find_rhythm("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
print(find_rhythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
print(find_rhythm("Пам-парам-пурум Пум-пурум-карам"))