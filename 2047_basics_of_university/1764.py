#듣보잡 [실버 4]

class solution:
    def __init__(self, n, m):
        self.n=n
        self.m=m
        self.DL=set()           #
        self.DS=set()           #
        self.DLS=[]

    def name_set(self, set):
        set.add(input())
    
    def set_setting(self, set, num):
        for i in range(num):
            self.name_set(set)
    
    def list_duplication(self):                     #
        self.DLS = sorted(list(self.DL & self.DS))
    
    def print_answer(self):
        print(len(self.DLS))
        for name in self.DLS:
            print(name)
    
    def answer(self):
        self.set_setting(self.DL, self.n)
        self.set_setting(self.DS, self.m)
        self.list_duplication()
        self.print_answer()

N, M = map(int, input().split())
test=solution(N, M)
test.answer()


# <알아가야할 것>
# 1) 줄바꿈도 split()으로 쪼개진다..
# 2) set이라는 집합 활용 (매소드?)
#   - 교집합 : &
#   - 합집합 : |
#   - 차집합 : -
#   - 집합에 값 추가하기
#       i) set.add()으로 단일 값 추가
#       ii) set.update()로 여러 값 추가
#   - 집합에서 특정값 제거 : remove()
# 3) 비교 연산에서 순차 비교?는 비효율적 -> 대책 마련 알기(여기선 집합으로 중복값 찾음)

#추가 공부 내용
'''
for문에 변수 2개 사용하는 방법
 1) enumerate(반복 가능값, 인덱스 시작 지점) -> 반복 가능한 변수의 인덱스를 부여해서 대입

    for r_idx, row in enumerate(list, 1)
        print(r_idx, row)
        # 1 'row[0]'
        # 2 'row[1]'
        # 3 'row[2]'

 2) zip(반복가능1, 반복가능2) -> 반복 가능한 두 변수에서 같은 인덱스를 갖는 값을 짝지어 대입

    for i, j in zip(list1, list2)
        print(i, j)
        # list1[0] list2[0]
        # list1[1] list2[1]
        # list1[2] list2[2]  
'''