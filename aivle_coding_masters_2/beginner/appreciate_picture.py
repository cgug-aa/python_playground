# 그림 감상

palette=[input() for _ in range(4)]
checker=0
for col_idx in range(3):
    for row_idx in range(3):
        count=0
        count+=1 if palette[col_idx][row_idx]=='X' else 0
        count+=1 if palette[col_idx+1][row_idx]=='X' else 0
        count+=1 if palette[col_idx][row_idx+1]=='X' else 0
        count+=1 if palette[col_idx+1][row_idx+1]=='X' else 0

        if count>=3:
            checker=1
            break
if checker:
    print('yes')
else:
    print('no')