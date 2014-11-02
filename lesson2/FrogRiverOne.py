# https://codility.com/demo/take-sample-test/frog_river_one

def solution(X, A):
    path = [-1] * X

    for time, position in enumerate(A):
        if path[position - 1] is -1:
            path[position - 1] = time

    if -1 in path:
        return -1
    else:
        return max(path)