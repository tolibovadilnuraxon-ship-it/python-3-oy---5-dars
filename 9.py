baholar = list(map(int, input().split()))
katta_baholar = list(filter(lambda x: x > 70, baholar))
print(katta_baholar)
