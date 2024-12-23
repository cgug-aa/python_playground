# 옹알이(1) 프로그래머스 [레벨 0]
can_speak=['aya', 'ye', 'woo', 'ma']
count=0

babbling1=['aya', 'yee', 'u', 'maa', 'wyeoo']
babbling2=['ayaye', 'uuuma', 'ye', 'yemawoo', 'ayaa']
for c in babbling2:
    for s in can_speak:
        if c.find(s)!=-1:
            c=c.replace(s,' ')
    if len(c.strip())==0:
        count+=1
print(count)

'''
주의: replace의 결과를 저장하기 위해 리턴값을 받아줘야한다.
'''