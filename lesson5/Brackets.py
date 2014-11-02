# https://codility.com/demo/take-sample-test/brackets


def solution(S):
    if len(S) % 2 != 0:
        return 0

    stack = []
    for symbol in S:
        if symbol in ['[', '{', '(']:
            stack.append(symbol)
        else:
            if len(stack) == 0 \
                    or stack.pop() + symbol not in ['()', '[]', '{}']:
                return 0

    return 1 if len(stack) == 0 else 0