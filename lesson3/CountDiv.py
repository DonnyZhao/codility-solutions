# https://codility.com/demo/take-sample-test/count_div


def solution(A, B, K):
    if A % K == 0:
        return ((B - A) // K) + 1
    else:
        return (B - (A - (A % K))) // K
