
## 그리디 알고리즘



def solution() :
    N = int(input())
    rope_list = []
    for _ in range(N) :
        rope_list.append(int(input()))

    rope_list.sort()
    
    length = len(rope_list)
    max_value = 0

    for idx in range(length) :
        min_rope = rope_list[idx]
        if max_value < min_rope * (length-idx) :
            max_value = min_rope * (length-idx)

    print(max_value)

solution()