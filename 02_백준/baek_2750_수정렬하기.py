N = int(input())


all_list = []
for _ in range(N):
    input_num = int(input())
    all_list.append(input_num)

answer_list = sorted(all_list)

for element in answer_list:
    print(element)