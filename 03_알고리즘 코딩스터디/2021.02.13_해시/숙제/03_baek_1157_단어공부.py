word = list(input().strip().upper())

count_dict = {}

for alphabet in word :
    if alphabet not in count_dict.keys() :
        count_dict[alphabet] = 0
    else :
        count_dict[alphabet] += 1


sorted_dict = sorted(count_dict.items(), key=lambda x : x[1], reverse=True)

if len(sorted_dict) == 1:
    print(sorted_dict[0][0])
elif sorted_dict[0][1] == sorted_dict[1][1] :
    print('?')
else :
    print(sorted_dict[0][0])