# https://codility.com/demo/take-sample-test/tape_equilibrium


def solution(A):
    left_part = A[0]
    sum_all = sum(A)
    min_diff = abs(sum_all - (2*left_part))

    for i in range(1, len(A)-1):
        left_part += A[i]
        min_diff = min(min_diff, abs(sum_all - (2*left_part)))

    return min_diff