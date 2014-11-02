# https://codility.com/demo/take-sample-test/min_avg_two_slice


def solution(A):
    prefix_sum = [A[0]]

    for i in range(1, len(A)):
        prefix_sum.insert(i, A[i] + prefix_sum[i - 1])

    lowest_index = 0
    lowest_avg = (A[0] + A[1]) / 2.0

    for num_range in [2, 3]:
        for i in range(0, len(prefix_sum) - num_range + 1):
            x = prefix_sum[i - 1] if i - 1 >= 0 else 0
            y = prefix_sum[i + num_range - 1]
            avg = (y - x) / float(num_range)
            if lowest_avg > avg:
                lowest_avg = avg
                lowest_index = i

    return lowest_index