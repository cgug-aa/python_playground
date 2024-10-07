class BHeap:
    def __init__(self, a):          #이진힙 생성
        self.a=a                    #리스트 a
        self.N=len(a)-1             #항목 수

    def create_heap(self):          #초기 힙 만들기
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

# 상향식 힙 만들기
# 아이디어: 상향식 방식으로 각 노드에 대해 힙속성을 만족하도록 부모와 자식을 서로 교환
#           n개의 항목이 배역에 임의의 순소러 저장되어 있을 때, 힙을 만들기 위해선
#           a[n/2]부터 a[1]까지 차례로 downheap을 각각 수행하여 힙 속성을 충족시킨다.

    def insert(self, key_value):    #삽입 연산
        self.N +=1
        self.a.append(key_value)    #새 항목을 힙 마지막에 추가
        self.upheap(self.N)         #힙속성 회복시키기 위해

    def delete_min(self):           #최솟값 삭제 (상향식 힙이기 때문에 root를 삭제한다고 보면됨)
        if self.N==0:
            print('힙이 비어 있음')
            return None
        minimum=self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -=1
        self.downheap(1)            #힙속성 회복
        return minimum

    def downheap(self, i):          #힙 내려가며 힙속성 회복
        while 2*i <= self.N:
            k=2*i
            if k<self.N and self.a[k][0] > self.a[k+1][0]:  #자식 노드 중에 더 작은 값의 인덱스를 얻음
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i=k

    def upheap(self, j):            #힙 올라가며 힙속성 회복
        while j>1 and self.a[j//2][0] > self.a[j][0]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j=j//2

    def print_heap(self):
        for i in range(1, self.N+1):
            print('[ %2d' % self.a[i][0], self.a[i][1], ']', end="")
        print('\n힙 크기 =', self.N)

a=[]
a.append([90,'watermelon'])
a.append([80,'watermelon'])
a.append([70,'watermelon'])
a.append([50,'watermelon'])
a.append([60,'watermelon'])
a.append([20,'watermelon'])
a.append([30,'watermelon'])
a.append([35,'watermelon'])
a.append([10,'watermelon'])
a.append([15,'watermelon'])
a.append([45,'watermelon'])
a.append([40,'watermelon'])

b=BHeap(a)  #힙 객체 생성
print('힙 만들기 전: ')
b.print_heap()
b.create_heap()
print("최소힙: ")
b.print_heap()

#파이썬의 우선순위 큐를 위한 heapq 라이브러리
# heapq.heappush(heap, item) : insert()메소드와 동일
# heapq.heappop(heap)        : delete_min()메소드와 동일
# heapq.heappushpop(heap, item): item 삽입 후 delete_min() 수행
# heapq.heapify(x)           : create_heap() 메소드와 동일
# heapq.heapreplace(heap, item): delete_min() 먼저 수행 후, item 삽입
# 주의사항: 힙의 항목 수가 많아지면 이 연산들은 매우 비효율적이므로 사용 지양.