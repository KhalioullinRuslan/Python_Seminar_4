# Задача №27. 
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

str = """She sells sea shells on the sea shore The shellsthat she sells are sea shells 
I'm sure.So if she sells sea 
shells on the sea shore I'm sure that the shells are sea
shore shells"""

znaki = ['.', ',',';']

for z in znaki:
    str = str.replace(z, ' ')

print(str)

lst = set(str.lower().split()) 

print(len(lst))