#디지털 티비 [브론즈 1]

def button1(p):
    p+=1
def button2(p):
    p-=1
def button3(list, p):
    list[p], list[p+1]=list[p+1], list[p]
    p+=1
def button4(list, p):
    list[p-1], list[p]=list[p], list[p-1]
    p-=1
def search_channel(list, c):
    n=list.index(c)
    return n


def solution(N):
    channel=[]
    button=[]
    p=0

    for i in range(N):
        channel.append(input())
    k1=search_channel(channel, 'KBS1')
    k2=search_channel(channel, 'KBS2')
    
    #조건 부분
    '''
    
    '''



n=int(input())
solution(n)

# 조건문을 어떻게 짜야할까
# 버튼 1과 3을 다르게 쓰는 기준은?
# 버튼 2와 4를 다르게 쓰는 기준은?