# 최댓값 연산

x, y, z = map(int, input().split())

arr = [x, y, z]
arr.sort()

if arr[0]==arr[1] and arr[1]!=arr[2]:
    print('impossible')
elif arr[0]!=arr[1] and arr[1]!=arr[2]:
    print('impossible')
else:
    print('possible')
    
# 가능한 경우의 수
# 1) a, b, c 모두 같을 때 1 1 1 > 1 1 1
# 2) a, b가 같을 때 1 1 2    > 1 2 2 
# 3) b, c가 같을 때 1 2 2    > 2 2 2
# 4) a, b, c 다 다를 때 1 2 3 > 2 3 3 