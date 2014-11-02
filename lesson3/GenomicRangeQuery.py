# https://codility.com/demo/take-sample-test/genomic_range_query


def solution(S, P, Q):
    s_length = len(S)
    a = [0]
    c = [0]
    g = [0]
    t = [0]

    for i in range(1, s_length + 1):
        a.append(a[i - 1] + 1 if S[i - 1] is 'A' else a[i - 1])
        c.append(c[i - 1] + 1 if S[i - 1] is 'C' else c[i - 1])
        g.append(g[i - 1] + 1 if S[i - 1] is 'G' else g[i - 1])
        t.append(t[i - 1] + 1 if S[i - 1] is 'T' else t[i - 1])

    result = []
    for p, q in zip(P, Q):
        if a[q + 1] - a[p] > 0:
            result.append(1)
        elif c[q + 1] - c[p] > 0:
            result.append(2)
        elif g[q + 1] - g[p] > 0:
            result.append(3)
        else:
            result.append(4)
    return result