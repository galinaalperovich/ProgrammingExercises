import fileinput
# http://codeforces.com/contest/894/problem/C
import functools
import sys

GCD_CACHE = {}


def gcd(a, b):
    if (a, b) in GCD_CACHE:
        return GCD_CACHE.get((a, b))

    result = abs(a) if b == 0 else gcd(b, a % b)
    if a <= b:
        GCD_CACHE[(a, b)] = result
    else:
        GCD_CACHE[(b, a)] = result
    return result


def gcd_arr(arr):
    if len(arr) == 1:
        return arr
    else:
        result = functools.reduce(gcd, arr)
        if type(result) == int:
            return [result]
        else:
            return result


def lcm(a, b):
    return a * b // gcd(a, b)


def get_gcds(arr):
    result = []
    for i, num_i in enumerate(arr):
        for j, num_j in enumerate(arr):
            if i <= j:
                sub_arr = arr[i:j + 1]
                result.append(gcd_arr(sub_arr))

    return set(result)


class InputData:
    def __init__(self, m, gcd_arr):
        self.m = m
        self.s_arr = gcd_arr


class Result:
    def __init__(self, n=None, seq=None):
        self.n = n
        self.seq = seq

    def __str__(self):
        if self.n is None and self.seq is None:
            return '-1'
        else:
            seq_str = ' '.join([str(num) for num in self.seq])
            return '{}\n{}'.format(self.n, seq_str)


def solve(input_data: InputData) -> Result:
    s_arr = input_data.s_arr
    min_el = s_arr[0]
    gcds = gcd_arr(s_arr)
    if min_el not in gcds:
        return Result()
    else:
        res_arr = [min_el]
        l = len(s_arr)
        for i, el in enumerate(s_arr):
            if i != 0:
                res_arr.append(el)
                if i != l-1:
                    res_arr.append(min_el)

        return Result(len(res_arr), res_arr)


def main():
    input = fileinput.input(sys.argv[1:])
    m = int(input.readline().replace('\n', ''))
    gcd_arr = [int(num) for num in input.readline().replace('\n', '').split(' ')]
    input_data = InputData(m, gcd_arr)
    result = solve(input_data)
    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
