# https://codility.com/demo/take-sample-test/max_profit


def solution(A):
    max_end = 0
    max_daily_profit = 0
    for i in range(1, len(A)):
        daily_profit = A[i] - A[i-1]
        max_end = max(0, max_end + daily_profit)
        max_daily_profit = max(max_daily_profit, max_end)

    return max_daily_profit


