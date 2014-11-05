# https://codility.com/demo/take-sample-test/dominator


def solution(A):
    num = len(A)
    if num == 0:
        return -1

    sorted_input = sorted(A)

    dominators_count = [0]
    dominators = [sorted_input[0]]
    last_val = sorted_input[0]
    for val in sorted_input:
        if val == last_val:
            dominators_count[-1] += 1
        else:
            last_val = val
            dominators.append(val)
            dominators_count.append(1)

    dominator_occurrence = max(dominators_count)
    dominator_candidate = dominators[dominators_count.index(dominator_occurrence)]

    if num // 2 < dominator_occurrence:
        return A.index(dominator_candidate)
    else:
        return -1