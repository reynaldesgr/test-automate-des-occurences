def pp(G, s):
    P = {s : None}
    for v in G[s]:
        if v not in P:
            P[v] = s
            dfs(G, P, v)
    return P

""" dfs """
def dfs(G, P, u):
    for v in G[u]:
        if v not in P:
            P[v] = u
            dfs(G, P, v)

""" bfs """
def bfs(G, s):
    P, Q = {s : None}, [s]
    while Q:
        u = Q.pop(0)
        for v in G[u]:
            if v in P : continue
            P[v] = u
            Q.append(v)
    return P

def f(G, s, v):
    P  = bfs(G, s)
    ch = [v]
    while P[v]:
        ch.append(P[v])
        v = P[v]
    ch.reverse()
    return ch

G      = dict()
G['a'] = ['b', 'c']
G['b'] = ['a', 'd', 'e']
G['c'] = ['a', 'd']
G['d'] = ['b', 'c', 'e']
G['e'] = ['b', 'd', 'f', 'g']
G['f'] = ['e', 'g']
G['g'] = ['e', 'f', 'h']
G['h'] = ['g']

print(bfs(G, 'g'))
#print(f(G, 'b', 'f'))
print(pp(G, 'g'))