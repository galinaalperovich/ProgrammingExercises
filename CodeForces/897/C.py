import fileinput
import sys


# http://codeforces.com/contest/897/problem/C

class InputData:
    def __init__(self, questions):
        self.questions = questions


class Result:
    def __init__(self, s):
        self.n = s

    def __str__(self):
        return f'{self.n}'


X = 'What are you doing while sending "'
A = 'What are you doing at the end of the world? Are you busy? Will you save us?'
Y = '"? Are you busy? Will you send "'
Z = '"?'

l_x = len(X)
l_a = len(A)
l_y = len(Y)
l_z = len(Z)

d_letter = {'X': X, 'A': A, 'Y': Y, 'Z': Z}
d_len = {'X': l_x, 'A': l_a, 'Y': l_y, 'Z': l_z}

length_storage = [l_a]


def get_question_by_prev(prev):
    return X + prev + Y + prev + Z


def get_length_storage():
    global length_storage
    i = 1
    next_value = 0
    while next_value <= 10 ** 18:
        prev_value = length_storage[i - 1]
        next_value = l_x + prev_value + l_y + prev_value + l_z
        length_storage.append(next_value)
        i += 1
    return length_storage


def char_at(n, k):
    global length_storage
    if n == 0:
        return A[k]
    if n > len(length_storage):
        return char_at(n - 1, k - l_a)

    f_n_prev = length_storage[n - 1]
    a1 = l_x
    a2 = a1 + f_n_prev
    a3 = a2 + l_y
    a4 = a3 + f_n_prev

    try:
        if k <= a1:
            return X[k]
        elif a1 + 1 <= k < a2:
            return char_at(n - 1, k - a1)
        elif a2 + 1 <= k < a3:
            return Y[k - a2]
        elif a3 + 1 <= k < a4:
            return char_at(n - 1, k - a3)
        elif k >= a4 + 1:
            return Z[k - a4]
    except:
        return '.'


def solve(input_data: InputData) -> Result:
    global length_storage
    length_storage = get_length_storage()
    questions = input_data.questions
    result = ''
    for n, k in questions:
        result += char_at(n, k - 1)
    return Result(result)


def get_int_arr(line):
    l = [int(num) for num in line.replace('\n', '').split(' ')]
    if len(l) == 1:
        return l[0]
    else:
        return l


def main():
    input = fileinput.input(sys.argv[1:])

    q = get_int_arr(input.readline())
    questions = []
    for i in range(q):
        n, k = get_int_arr(input.readline())
        questions.append((n, k))

    input_data = InputData(questions)
    result = solve(input_data)

    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
