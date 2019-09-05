projects_string = "abcdef"

projects_flag = {x:False for x in projects_string}
print(projects_flag)


dependency = {'a':'d',
              'f':'b',
              'b':'d',
              'f':'a',
              'd':'c'
    }
def chk_all_true():
    for x in projects_flag:
        if(not projects_flag[x]):
            return False
    return True

def chk_dep(dep, _from, output):
    output += [_from]
    projects_flag[_from] = True
    if(_from in dep):
      projects_flag[dep[_from]] = True
      if(chk_all_true()):
          return output + [dep[_from]]
      else:
          chk_dep(dep, dep[_from], output)
    else:
        if(not chk_all_true()):
            output = []
            return output

out = []
for x in projects_string:
    chk_dep(dependency, x, out)
if(len(out) > 0):
    print(out)
