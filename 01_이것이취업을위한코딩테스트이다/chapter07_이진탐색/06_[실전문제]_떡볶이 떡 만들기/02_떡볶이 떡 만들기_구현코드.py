only_plus = lambda x : 0 if x <= 0 else x


N, M = map(int, input().split())
dduk_list = list(map(int, input().split()))

H = max(dduk_list)
s = 0

while s < M :
    cut_dduk_list = list(map(lambda x : only_plus(x-H), dduk_list))
    s = sum(cut_dduk_list)
    H -= 1

print(H+1)