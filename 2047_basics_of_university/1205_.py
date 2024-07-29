#등수 구하기 [실버 4]

class solution():
    def __init__(self, n, score, p):
        self.n=n
        self.score=score
        self.p=p
    
    def ranking_setting(self):
        if self.n>0:
            self.ranking=list(map(int, input().split()))
            self.ranking.append(self.score)
            self.ranking.sort(reverse=True)
        else:
            self.ranking=[]
            self.ranking.append(self.score)

    def slicing_ranking(self, list):
        if self.n>=self.p:
            if list[self.p-1]==list[self.p]:
                idx=self.ranking.index(list[self.p])
                self.ranking=list[:idx]
            else:
                self.ranking=list[:self.p]
        else:
            pass

    def chulsoo_position(self, list):
        try:
            c_idx=list.index(self.score)
            print(c_idx+1)
        except ValueError:
            print(-1)


    def answer(self):
        self.ranking_setting()               #EOFError: "self.ranking_setting(input())" 현재 차트에 아무것도 없을 때, 입력이 없는데 입력을 받으려고 하고 있음.
        self.slicing_ranking(self.ranking)
        self.chulsoo_position(self.ranking)


N, score, P= map(int, input().split())
sol=solution(N, score, P)
sol.answer()

# 알게 된 점
# 1) 리스트 원소 자료형 변환: list(map(자료형, 리스트)) 
# 2) 리스트 내장 함수 index는 찾는 원소가 리스트에 없으면 ValueError가 발생한다.
# 3) EOFError 란
#     EOFError는 "End Of File Error"의 약자로, 파일을 읽을 때 파일의 끝을 만나면 발생하는 에러.
#     말 그대로 파일의 끝에 도달했을 때 더 이상 읽을 내용이 없어서 발생하는 에러.
#     혹은 파일을 읽는 도중 사용자가 예상치 못한 입력을 했을 때 발생할 수도 있다.
#   -> *입력이 없을 때도 고려해서 코드를 작성해야 됨.*