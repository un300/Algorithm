



def solution() :
    N = int(input())
    score_list = []
    for _ in range(N) :
        score_list.append(int(input()))
    

    score_list = score_list[::-1]
    answer = 0
    for idx in range(N-1) :
        if score_list[idx] <= score_list[idx+1] :
            answer += (score_list[idx+1] - score_list[idx] + 1)
            score_list[idx+1] = score_list[idx] - 1

    return answer


print(solution())