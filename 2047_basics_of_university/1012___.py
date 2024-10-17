# 유기농 배추 [실버 2]

import sys
input=sys.stdin.readline
# 테스트 횟수
T=int(input().rstrip())

# 카운팅 한 클러스터 지우기 -> 런타임 에러
def remove(a, b, numpy_array):
    if 0<=a<N and 0<=b<M and numpy_array[a][b]==1:
        numpy_array[a][b]=0
        remove(a-1, b, numpy_array)
        remove(a, b-1, numpy_array)
        remove(a+1, b, numpy_array)
        remove(a, b+1, numpy_array)
    else:
        return None

# 배추 클러스터 개수 파악
def check_cluster(location_list, numpy_array):
    count=0
    
    for loc in location_list:
        x, y = loc
        if numpy_array[x][y]==1:
            count+=1
            remove(x, y, numpy_array)
    return count


#가로, 세로, 심은 배추 개수
for _ in range(T):
    M, N, K= map(int, input().split())
    
    #밭 만들기
    cabbage=[]
    for _ in range(N):
        row=[0 for _ in range(M)]
        cabbage.append(row)

    cabbage_loc=[]
    #배추 심기
    for _ in range(K):
        a, b=map(int, input().split())
        cabbage_loc.append([b, a])              #a가 열, b가 행이므로
        cabbage[b][a]=1

    #배추 클러스터 파악
    print(check_cluster(cabbage_loc, cabbage))



# *주의 사항*  
#   1) 가로x세로 != 행x열
#   2) numpy 사용 불가
#   3) DFS, BFS