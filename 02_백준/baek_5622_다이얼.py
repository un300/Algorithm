
input_alphabet_list = input()

dial_dict = {
    'ABC'  : 2 + 1,
    'DEF'  : 3 + 1,
    'GHI'  : 4 + 1,
    'JKL'  : 5 + 1,
    'MNO'  : 6 + 1,
    'PQRS' : 7 + 1,
    'TUV'  : 8 + 1,
    'WXYZ' : 9 + 1
}

answer_list = []
for key in dial_dict.keys() :
    for alphabet in input_alphabet_list :
        if alphabet in key :
            answer_list.append(dial_dict[key])


print(sum(answer_list))