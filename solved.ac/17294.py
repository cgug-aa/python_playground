# 귀여운 수~ε٩(๑> ₃ <)۶з [브론즈 1]

import sys
input=sys.stdin.readline
output=sys.stdout.write

k=input().rstrip()
check=True
for idx in range(0,len(k)-1):
    if idx==0:
        gap=int(k[idx+1])-int(k[idx])
        continue
    if gap!=(int(k[idx+1])-int(k[idx])):
        check=False
        break
if check:
    output("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    output("흥칫뿡!! <(￣ ﹌ ￣)>")
