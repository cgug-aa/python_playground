#회색조
hex_code=input()
tmp=0
for idx in range(1,len(hex_code),2):
    tmp+=int(hex_code[idx:idx+2], 16)
    # 16진수를 10진수로 변환
    
gray = round(tmp/3)
gray_hex = f'{gray:02X}'
print(f'#{gray_hex}{gray_hex}{gray_hex}')