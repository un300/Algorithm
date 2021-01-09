import sys

N = int(sys.stdin.readline())


member_array = []
k = 0
for _ in range(N) :
    age, name = sys.stdin.readline().split()
    member_array.append([ k, int(age), name ])
    k += 1

sorted_array = sorted(member_array, key=lambda x : (x[1], x[0]))
for member_list in sorted_array :
    print('{} {}' .format(member_list[1], member_list[2]))