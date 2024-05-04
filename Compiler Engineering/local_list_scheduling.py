cumulative_latency=[]; dependency_graph=[]; l=[]; delay=[]; ready=[]; active=[]; roots=[]; leaves=[]; s=[]; finished=[]; parent=[]

n=int(input("\nEnter the number of instructions: "))
dependency_graph=[0]*n
l=[0]*n

for i in range(n):
 dependency_graph[i]=[0]*n
 l[i]=[0]*n
 s.append(0)
 finished.append(0)
 parent.append([])
 cumulative_latency.append(0)
 delay.append(0)
 
d=int(input("\nEnter no' of dependencies: "))
print("\nEnter for each edge x y")
for i in range(d):
 x=int(input("\nEnter x: "))
 y=int(input("\nEnter y: "))
 dependency_graph[x][y]=1
 l[x][y]=int(input(f"\nEnter latency for {x}->{y}: "))
 delay[x]=l[x][y]
 parent[y].append(x)

for i in range(n):
 if dependency_graph[i].count(0)==n:
  roots.append(i)
  cumulative_latency[i]=int(input(f"\nEnter latency for root node {i}: "))

for i in range(n):
 if(parent[i]==[]):
  leaves.append(i)

def cal_cumulative_latency(i):
 if(cumulative_latency[i]!=0):
  return cumulative_latency[i]
 else:
  c=0
  for j in range(n):
   if(dependency_graph[i][j]==1):    
    c=c+cal_cumulative_latency(j)
  cumulative_latency[j]=c
  return cumulative_latency[j]  
for i in range(n):
 cumulative_latency[i]=cal_cumulative_latency(i)

for i in leaves:
 ready.append(i)
 
cycle=1
while(set(ready).union(set(active))!=set()):
 print(ready," ",active)
 if(ready!=[]):
  o=ready.pop(0)
  s[o]=cycle
  active.append(o)
 cycle+=1
 for o in active:
  if(s[o]+delay[o]<=cycle):
   active.remove(o)
   print("\nInstn scheduled: ",o," ",cycle )
   finished[o]=1
   for i in range(n):
    if(dependency_graph[o][i]==1 and finished[i]!=1 and i not in ready):
     z=1
     for j in parent[i]:
      if(finished[j]!=1):
       z=0
       break
     if(z):
      ready.append(i)
