N, K = map(int, input().split())

A_list = map(int, input().split())
B_list = map(int, input().split())

sorted_A_list = sorted(A_list, reverse=False)
sorted_B_list = sorted(B_list, reverse=True)

for index in range(K):
    if sorted_A_list[index] <= sorted_B_list[index]:
        break
    sorted_A_list[index], sorted_B_list[index] = sorted_B_list[index], sorted_A_list[index]

print(sum(sorted_A_list))