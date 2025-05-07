# Arno's Sleep Schedule

start=int(input())
end=int(input())

sleep= 24+end-start if start>=20 else end-start
print(sleep)