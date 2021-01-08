import sys

N = int(sys.stdin.readline())

input_list = []
for _ in range(N):
    input_num = int(sys.stdin.readline())
    input_list.append(input_num)


input_list.sort()
# 산술평균
print( int(round( sum(input_list)/N, 0)) )

# 중앙값
idx = N // 2
print( input_list[idx] )

# 최빈값
cnt_dict = {}
for element in input_list:
    if element not in cnt_dict.keys():
        cnt_dict[element] = 0
    else :
        cnt_dict[element] += 1

mode_cnt = max(cnt_dict.values())
temp_list = [ key for key, value in cnt_dict.items() if value == mode_cnt  ]
if len(temp_list) > 1:
    temp_list.sort() 
    print(temp_list[1])
else :
    print(temp_list[0])

# 범위
print(input_list[N-1] - input_list[0])

