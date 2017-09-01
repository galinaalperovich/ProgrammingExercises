import fileinput
import sys

# http://codeforces.com/contest/821/problem/A

TEST = False

num_elements = None
arr = None
results_arr = []


def solve():
    global arr, num_elements, results_arr

    yes = False
    not_zero = 0

    for i, el in enumerate(arr):
        if el != 0:
            yes = True
            not_zero = i
            break

    if not yes:
        results_arr.append('NO')
        return
    else:
        pairs = []
        start = 1
        next = not_zero + 1
        end = not_zero + 1
        for i, el in enumerate(arr):
            if i >= next:
                if el == 0:
                    end += 1
                else:
                    pairs.append((start, end))
                    start = i + 1
                    end = i + 1

        pairs.append((start, end))

        results_arr.append('YES')
        results_arr.append(str(len(pairs)))
        results_arr += ['{} {}'.format(x[0], x[1]) for x in pairs]


def main():
    data = fileinput.input()

    data_arr = []

    for i, line in enumerate(data):
        data_arr.append(line.replace('\n', ''))

    global num_elements, arr
    num_elements = int(data_arr[0])
    arr = list(map(lambda x: int(x), data_arr[1].split(' ')))

    solve()

    global results_arr

    if TEST:
        for line, res in zip(open('output', 'r').readlines(), results_arr):
            print(line.split()[0] == res, line, res)
    else:
        result = '\n'.join(results_arr)
        sys.stdout.write(result)


if __name__ == '__main__':
    main()
