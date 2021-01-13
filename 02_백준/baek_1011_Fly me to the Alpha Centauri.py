T = int(input())

for _ in range(T) :
    x, y = map(int, input().split())
    y = y - 1  # 마지막은 거리를 1로 이동해야하기 떄문에 1뺴주고 cnt는 0이 아닌 1부터 시작

    move = 1
    cnt = 1
    while x < y :
        x += move
        cnt += 1
        move += 1
    
    print(cnt)