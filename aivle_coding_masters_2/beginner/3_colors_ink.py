# 삼색 잉크

months = [(1,31), (2,28), (3,31), (4,30), (5,31), (6,30), (7,31), (8,31),
           (9,30), (10,31), (11,30), (12,31)]
ink = [[0, 0, 0] for _ in range(10)]
start = input()
week_day={'SUN': 0, 'MON': 1, 'TUE': 2, 'WED': 3,
            'THU': 4, 'FRI': 5, 'SAT': 6}
count = week_day[start]

N = int(input())
holidays = [tuple(map(int, input().split())) for _ in range(N)]
for m, days in months:
    for day in range(1, days+1):
        str_d=list(map(int, list(str(day))))
        if count%7==0 or (m, day) in holidays:
            for color_d in str_d:
                ink[color_d][0]+=1
        elif count%7==6:
            for color_d in str_d:
                ink[color_d][1]+=1
        else:
            for color_d in str_d:
                ink[color_d][2]+=1
        count+=1
for ik in ink:
    print(f'{ik[0]} {ik[1]} {ik[2]}')