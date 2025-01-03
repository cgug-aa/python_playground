# 7의 개수 프로그래머스 [레벨 0]

arr1=[7, 77, 17]
arr2=[10, 29]

def solution(arr):
    count=0
    for num in arr:
        while True:
            q, r=divmod(num, 10)
            if r==7: count+=1
            if q==0: break
            num=q
    return count

print(solution(arr1))
print(solution(arr2))

'''
내 풀이의 단점: while문 때문에 숫자가 커지면 시간이 증가

sol) 숫자 전체를 문자열로 바꿔 계산을 한번에 하고, 컴프리헨션을 통해 빠르게 계산할 수 있다.
def solution(arr):
    return sum(str(num).count('7') for num in array)
'''