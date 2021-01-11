import string

S = list(input())

lower_alphabet_list = string.ascii_lowercase


for alphabet in lower_alphabet_list :
    if alphabet in S :
        print(S.index(alphabet), end=' ')
    else :
        print(-1, end=' ')
