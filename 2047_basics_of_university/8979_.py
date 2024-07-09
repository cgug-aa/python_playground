#올림픽 [실버 5]
#sort 함수 활용, lambda함수 사용, 문자열 슬라이싱 등 활용

N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)
idx = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(i)
        break

#sort와 sorted의 key, reverse 파라미터
#1) key로 정렬의 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
#   print(sorted(str_list, key=lambda x : x[1]))  # 람다
#   또한 key 파라미터를 여러개로 설정하면, 동일 조건에 차례로 처리할 수 있다.
#2) reverse를 통해 내림차순으로할지 오름차순으로 할지 결정할 수 있다.
#출처: https://develop247.tistory.com/234 [ImJay:티스토리]