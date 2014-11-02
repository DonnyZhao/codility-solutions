# https://codility.com/demo/take-sample-test/number_of_disc_intersections


def solution(A):
    left_edges = []
    right_edges = []

    for center, radius in enumerate(A):
        left_edges.append(center - radius)
        right_edges.append(center + radius)

    sorted_left_edges = sorted(left_edges)
    sorted_right_edges = sorted(right_edges)

    left_index = 0
    intersects = 0
    discs_count = len(A)
    for right_index, right_edge in enumerate(sorted_right_edges):
        while left_index < discs_count and \
                right_edge >= sorted_left_edges[left_index]:
            left_index += 1

        intersects += left_index - right_index - 1

        if intersects > 10000000:
            return -1

    return intersects