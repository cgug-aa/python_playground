# 연도 진행바 [실버 5]

import sys
input=sys.stdin.readline
output=sys.stdout.write

calendar = input().split()
calendar[3]=calendar[3].split(':')
month_dict={'January':31,
            'February':28,
            'March':31,
            'April':30,
            'May':31,
            'June':30,
            'July':31,
            'August':31,
            'September':30,
            'October':31,
            'November':30,
            'December':31}
days=365
if int(calendar[2])%400==0 or (int(calendar[2])%4 == 0 and int(calendar[2])%100!=0):
    days+=1
    month_dict['February']+=1

total_min = days * 1440
present_min=int(calendar[3][1])+60*int(calendar[3][0])+(int(calendar[1].replace(',',''))-1)*1440
for mon in month_dict.keys():
    if mon==calendar[0]:
        break
    present_min+=int(month_dict[mon]*1440)

output(str((present_min/total_min)*100))