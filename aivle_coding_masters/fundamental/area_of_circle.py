# 원의 넓이

area=int(input())**2*3.14
if (area*100)%10!=0:
    print('{:.2f}'.format(area))
elif (area*10)%10!=0:
    print('{:.1f}'.format(area))
else:
    print(int(area))
    