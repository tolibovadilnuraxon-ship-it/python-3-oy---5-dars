def ijobiy_yigindi(*sonlar):
    yigindi = 0
    for s in sonlar:
        if s > 0:
            yigindi += s
    return yigindi

n = int(input())
sonlar = list(map(int, input().split()))
print(ijobiy_yigindi(*sonlar))
