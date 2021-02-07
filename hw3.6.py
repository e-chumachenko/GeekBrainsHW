# 1 часть


def int_func(word):
    return word.title()


user_word = input('Введите, пожалуйста, слово из маленьких латинских букв - ')
print(int_func(user_word))

# 2 часть


def int_func(word):
    return word.title()


user_phrase = input('Введите, пожалуйста, фразу, состоящую из латинских слов в нижнем регистре, разделенных пробелом ')
phrase_l = user_phrase.split()
phrase_t = []
for w in phrase_l:
    title = int_func(w)
    phrase_t.append(title)
print(" ".join(phrase_t))
