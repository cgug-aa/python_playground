# 2차원으로 만들기 프로그래머스 [레벨 0]

num_list1=[1, 2, 3, 4, 5, 6, 7, 8]
n1=2
num_list2=[100, 95, 2, 4, 5, 6, 18, 33, 948]
n2=3

def solution(num_list, n):
    return [num_list[idx:idx+n] for idx in range(0, len(num_list), n)]

print(solution(num_list1, n1))
print(solution(num_list2, n2))