# https://codility.com/demo/take-sample-test/equi_leader


def solution(A):
    count = len(A)

    if count == 1:
        return 0

    size = 0
    for i, val in enumerate(A):
        if size == 0:
            candidate = val
            size += 1
        else:
            if val == candidate:
                size += 1
            else:
                size -= 1

    leader_occurrence = 0
    for val in A:
        if candidate == val:
            leader_occurrence += 1

    if count // 2 > leader_occurrence:
        return 0

    equi_leader = 0
    leader_occurrence_in_first_part = 0
    for i in range(1, count):
        if candidate == A[i-1]:
            leader_occurrence_in_first_part += 1

        first_part = True if i // 2 < leader_occurrence_in_first_part else False
        second_part = True if (count - i) // 2 < leader_occurrence - leader_occurrence_in_first_part else False

        if first_part and second_part:
            equi_leader += 1

    return equi_leader