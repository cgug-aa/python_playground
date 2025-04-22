# 배수 만들기

N=int(input())
nums=list(map(int, input().split()))

if N==1:
    if nums[0]!=0:
        print(-1)
    else:
        print(0)
elif N==2:
    print(-1)
else:
    if str(nums).count('0')<2:
        print(-1)
    else:
        nums.remove(0)
        nums.remove(0)
        if sum(nums)%3!=0:
            print(-1)
        else:
            nums.sort(reverse=True)
            for n in nums:
                print(n, end='')
            print('00')