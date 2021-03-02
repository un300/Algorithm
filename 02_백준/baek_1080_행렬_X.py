

def match(A, B, N, M) :
    max_value = 0
    max_location = (None, None)
    for row in range(N-2) :
        for col in range(M-2) :
            part_A = sum(list(map(lambda x : x[col:col+3], A[row:row+3])), [])
            part_B = sum(list(map(lambda x : x[col:col+3], B[row:row+3])), [])

            cnt = 0
            
            for element_A, element_B in zip(part_A, part_B) :
                if element_A != element_B :
                    cnt += 1

            if cnt > max_value :
                max_value = cnt
                max_location = (row, col)

    return max_location


def switch(array, location) :
    start_row, start_col = location
    
    for row in range(start_row, start_row+3) :
        for col in range(start_col, start_col+3) :
            array[row][col] = not array[row][col]

    return array





def solution() :
    N, M = map(int, input().split())

    A = [ list(map(lambda x : bool(int(x)), input())) for _ in range(N) ]
    B = [ list(map(lambda x : bool(int(x)), input())) for _ in range(N) ]

    cnt = 0
    while A != B :
        location = match(A, B, N, M)
        A = switch(A, location)
        cnt += 1

        if cnt > (N-2) * (M-2) :
            cnt = -1
            break

    print(cnt)

    

solution()