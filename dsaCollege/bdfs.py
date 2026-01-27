g = {
    "a": ["b", "c", "e"],
    "b": ["a", "d"],
    "c": ["a", "f"],
    "d": ["b"],
    "e": ["a", "f"],  
    "f": ["c", "e"]
}

#bfs
def bfs(q, v):
    if q == []:
        return

    x = q[0]
    print(x, end=" ")
    q = q[1:]

    for i in g[x]:
        if i not in v:
            v.append(i)
            q.append(i)

    bfs(q, v)

bfs(["a"], ["a"])
print()