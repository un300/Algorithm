## 그리디 알고리즘


def solution() :
    arr = input().split('-')
    answer = []
    for element in arr :
        if '+' in element :
            temp = list(element.split('+'))
            new_element = sum(list(map(int, temp)))
            answer.append(new_element)
        else :
            answer.append(int(element))

    return answer[0] - sum(answer[1:])


print(solution())