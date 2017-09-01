import fileinput
import sys
import re

TEST = False

ALPHABET2 = {'i': 1, 'j': 1, 'a': 2, 'b': 2, 'c': 2,
             'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4,
             'k': 5, 'l': 5, 'm': 6, 'n': 6, 'p': 7,
             'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8,
             'w': 9, 'x': 9, 'y': 9, 'o': 0, 'q': 0, 'z': 0}


def word_to_num(word):
    num = ''
    for w in word:
        w_ = ALPHABET2.get(w, None)
        if w_ is None:
            return None
        num += str(w_)

    return num


def run_process(id, vocab_idx, current_tel, solution_arr, all_solutions, L):
    if id == len(current_tel):
        l = len(solution_arr)
        if l < L[0]:
            L[0] = l
        all_solutions.append(solution_arr)
        return

    if id != 0 and L != 0 and len(solution_arr) >= L[0]:
        return
    words = vocab_idx.get(id, None)
    if words is None:
        return

    for word_n, word in words:
        l = len(word_n)
        next_id = id + l
        solution_arr_copy = solution_arr[:]
        solution_arr_copy.append(word)
        # solution_arr.append(word)
        run_process(next_id, vocab_idx, current_tel, solution_arr_copy, all_solutions, L)


def solve(current_tel, current_vocab):
    vocab_num = []
    vocab_idx = {}

    for word in current_vocab:
        vocab_num.append(word_to_num(word))

    vocab_set = set()
    for word_n, word in zip(vocab_num, current_vocab):
        vocab_set.add((word_n, word))


    vocab_num = list(filter(lambda x: x[0] is not None and x[0] and x[0] != '' and x[0] in current_tel, vocab_set))
    vocab_num = sorted(vocab_num, key=lambda x: len(x[0]), reverse=True)
    for word_n, word in vocab_num:
        idx = [m.start() for m in re.finditer('(?={0})'.format(re.escape(word_n)), current_tel)]
        for id in idx:
            words_by_id = vocab_idx.get(id, [])
            words_by_id.append((word_n, word))
            vocab_idx[id] = words_by_id

    all_solutions = []
    run_process(0, vocab_idx, current_tel, [], all_solutions, [50000])
    cleaned_solutions = []
    for sol in all_solutions:
        if len(''.join(sol)) == len(current_tel):
            cleaned_solutions.append(sol)
    if cleaned_solutions:
        return ' '.join(sorted(cleaned_solutions, key=lambda x: len(x))[0])
    else:
        return 'No solution.'


def main():
    data = fileinput.input()
    results_arr = []

    current_tel = None
    current_vocab = []
    after_tel = False
    num_words = 0
    for line in data:
        line = line.replace('\n', '')
        if num_words == 0 and not after_tel:
            if current_tel is not None or line == '-1':
                if current_tel != '':
                    solution = solve(current_tel, current_vocab)
                else:
                    solution = 'No solution.'
                results_arr.append(solution)

            if line:
                current_tel = line
            else:
                current_tel = ''
            current_vocab = []
            after_tel = True

        else:
            if after_tel:
                num_words = int(line)
                after_tel = False
            else:
                current_vocab.append(line)
                num_words -= 1

    if TEST:
        for line, res in zip(open('output1', 'r').readlines(), results_arr):
            line_cl = line.replace('\n', '')
            print(line_cl == res, line, res)
    else:
        result = '\n'.join(results_arr)
        sys.stdout.write(result)


if __name__ == '__main__':
    main()
