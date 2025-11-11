# 삼각형과 세 변 [브론즈 3]

while(1):
    nums = list(map(int, input().split()))
    total = sum(nums)
    mval = max(nums)
    
    if total == 0 : break

    if total-mval*2 <= 0:
        print("Invalid")
    else:
        length=len(set(nums))
        if length==1:
            print('Equilateral')
        elif length==2:
            print('Isosceles')
        else:
            print('Scalene')