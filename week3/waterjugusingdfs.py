def dfs_3jug(cap1, cap2, cap3, target):
    visited = set()
    path = []

    def dfs(a, b, c):
        if (a, b, c) in visited:
            return False

        visited.add((a, b, c))
        path.append((a, b, c))

       
        if a == target or b == target or c == target:
            return True

        
        if dfs(cap1, b, c): return True
        if dfs(a, cap2, c): return True
        if dfs(a, b, cap3): return True

        
        if dfs(0, b, c): return True
        if dfs(a, 0, c): return True
        if dfs(a, b, 0): return True

       
        pour = min(a, cap2 - b)
        if dfs(a - pour, b + pour, c): return True

        
        pour = min(a, cap3 - c)
        if dfs(a - pour, b, c + pour): return True

        
        pour = min(b, cap1 - a)
        if dfs(a + pour, b - pour, c): return True

        
        pour = min(b, cap3 - c)
        if dfs(a, b - pour, c + pour): return True

       
        pour = min(c, cap1 - a)
        if dfs(a + pour, b, c - pour): return True

       
        pour = min(c, cap2 - b)
        if dfs(a, b + pour, c - pour): return True

        path.pop()
        return False

    if dfs(0, 0, 0):
        return path
    else:
        return None



cap1 = 8
cap2 = 5
cap3 = 3
target = 4

result = dfs_3jug(cap1, cap2, cap3, target)

if result:
    print("Steps to reach target:")
    for step in result:
        print(step)
else:
    print("No solution found.")
