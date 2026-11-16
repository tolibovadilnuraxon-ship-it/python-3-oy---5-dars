def daraja(son, n=2):
    return son ** n

qator = list(map(int, input().split()))
if len(qator) == 2:
    print(daraja(qator[0], qator[1]))
else:
    print(daraja(qator[0]))
