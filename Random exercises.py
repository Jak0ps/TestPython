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

#Exercise 8
def censor(text,word):
    tempword = ""
    centext = ""
    for i in text:
        if not i.isspace():
            tempword = tempword + i
        elif tempword == word:
            if not centext == "":
                centext = centext + " "
            for i in range(len(word)):
                centext = centext + "*"
                tempword = ""
        else:
            if centext == "":
                centext = tempword
                tempword = ""
            else:
                centext = centext + " " + tempword
                tempword = ""
    if tempword == word:
        centext = centext + " "
        for i in range(len(word)):
            centext = centext + "*"
    else:
        centext = centext + " " + tempword
    return centext

#Correct code
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)
    return result


#Exercise 9
def count(sequence,item):
    counter=0
    for i in sequence:
        if i == item:
            counter += 1
    return int(counter)

#Exercise 10
def purify(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even

purify([1,2,3])

#Exercise 11
def product(numbers):
    prod = 1
    for i in numbers:
        prod = prod * i
    return int(prod)

print product([4, 5, 5])

#Exercise 12
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    inputlist = sorted(inputlist)
    outputlist = [inputlist[0]]
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
    return outputlist

print remove_duplicates([1, 1, 2, 2])

#Exercise 13
def median(numbers):
    if numbers == []:
        return []
    numbers = sorted(numbers)
    #you can use this as well
    #numbers.sort()
    if len(numbers) % 2 == 1:
        return numbers[int(len(numbers)/2)]
    else:
        return ((numbers[int(len(numbers)/2)-1] + \
                 numbers[int(len(numbers)/2)]) / (2.0))

print median([7, 12, 3, 1, 6])
print median([7, 3, 1, 4])