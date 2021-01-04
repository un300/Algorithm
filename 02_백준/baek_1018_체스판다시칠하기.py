def board_check(input_array):

    white_chess_board = [
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ]

    black_chess_board = [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ]
    
    white_inconsistency = 0
    black_inconsistency = 0
    for input_list, white_list, black_list in zip(input_array, white_chess_board, black_chess_board):
        for input_cell, white_cell, black_cell in zip(input_list, white_list, black_list):
            if input_cell != white_cell:
                white_inconsistency += 1
            elif input_cell != black_cell:
                black_inconsistency += 1
    return white_inconsistency, black_inconsistency



M, N = map(int, input().split())

input_board = []
for _ in range(M):
    input_list = list(input())
    input_board.append(input_list)

white_nomatch_list = []
black_nomatch_list = []
for row in range( (M-8) + 1):
    for col in range( (N-8) + 1 ):
        input_board_part = [element[col:col+8] for element in input_board[row:row+8]]
        
        white_nomatch, black_nomatch = board_check(input_board_part)
        white_nomatch_list.append(white_nomatch)
        black_nomatch_list.append(black_nomatch)

all_nomatch_list = white_nomatch_list + black_nomatch_list
print(min(all_nomatch_list))


# python3 통과