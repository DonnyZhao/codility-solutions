# https://codility.com/demo/take-sample-test/min_perimeter_rectangle


def solution(N):
    min_perimeter = 2 * (1 + N)
    i = 1
    while i * i <= N:
        if N % i == 0:
            min_perimeter = min(min_perimeter, 2 * ((N / i) + i))
        i += 1

    return min_perimeter