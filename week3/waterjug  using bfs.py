from collections import deque

def bfs_3jug(cap1, cap2, cap3, target):
    visited = set()
    queue = deque()

   
    queue.append((0, 0, 0, [])) 

    while queue:
        a, b, c, path = queue.popleft()

        if (a, b, c) in visited:
            continue

        visited.add((a, b, c))
        path = path + [(a, b, c)]

       
        if a == target or b == target or c == target:
            return path

        states = []

        
        states.append((cap1, b, c))
        states.append((a, cap2, c))
        states.append((a, b, cap3))

       
        states.append((0, b, c))
        states.append((a, 0, c))
        states.append((a, b, 0))

        
        pour = min(a, cap2 - b)
        states.append((a - pour, b + pour, c))

       
        pour = min(a, cap3 - c)
        states.append((a - pour, b, c + pour))

        
        pour = min(b, cap1 - a)
        states.append((a + pour, b - pour, c))

     
        pour = min(b, cap3 - c)
        states.append((a, b - pour, c + pour))

        pour = min(c, cap1 - a)
        states.append((a + pour, b, c - pour))

        
        pour = min(c, cap2 - b)
        states.append((a, b + pour, c - pour))

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], state[2], path))

    return None



cap1 = 8
cap2 = 5
cap3 = 3
target = 4

result = bfs_3jug(cap1, cap2, cap3, target)

if result:
    print("Steps to reach target:")
    for step in result:
        print(step)
else:
    print("No solution found.")
