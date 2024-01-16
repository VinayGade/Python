

t = int(input())
for i in range(t):
    s = str(input())
    l = list(s)
    if len(l) % 2 != 0:
        del l[len(l)//2]
    ll = l[:len(l)//2]
    l = l[len(l)//2:]
    if sorted(ll) == sorted(l):
        print("YES")
    else:
        print("NO")


