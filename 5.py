def yetkazish_haqi(narx, haq=5000):
    return narx + haq

qator = list(map(int, input().split()))
if len(qator) == 2:
    print(yetkazish_haqi(qator[0], qator[1]))
else:
    print(yetkazish_haqi(qator[0]))
