


def solution() :
    N = int(input())
    
    digit_dict = {}
    word_list = []
    for _ in range(N) :
        word = input()
        word_list.append(word)

    for word in word_list :
        for idx, alphabet in enumerate(word[::-1]) :
            if alphabet not in digit_dict.keys() :
                digit_dict[alphabet] = 10**idx
            else :
                digit_dict[alphabet] += 10**idx

    
    answer = 0
    sorted_dict = sorted(digit_dict.items(), key=lambda x : x[1], reverse=True)
    digit_list = list(range(0, 10))
    for element in sorted_dict :
        answer += element[1] * digit_list.pop()
    print(answer)

solution()