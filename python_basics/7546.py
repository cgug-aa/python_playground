#그릇 [브론즈 2]

stack=input()
height=10
for i in range(1, len(stack)):
    if stack[i-1]!=stack[i]:
        height+=10
    else:
        height+=5
print(height)