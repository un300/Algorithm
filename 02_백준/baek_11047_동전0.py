## 그리디 알고리즘




def solution() :
    N, K = map(int, input().split())
    coin_kinds = []
    for _ in range(N) :
        coin_kinds.append(int(input()))
    
    coin_kinds.sort(reverse=True)
    answer = 0

    for coin in coin_kinds :
        answer += K // coin
        K = K % coin
    return answer        



print(solution())