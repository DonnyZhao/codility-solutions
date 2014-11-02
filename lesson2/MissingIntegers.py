# https://codility.com/demo/take-sample-test/missing_integer


def solution(A):
    filtered_input = filter(lambda i: i > 0 == 0, A)

    if len(filtered_input) == 0:
        return 1

    sorted_input = sorted(filtered_input)

    last_num = sorted_input[0]

    if last_num > 1:
        return 1

    for i in sorted_input:
        if last_num + 1 < i:
            return last_num + 1

        last_num = i

    return last_num + 1