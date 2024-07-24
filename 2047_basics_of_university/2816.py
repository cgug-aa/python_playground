#디지털 티비 [브론즈 1]

class sol:
    def __init__(self):
        self.channel=[]
        self.button=[]
        self.p=0
    def button1(self):
        self.button.append(1)
        self.p+=1
    def button2(self):
        self.button.append(2)
        self.p-=1
    def button3(self):
        self.button.append(3)
        self.channel[self.p], self.channel[self.p+1]=self.channel[self.p+1], self.channel[self.p]
        self.p+=1
    def button4(self):
        self.button.append(4)
        self.channel[self.p-1], self.channel[self.p]=self.channel[self.p], self.channel[self.p-1]
        self.p-=1
    def search_channel(self,c):
        n=self.channel.index(c)
        return n
    def print_button(self):
        for i in range(len(self.button)):
            print(self.button[i], end='')
    
    def channel_sort(self, N):
        for i in range(N):
            self.channel.append(input())
        
        #KBS1 설정 부분
        k1=self.search_channel('KBS1')
        if k1==0:
            pass
        else:
            while self.p+1<k1:
                self.button3()
            if self.p==0:
                self.button3()
            else:
                self.button1()
                while self.p>=1:
                    self.button4()

        #KBS2 설정 부분
        k2=self.search_channel('KBS2')
        if k2==1:
            pass
        else:
            while self.p+1<k2:
                self.button1()
            if self.p==1:
                self.button3()
            else:
                self.button1()
                while self.p>=2:
                    self.button4()

n=int(input())
solution=sol()
solution.channel_sort(n)
solution.print_button()

# 조건문을 어떻게 작성해야할까
'''
 버튼 1과 3을 다르게 쓰는 기준은?
 p+1이 k1이 될 때까지 3번
 p+1이 k1이면 p가 0이 될 때까지 1번 후 4번 반복
 KBS1을 위치시킨 뒤, KBS2는 동일한 기준 적용
'''

#주의사항
'''
항상 경계점의 관점 이용.
(시작점, 끝점)을 고려
'''