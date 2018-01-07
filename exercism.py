#
#   Exercism.io coding exercises
#

import string
import datetime

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False


def is_isogram(word):
    dictionary = {}
    for letter in word.lower():
        if letter != " " and letter != "-":
            if letter in dictionary:
                return False
            else:
                dictionary[letter] = ''
    return True


def is_pangram(word):
    dictionary = dict.fromkeys(string.ascii_lowercase, False)
    for letter in word.lower():
        if letter in dictionary:
            dictionary[letter] = True
    for letter in dictionary:
        if not dictionary[letter]:
            return False
    return True


def to_rna(dna):
    dictionary = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_nucleotide = ""
    for dna_nucleotide in dna.upper():
        if dna_nucleotide in dictionary:
            rna_nucleotide += dictionary.get(dna_nucleotide)
        else:
            raise ValueError("Invalid nucleotide: %s" % dna_nucleotide)
    return rna_nucleotide


def hamming(x, y):
    if x == y:
        return 0
    if len(x) == len(y):
        distance = 0
        for i in range(0, len(x)):
            if x[i] != y[i]:
                distance += 1
        return distance
    else:
        raise ValueError("Strands must be of equal length!")


def word_count(sentence):
    word_array = sentence.lower().replace(',', ' ').replace('_', ' ').split()
    dictionary = {}
    for word in word_array:
        try:
            while not word[0].isalnum():
                word = word[1:]
        except IndexError:
            pass

        try:
            while not word[-1].isalnum():
                word = word[0:-1]
        except IndexError:
            pass

        if len(word) != 0:
            if word in dictionary:
                dictionary.update({word: dictionary[word] + 1})
            else:
                dictionary[word] = 1
    return dictionary


def add_gigasecond(start_date):
    temp_date = datetime.timedelta(seconds=1000000000)
    return start_date + temp_date


#try:
#print(word_count("testing 1 2 testing"))
#except ValueError as error:
#    print(error)
#    exit(1)

#word = "fish::"
#while not word[-1].isalpha():
#    word = word[0:-1]
#print(word[1:])
