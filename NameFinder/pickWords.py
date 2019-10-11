"""
Read text file and must follow the /n 
Description
"""

import os,random,math,re

# Reading the words from file
# file = open('/home/rahul/words.txt')
# WORDS = file.read().split('\n')
# count = 0
# for line in WORDS:
#     count += 1
WORDS = ['rahul', 'hariom', 'raj']

def pickWords(minCount, maxCount):
    pickedWords = []
    picked = ''
    count = minCount + round(random.random() * (maxCount - minCount))
    for i in range(0, count):

        while not re.search('/^[a-zA-Z]+$/', picked):
            picked = WORDS[math.floor(random.random() * count)]
            print(picked)
        pickedWords.append(picked)
    print(pickedWords)
        

if __name__ == "__main__":
    pickWords(1,2)