

MAX = 200005

def add_num(nn, x):
    if nn == -1:
        return
    Tree[nn][0] += x
    for ni in Tree[nn][1]:
        add_num(ni, x)


ipt = input().split()
N = int(ipt[0])
Q = int(ipt[1])



Tree = []
for m in range(MAX-1):
    Tree.append([-1, [-1]])

nodes = set()
nodes.add(1)

for i in range(N-1):
    ipti = input().split()
    a = int(ipti[0])
    b = int(ipti[1])

    Tree[a][0] = 0
    Tree[a][1].insert(0, b)
    Tree[b][0] = 0

    nodes.add(b)



for i in range(Q):
    ipti = input().split()
    p = int(ipti[0])
    x = int(ipti[1])

    cands = set()

    Tree[p][0] += x

    for pi in range(p,MAX-1):
        if Tree[pi] == -1:
            break
        for pii in Tree[pi][1]:
            cands.add(pii)
    for ci in cands:
        Tree[ci][0] += x

    #add_num(p, x)


for n in nodes:
    print(Tree[n][0])






