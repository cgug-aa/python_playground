#팬그램

text = input()
text=text.upper()
length=len(set(text))
if length==26:
    print('YES')
else:
    print('NO')