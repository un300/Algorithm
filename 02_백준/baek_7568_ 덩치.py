N = int(input())

person_array = []
for _ in range(N) :
    temp_input = list(map(int, input().split()))
    person_array.append(temp_input)


rank_list = []

for person in person_array :
    rank = 1
    for idx in range(len(person_array)):
        compare_person = person_array[idx]
        if ( person[0] < compare_person[0] ) & ( person[1] <compare_person[1] ):
            rank += 1
    rank_list.append(rank)


answer = ' '.join(list(map(str, rank_list)))
print(answer)