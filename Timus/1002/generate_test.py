import os

ALPHABET2 = {'i': 1, 'j': 1, 'a': 2, 'b': 2, 'c': 2,
             'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4,
             'k': 5, 'l': 5, 'm': 6, 'n': 6, 'p': 7,
             'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8,
             'w': 9, 'x': 9, 'y': 9, 'o': 0, 'q': 0, 'z': 0, '5': 'aaaa'}


def get_word_num(word):
    word_num = [str(ALPHABET2[w]) for w in word]
    return ''.join(word_num)


def generate(word, vocab):
    test_str = ''
    word_num = get_word_num(word)
    test_str += word_num + '\n'
    if vocab:
        test_str += str(len(vocab)) + '\n'
    else:
        test_str += str(len(vocab))
    if len(vocab) == 0:
        words = ''
    else:
        words = '\n'.join(vocab)
    test_str += words
    return test_str


tels = ['iiij iiii iiii']
# vocab = ['hi', 'him', 'galya', 'is', 'name', 'namei', 'please', 'help', 'me', 'ple', 'pleasehelp', 'p', 'l', 'e', 'a',
#          's', 'e', 'my']
vocab = ['iiijiiii', 'ii']

general_test_str = ''
general_out_str = ''
for i, tel in enumerate(tels):
    general_out_str += tel + '\n'
    test = generate(tel.replace(' ', ''), vocab)
    if i != len(tels) - 1:
        general_test_str += test + '\n'
    else:
        general_test_str += test + '\n-1'

open('input1', 'w').write(general_test_str)
open('output1', 'w').write(general_out_str)

os.system("python 1002.py input1")
