def limitWord(sen, a):
    words = sen.split()
    if len(words) <= a:
        return True
    else:
        print("ваше речення не має бути довшим за 10 слів")

sen = input("Введіть речення:")
a = 10
words = sen.split()
temp = words[0]
words[0] = words[-1]
words[-1] = temp
if sen.strip() == " ":
    print("Речення містить прогалини на початку або в кінці!")
if "-" in sen:
    print("Речення містить заборонений символ '-'!")
if limitWord(sen, a) :
    newSen = ' '.join(words)
    print("Результат:", newSen)        

