# https://codility.com/demo/take-sample-test/perm_check


def solution(A):
    A.sort()

    for i in range(1, len(A) + 1):
        if i != A[i - 1]:
            return 0
    return 1