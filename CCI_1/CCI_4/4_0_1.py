graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find_route(gph, _from, _to, path):
    path += [_from]
    if(_from == _to):
        return path
    if(_from not in gph):
        return None
    for next in gph[_from]:
        if(next not in path):
            newpath = find_route(gph, next, _to, path)
            if newpath:
                return newpath
    return None
