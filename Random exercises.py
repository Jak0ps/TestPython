#!/usr/bin/python

#Exercise 1
def is_int(x):
    if not x - int(x) == 0:
        return False
    else:
        return True

print is_int(7.0)
print is_int(7.5)
print is_int(-1)

#Exercise 2
def digit_sum(n):
    total = 0
    for i in (str(n)):
        total += int(i)
    return total

digit_sum(1234)

#Another way to do the above

def digit_sum2(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

digit_sum2(1234)

#Exercise 3
def factorial(x):
    sum = 1
    while x > 0:
        sum *= x
        x -= 1
    return sum

print factorial(4)
print factorial(1)
print factorial(3)

#Exercise 4
def is_prime(x):
    if x < 2:
        return False
    for n in range(2,x):
        if float(x) % n == 0.0:
            return False
            break
    return True

for i in range(18):
    print "prime of", i, is_prime(i)

#Exercise 5
def reverse(text):
    rev_text = []
    for i in str(text):
        rev_text.append(i)
    lenoftext = len(rev_text)
    while lenoftext > 0:
        print rev_text[lenoftext-1],
        rev_text.pop(lenoftext-1)
        lenoftext -= 1

#Correct code

def reverse2(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

#Exercise 6
def anti_vowel(text):
    vowels = ['a','e','i','o','u']
    word = ""
    for n in vowels:
        for i in range(len(text)):
            if not n == text[i] and not n.upper() == text[i]:
                word = word + text[i]
        text = word
        word = ""
    return text

print anti_vowel("Hey You!")
print anti_vowel("Yab Gab to Trab Yab Yab Aeiouz")

#Exercise 7
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for i in word:
        total = total + score[i.lower()]
    return total


print scrabble_score("jacob")