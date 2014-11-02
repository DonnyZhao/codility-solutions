# https://codility.com/demo/take-sample-test/perm_missing_elem


def solution(A):
    return ((len(A) + 1) * (len(A) + 2) / 2) - sum(A)