input_chr_list = input().strip()

croatia_alphabet_list= ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


if input_chr_list == ' ':
    print(0)
else :
    cnt = 0
    minus = 0
    for i in range(len(input_chr_list)-1):
        if input_chr_list[i:i+2] in croatia_alphabet_list :
            cnt += 1
            minus += 1
            
    for croatia_alphabet in croatia_alphabet_list :
        input_chr_list = input_chr_list.replace(croatia_alphabet, ' ')
    print(len(input_chr_list) + cnt - minus)

