# 모의고사 프로그래머스 [레벨 1]

'''
1번: 1,2,3,4,5,1,2,3, ..., 주기:5
2번: 2,1,2,3,2,4,2,5,2,1,  주기:8
3번: 3,3,1,1,2,2,4,4,5,5,3,3... 주기:10

문제는 10,000문제 존재하므로 5,8,10 모두 10,000의 약수이다.
따라서 5, 8, 10의 최소 공배수인 40문제까지만 고려하면 된다.
'''
s1=[1, 2, 3, 4, 5]
s2=[2, 1, 2, 3, 2, 4, 2, 5]
s3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answer1=[1, 2, 3, 4, 5]
answer2=[1, 3, 2, 4, 2]
def solution(answers):
    counts=[0, 0, 0, 0]
    for idx in range(40):
        q1=idx%5
        if s1[q1]==answers[q1]:
            counts[1]+=1
        if s2[(idx%8)]==answers[q1]:
            counts[2]+=1
        if s3[(idx%10)]==answers[q1]:
            counts[3]+=1
    tgt=max(counts)
    print(counts)
    return [idx for idx in range(1,4) if tgt==counts[idx]]

print(solution(answer1))
print(solution(answer2))

'''
문제의 의도: 문제의 개수=answers의 개수
awswers의 길이가 변하고, 그에 따라 s1, s2, s3가 결정된다.

def solution(answers):
    answer_types=[
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5]
    ]
    scores=[0,0,0]
    for type_idx, ans_type in enumerate(answer_types):
        for idx, ans in enumerate(answers):
            if ans==ans_type[idx%len(ans_type)]
                scores[type_idx]+=1

    return [idx+1 for idx, score in enumerate(scores) if score==max(scores)]
'''