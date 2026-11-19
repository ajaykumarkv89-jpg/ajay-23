def dfs (graph,source):
    stack=[]
    visited=[]
    stack.append(source)
    visited.append(source)
    
    while len (stack)!=0:
        vertex=stack.pop()
        print(vertex,end=" ")
        for u in graph[vertex]:
            if u not in visited:
                stack.append(u)
                visited.append(u)

#main
graph ={'A':['B','D'],'B':['C','F'],'C':['E','G','H'],'D':['F'],'E':['B','F'],'F':['A'],'G':['E','H'],'H':['A']}
print("given graph ",graph)
print("\n DFS taversal \n")
dfs(graph,"H")