graph = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

from collections import deque

def find_route(g, start, goal, route):
    visited = set()
    visited.add(start)
    deq = deque([])
    deq.append(start)
    while(len(deq) > 0):
        new_route = deq.popleft()
        if(new_route in visited):
            route += [new_route]
        if(new_route == goal):
            return route
        for next_node in g[new_route]:
            if(next_node in visited):
                continue
            else:
                visited.add(next_node)
                deq.append(next_node)
    return None

def find_route_d(g, start, goal, route, visited):
    visited.add(start)
    route += [start]
    if(start == goal):
        return route
    for next_node in g[start]:
        if(next_node in visited):
            continue
        else:
            return find_route_d(g, next_node, goal, route, visited)
    return None
                
print(find_route_d(graph, 'A', 'F', [], set()))
        
    