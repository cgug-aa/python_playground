# 시각 [난이도 1]

# 0시 0분 0초에서 N시 59분 59초까지 3이 들어가면 카운팅
# 시간: 3600초
# 분: 60초

N=int(input())
count=0

# N시간을 초로 변환
seconds=(N+1)*3600

for s in range(seconds):
    h=s//3600
    m=(s%3600)//60
    sec=(s%3600)%60

    if '3' in str(h) or '3' in str(m) or '3' in str(sec):
    # sol) if '3' in str(h) + str(m) + str(sec):
        count+=1
print(count)

# 출제 의도)
# 23시 59분 59초까지 모두 카운팅 한다고 해도 86,400가지이므로 모든 초를 카운팅해도 100,000개도 되지않아
# 2초 제한시간을 넘지 않을 것