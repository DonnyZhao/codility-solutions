# https://codility.com/demo/take-sample-test/max_product_of_three


def solution(A):
    A.sort()

    min1 = A[0]
    min2 = A[1]
    max1 = A[-1]
    max2 = A[-2]
    max3 = A[-3]

    product1 = min1 * min2 * max1
    product2 = max1 * max2 * max3

    return product1 if product1 > product2 else product2