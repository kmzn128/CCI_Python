graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find_route(_g, _from, _to, path):
    path += [_from]
    if(_from == _to):
        return path
    if(_from not in _g):
        return None
    for node in _g[_from]:
        if node not in path:
            newpath = find_route(_g, node, _to, path)
            if newpath:
                return newpath
    return None

# def find_all_route(_g, _from, _to, path):
#     path += [_from]
#     if(_from == _to):
#         return [path]
#     paths = []
#     for node in _g[_from]:
#         if node not in path:
#             newpaths = find_all_route(_g, node, _to, path)
#         for newpath in newpaths:
#             paths.append(newpath)
#     return paths

result = find_route(graph, 'A', 'B', path=[])
print(result)