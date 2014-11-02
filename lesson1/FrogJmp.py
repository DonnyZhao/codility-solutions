# https://codility.com/demo/take-sample-test/frog_jmp

from math import ceil


def solution(X, Y, D):
    return int(ceil((Y - X) / float(D)))