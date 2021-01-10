
alphabet_list = list(input().upper())

cnt_dict = {}


for alphabet in alphabet_list:
    if alphabet not in cnt_dict.keys() :
        cnt_dict[alphabet] = 0
    else : 
        cnt_dict[alphabet] += 1

sort_dict = sorted(cnt_dict.items(), key=lambda x : (x[1], x[0]), reverse=True)

if sort_dict[0][1] == sort_dict[1][1] :
    print('?')
else :
    print(sort_dict[0][0])
