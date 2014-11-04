# https://codility.com/demo/take-sample-test/fish


def solution(A, B):
    alive_fish = 0
    fish_flow_down = []

    for i, current_fish_size in enumerate(A):
        if B[i] == 1:
            fish_flow_down.append(current_fish_size)
        else:
            while len(fish_flow_down) > 0:
                last_fish_flow_down = fish_flow_down.pop()
                if last_fish_flow_down > current_fish_size:
                    fish_flow_down.append(last_fish_flow_down)
                    break
            else:
                alive_fish += 1

    return alive_fish + len(fish_flow_down)