# https://codility.com/demo/take-sample-test/peaks


def solution(A):
    count = len(A)

    if count < 3:
        return 0

    peaks_from_start = [0]
    for i in xrange(1, count - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks_from_start.append(peaks_from_start[i - 1] + 1)
        else:
            peaks_from_start.append(peaks_from_start[i - 1])
    peaks_from_start.append(peaks_from_start[-1])

    divisors = []
    for i in range(2, count + 1):
        if count % i == 0:
            divisors.append(i)

    for divisor in divisors:
        success = False
        last = 0
        for i in range(divisor - 1, count, divisor):
            if peaks_from_start[i] > last:
                last = peaks_from_start[i]
                success = True
            else:
                success = False
                break

        if success:
            return count / divisor

    return 0
