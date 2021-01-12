N = int(input())

cnt = N
for _ in range(N) :
    input_chr = input()

    breaker = False
    for idx1, element1 in enumerate(input_chr) :
        for idx2, element2 in enumerate(input_chr) :
            if ( element1 == element2 ) & ( len(set(input_chr[idx1:idx2+1])) > 1 ) :
                cnt -= 1
                breaker = True
                break
        if breaker :
            break

print(cnt)