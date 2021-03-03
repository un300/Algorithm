

# def match(A, B, N, M) :
#     max_value = 0
#     max_location = (None, None)
#     for row in range(N-2) :
#         for col in range(M-2) :
#             part_A = sum(list(map(lambda x : x[col:col+3], A[row:row+3])), [])
#             part_B = sum(list(map(lambda x : x[col:col+3], B[row:row+3])), [])

#             cnt = 0
            
#             for element_A, element_B in zip(part_A, part_B) :
#                 if element_A != element_B :
#                     cnt += 1

#             if cnt > max_value :
#                 max_value = cnt
#                 max_location = (row, col)

#     return max_location


# def switch(array, location) :
#     start_row, start_col = location
    
#     for row in range(start_row, start_row+3) :
#         for col in range(start_col, start_col+3) :
#             array[row][col] = not array[row][col]

#     return array





# def solution() :
#     N, M = map(int, input().split())

#     A = [ list(map(lambda x : bool(int(x)), input())) for _ in range(N) ]
#     B = [ list(map(lambda x : bool(int(x)), input())) for _ in range(N) ]

#     cnt = 0
#     while A != B :
#         location = match(A, B, N, M)
#         A = switch(A, location)
#         cnt += 1

#         if cnt > (N-2) * (M-2) :
#             cnt = -1
#             break

#     print(cnt)

    

# solution()




def convert(row, col, arr) :
    for r in range(row, row+3) :
        for c in range(col, col+3) :
            arr[r][c] = 1 - arr[r][c]
    return arr

def solution() :
    N, M = map(int, input().split())

    A = [ list(map(int, list(input()))) for _ in range(N) ]
    B = [ list(map(int, list(input()))) for _ in range(N) ]

    cnt = 0
    for r in range(0, N-2) :
        for c in range(0, M-2) :
            if A[r][c] != B[r][c] :
                A = convert(r, c, A)
                cnt += 1

    for r in range(N) :
        for c in range(M) :
            if A[r][c] != B[r][c] :
                print(-1)
                return

    print(cnt)

solution()

    











