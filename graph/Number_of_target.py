# 타겟 넘버 프로그래머스 [레벨 2]

# 아이디어: -/+로 이루어진 이진 트리라고 생각하고, 순회하여 순회 결과가 target과 같은 경우 카운팅
number1=[1, 1, 1, 1, 1]
target1=3
number2=[4, 1, 2, 1]
target2=4
cal=['-']

def dfs(cal: list, numbers):
    if len(cal)==len(numbers):
        result=0
        for c, n in  zip(cal, numbers):
            result+=n if cal=='+' else -n
        return result
    else:
        return dfs(cal.append('-'), numbers), dfs(cal.append('+'), numbers)
def solution(numbers, cal, target):
    count=0
    if dfs(cal, numbers)==target:
        count+=1
    return count

print(solution(number1, cal,target1))
    
