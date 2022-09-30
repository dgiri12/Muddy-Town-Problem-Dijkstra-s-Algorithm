# This code is contributed by AnkitRai01
# code source: https://www.geeksforgeeks.org/check-if-a-directed-graph-is-connected-or-not/

N = 100000

gr1 = {}
gr2={}

vis1 = [0] * N
vis2 = [0] * N

def addEdge(u, v):
    if u not in gr1:
        gr1[u] = []

    if v not in gr2:
        gr2[v] = []

    gr1[u].append(v)
    gr2[v].append(u)

def dfs1(x):
    vis1[x] = True
    if x not in gr1:
        gr1[x] = {}

    for i in gr1[x]:
        if (not vis1[i]):
            dfs1(i)

def dfs2(x):
    vis2[x] = True

    if x not in gr2:
        gr2[x] = {}

    for i in gr2[x]:
       if (not vis2[i]):
           dfs2(i)

def isConnected(n):
    global vis1
    global vis2

    vis1 = [False] * len(vis1)
    dfs1(1)

    vis2 = [False] * len(vis2)
    dfs2(1)

    for i in range(1, n + 1):
        if (not vis1[i] and not vis2[i]):
            return False

    return True

def run1():
    n = 4

    addEdge(1, 2)
    addEdge(1, 3)
    addEdge(2, 3)
    addEdge(3, 4)

    if (isConnected(n)):
        print("Yes")
    else:
        print ("No")

def run2():
    n = 5

    addEdge(1, 2)
    addEdge(3, 4)
    addEdge(4, 5)

    if (isConnected(n)):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    run1()

