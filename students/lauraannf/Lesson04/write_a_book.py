# -*- coding: utf-8 -*-
import random
file = open('hound.txt', 'r', encoding='utf8')
# file = open('testbook.txt', 'r')
lines = file.readlines()
del lines[:38]
word_list = []
for line in lines:
    for word in line.split():
        word_list.append(word)
word_dict = {}
for it in range(len(word_list)-2):
    if word_list[it] + ' ' + word_list[it+1] in word_dict:
        word_dict[word_list[it] + ' ' +
                  word_list[it+1]].append(word_list[it+2])
    else:
        word_dict[word_list[it] + ' ' + word_list[it+1]] = [word_list[it+2]]
word_list_new = ['Holmes', 'leaned']
word_key = word_list_new[0] + ' ' + word_list_new[1]
n = 1
while True:
    if word_key not in word_dict:
        break
    word_list_new.append(random.choice(word_dict[word_key]))
    word_key = word_list_new[n] + ' ' + word_list_new[n+1]
    n = n + 1
file.close()

file_new = open('new_hound.txt', 'w')
n_period = 0
for it in range(len(word_list_new)):
    # for it in range(300):
    file_new.write(word_list_new[it] + ' ')
    if word_list_new[it][-1] is '.' and len(word_list_new[it]) > 2 and \
            word_list_new[it] not in ['Mr.', 'Dr.', 'Mrs.']:
        n_period = n_period + 1
    if n_period == 5:
        file_new.write('\n     ')
        n_period = 0
file_new.close()
