v:int=6
E: list[tuple[int, int]] = [
    (0, 1),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 3),
    (2, 0),
    (2, 3),
    (2, 5),
    (3, 2),
    (3, 4),
    (3, 5),
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 5),
    (5, 0),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
]
l:list[list[int]]=[]
for i in range(0,v):
    t:list[int]=[]
    for j in range(0,v):
        if (i,j) not in E and i!=j :
            E.append((i,j))
            t.append(1)
        else:
            t.append(0)
    l.append(t)
print(E)
for row in l:
    print(row)
