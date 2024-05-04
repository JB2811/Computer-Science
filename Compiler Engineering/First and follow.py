import copy
gram=open('file2.txt','r').read()
gram=gram.split('\n')
print('\nGrammar: ',gram)
NT=[];T=[]; RHS=[]; LHS=[]

for i in gram:
 if i[0] not in NT:
  NT.append(i[0])
 RHS.append(i[2:])
 LHS.append(i[0])
for i in gram:
 for j in i:
  if j not in NT and j!='=' and j not in T:
   T.append(j)

print('Terminal: ',T,'\nNon-Terminals: ',NT,'\nLHS: ',LHS,"\nRHS: ",RHS)

firstset={}

for i in T:
 firstset.update({i:set(i)})

def first(i):
 if i in firstset.keys():
  return firstset[i]
 else:
  firstset.update({i:set()})
  for j in gram:
   if i==j[0] and j[2]!=i:
    if j[2] in T:
     firstset.update({i:firstset[i].union(set(j[2]))})
    else:
     firstset.update({i:firstset[i].union(set(first(j[2])))})
 return firstset[i]

for k in NT:
 first(k)

print("\nFIRST SET: ",firstset)

followset={}
def follow(i):
 for j in gram:
  if len(RHS[gram.index(j)])==3:
   if(i==j[3]):
    if('\\' in firstset[j[4]]):
     followset.update({i:followset[i].union(set(firstset[j[4]]-set('\\')).union(set(followset[j[4]])))})
    else:
     followset.update({i:followset[i].union(set(firstset[j[4]]))})
  elif len(RHS[gram.index(j)])==2:
   if(i==j[2]):
    if('\\' in firstset[j[3]]):
     followset.update({i:followset[i].union(set(firstset[j[3]]-set('\\')).union(set(followset[j[3]])))})
    else:
     followset.update({i:followset[i].union(set(firstset[j[3]]))})
   elif(i==j[3]):
    followset.update({i:followset[i].union(set(followset[j[0]]))})

 return followset[i]

f=copy.deepcopy(followset)

for k in NT:
 followset.update({k:set()})
 if k==NT[0]:
  followset.update({NT[0]:set('$')})

while(f!=followset):
 f=copy.deepcopy(followset)
 for k in NT:
  follow(k)
    
print('\nFOLLOW SET: ',followset)
