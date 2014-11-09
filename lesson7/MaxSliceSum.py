# https://codility.com/demo/take-sample-test/max_slice_sum


def solution(A):
    count = len(A)

    max_slice_sum = A[0]
    temp_sum = A[0]
    for i in range(1, count):
        temp_sum = max(A[i], temp_sum + A[i])
        max_slice_sum = max(temp_sum, max_slice_sum)

    return max_slice_sum