# https://codility.com/demo/take-sample-test/max_double_slice_sum


def solution(A):
    count = len(A)

    max_from_start = [0] * count
    max_prew = 0
    for i in range(1, count-1):
        max_from_start[i] = max(0, max_prew + A[i])
        max_prew = max_from_start[i]

    max_from_end = [0] * count
    max_prew = 0
    for i in range(count-2, 0, -1):
        max_from_end[i] = max(0, max_prew + A[i])
        max_prew = max_from_end[i]

    max_double_slice = 0
    for i in range(0, count-2):
        max_double_slice = max(max_double_slice, max_from_start[i] + max_from_end[i+2])

    return max_double_slice