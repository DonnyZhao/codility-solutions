# https://codility.com/demo/take-sample-test/passing_cars


def solution(A):
    go_to_east = 0
    passing = 0

    for car_direction in A:
        if car_direction == 1:
            passing += go_to_east
        else:
            go_to_east += 1

    return passing if passing <= 1000000000 else -1