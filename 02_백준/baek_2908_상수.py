x, y = map(str, input().split())
answer_list = [ x[::-1], y[::-1] ]
print(max(answer_list))