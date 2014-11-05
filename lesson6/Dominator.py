# https://codility.com/demo/take-sample-test/dominator


def solution(A):
    count = 0
    for val in A:
        if count == 0:
            candidate = val
            count += 1
        else:
            if candidate == val:
                count += 1
            else:
                count -= 1

    count_occurrence = 0
    for val in A:
        if val == candidate:
            count_occurrence += 1

    return A.index(candidate) if len(A) // 2 < count_occurrence else -1