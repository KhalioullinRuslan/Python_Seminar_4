# Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
# 15 минут

word = input("Введите слово: ")
array = []
for i in word:
    array += i.split(' ')
score = 0
many_letters = set(word)
for i in many_letters:                    
    for j in range(0,len(array)):
        if i == array[j]:
            score += 1
            if score >=2:
                array[j] = array[j] +'_'+ str(score - 1)  
    score = 0
print(" ".join(array))