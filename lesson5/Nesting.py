# https://codility.com/demo/take-sample-test/nesting


def solution(S):
    open_char = 0
    close_char = 0
    for symbol in S:
        if symbol == '(':
            open_char += 1
        else:
            close_char += 1

        if close_char > open_char:
            return 0

    return 1 if open_char == close_char else 0