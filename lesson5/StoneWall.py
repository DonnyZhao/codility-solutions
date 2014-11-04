# https://codility.com/demo/take-sample-test/stone_wall


def solution(H):
    """
    http://blog.codility.com/2012/06/sigma-2012-codility-programming.html
    """

    stones = 0
    stack = [0] * len(H)
    stack_num = 0

    for current_height in H:
        while stack_num > 0 and stack[stack_num - 1] > current_height:
            stack_num -= 1

        if stack_num == 0 or (stack_num > 0 and stack[stack_num - 1] != current_height):
            stones += 1
            stack[stack_num] = current_height
            stack_num += 1

    return stones