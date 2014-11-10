# https://codility.com/demo/take-sample-test/count_factors


def solution(N):
    factors = 0

    i = 1
    while i * i < N:
        if N % i == 0:
            factors += 2
        i += 1

    if i * i == N:
        factors += 1

    return factors