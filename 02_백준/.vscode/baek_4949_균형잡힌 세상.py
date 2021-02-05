sentence = list(input())
sentence.pop()
big   = 0
small = 0


stack = []
for element in sentence:
    if element == '[':
        stack.append(element)
        big += 1
    elif element == '(':
        stack.append(element)
        small += 1
    elif element == ')':
        if stack[-1] == '[':
            break
        else :
            small -= 1
    elif element == ']':
        if stack[-1] == '(':
            break
        else :
            big -= 1
    
    if (big<0) | (small<0):
        break

if (big==0) & (small==0):
    print('yes')
else :
    print('no')