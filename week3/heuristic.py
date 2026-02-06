import heapq

goal = (1,2,3,4,5,6,7,8,0)

def h(state):
    return sum(abs(i//3 - goal.index(state[i])//3) +
               abs(i%3 - goal.index(state[i])%3)
               for i in range(9) if state[i] != 0)

def neighbors(s):
    moves = {0:[1,3],1:[0,2,4],2:[1,5],
             3:[0,4,6],4:[1,3,5,7],5:[2,4,8],
             6:[3,7],7:[4,6,8],8:[5,7]}
    
    z = s.index(0)
    res = []
    
    for m in moves[z]:
        t = list(s)
        t[z], t[m] = t[m], t[z]
        res.append(tuple(t))
    
    return res

def heuristic_search(start):
    pq = [(h(start), start)]
    visited = set()
    
    while pq:
        _, state = heapq.heappop(pq)
        
        if state == goal:
            return state
        
        visited.add(state)
        
        for n in neighbors(state):
            if n not in visited:
                heapq.heappush(pq, (h(n), n))

start = (1,2,3,4,0,6,7,5,8)
print(heuristic_search(start))
