import copy
code=open('file.txt','r').read()
code=code.split('\n')
print(code)
res=[]; hasht=[]; rescode=[]
for i in code:
 z=0
 if(i[0] not in res):
  res.append(i[0])
  hasht.append([])
 if i[3]=='+' or i[3]=='*':
  hashv=[i[2]+i[3]+i[4],i[4]+i[3]+i[2]]
  for j in hasht:
   if hashv[0] in j or hashv[1] in j:
     rescode.append(i[0]+"="+str(res[hasht.index(j)]))
     hasht[res.index(i[0])]=hashv
     z+=1
     break
  if(z==0):
   hasht[res.index(i[0])]=hashv
   rescode.append(i[0]+"="+str(hashv))
 else:
  hashv=[i[2]+i[3]+i[4]]
  for j in hasht:
   if hashv[0] in j:
     rescode.append(i[0]+"="+str(res[hasht.index(j)]))
     hasht[res.index(i[0])]=hashv
     z+=1
     break
  if(z==0):
   hasht[res.index(i[0])]=hashv
   rescode.append(i[0]+"="+str(hashv))
for i in range(len(rescode)):
 print(rescode[i])
print(res,hasht)
