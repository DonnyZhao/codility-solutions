# https://codility.com/demo/take-sample-test/max_counters


def solution(N, A):
    counters = [0] * N
    min_value = 0
    max_counter = 0

    for i in A:
        if i <= N:
            counters[i - 1] = max(counters[i - 1], min_value)
            counters[i - 1] += 1
            max_counter = max(max_counter, counters[i - 1])
        else:
            min_value = max_counter

    for i in range(N):
        if counters[i] < min_value:
            counters[i] = min_value

    return counters