consonants = set("бвгдґжзйклмнпрстфхцчшБВГҐДЖЗЙКЛМНПРСТФХЦЧШ")

def count_vowels_consonants(word):
    consonants_count = 0
    vowels_count = 0
    for letter in word:
        if letter in consonants:
            consonants_count += 1
        else:
            vowels_count += 1
    return vowels_count, consonants_count

def make_lower(words):
    new_words = []
    for word in words:
        vowels, consonants = count_vowels_consonants(word)
        if consonants > vowels:
            new_words.append(word.lower())
        else:
            new_words.append(word)
    return new_words

words = ("СЬОГОДНІ ВУЛИЦЕЮ ЙШОВ КІТ МАМА СКАЗАЛА ЩОБ Я ЙОГО ЗУСТРІВ").split()

new_words = make_lower(words)
print("Перетворення:", " ".join(new_words))
