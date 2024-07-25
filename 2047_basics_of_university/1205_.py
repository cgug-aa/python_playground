#등수 구하기 [실버 4]

class solution():
    def __init__(self, n, score, p):
        self.n=n
        self.score=score
        self.p=p
    
    def ranking_setting(self, string):
        self.ranking=list(map(int, string.split()))
        self.ranking.append(self.score)
        self.ranking.sort(reverse=True)

    def slicing_ranking(self):
        self.ranking=self.ranking[:self.p]

    def chulsoo_position(self, list):
        '''
        c_idx=list.index(self.score)
        if type(c_idx)==int and c_idx!=len(list)-1:
            print(c_idx+1)
        else:
            print(-1)
        ''' 

    def answer(self):
        self.ranking_setting(input())
        self.slicing_ranking()
        self.chulsoo_position(self.ranking)




N, score, P= map(int, input().split())
sol=solution(N, score, P)
sol.answer()

# 알게 된 점
# 1) 리스트 원소 자료형 변환: list(map(자료형, 리스트)) 
# 2) 리스트 내장 함수 index는 찾는 원소가 리스트에 없으면 ValueError가 발생한다. 