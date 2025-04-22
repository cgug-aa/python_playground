#N을 보는 시각

N=int(input())

# 1시간 = 60분 = 3600초

seconds=0
for hour in range(24):
    if str(N) in str(hour):
        seconds+=3600
    else:
        for minute in range(60):
            if str(N) in str(minute):
                seconds+=60
            else:
                for sec in range(60):
                    if str(N) in str(sec):
                        seconds+=1
print(seconds)