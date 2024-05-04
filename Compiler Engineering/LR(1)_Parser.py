nG=int(input("Enter the number of productions:"))
G=[]
print("Enter the productions:")
for i in range(nG):
	G.append(input())

T=[]
NT=[]
for i in G:
	j=i.split("->")
	if j[0] not in NT and j[0].isupper():
		NT.append(j[0])
	y=j[1].split()
	for x in y:
		if x not in T and not(x.isupper()):
			T.append(x)
T.insert(0,"$")
NT.pop(0)
n=int(input("Enter the number of states:"))
Action={}
Goto={}
print("Enter ! if absent and acc for accepted.")
for i in range(n):
	print("Action for state "+str(i)+":")
	for j in T:
		Action[(str(i),j)]=input(j+":")
	print("Goto for state "+str(i)+":")
	for j in NT:
		Goto[(str(i),j)]=input(j+":")
print(Action)
print(Goto)

inp=input("Enter a string:")
inp=inp+"$"
print(("{:20}"*6).format("Iteration","State","word","Stack","Handle","Action"))
i=0
j=1
Stack=["$","0"]
flag=0
while True:
	word=inp[i]
	State=Stack[-1]
	StackP=" ".join(Stack)
	key=(State,word)
	if key not in Action or Action[key]=="!":
		print("Invalid input")
		break
	ac=Action[key]
	if ac=="acc":
		Handle=Stack[-2]
		flag=1
	elif ac[0]=='s':
		Handle="None"
		Stack.extend([word,ac[1:]])
		i+=1
	elif ac[0]=='r':
		r=int(ac[1:])-1
		g=G[r]
		X=g.split("->")
		Y=X[1].split()
		Handle=X[1]
		Stack=Stack[:-(2*len(Y))]
		key=(Stack[-1],X[0])
		if key not in Goto or Goto[key]=="!":
			print("Invalid input")
			break
		Go=Goto[key]
		Stack.extend([X[0],Go])
	print(("{:<20}"*6).format(str(j),State,word,StackP,Handle,ac))
	if flag==1:
		break
	j+=1
		
'''
1.
G=["G->L","L->L P","L->P","P->( P )","P->( )"]
States=12
Action={('0', '$'): '!', ('0', '('): 's3', ('0', ')'): '!', ('1', '$'): 'acc', ('1', '('): 's3', ('1', ')'): '!', ('2', '$'): 'r3', ('2', '('): 'r3', ('2', ')'): '!', ('3', '$'): '!', ('3', '('): 's6', ('3', ')'): 's7', ('4', '$'): 'r2', ('4', '('): 'r2', ('4', ')'): '!', ('5', '$'): '!', ('5', '('): '!', ('5', ')'): 's8', ('6', '$'): '!', ('6', '('): 's6', ('6', ')'): 's10', ('7', '$'): 'r5', ('7', '('): 'r5', ('7', ')'): '!', ('8', '$'): 'r4', ('8', '('): 'r4', ('8', ')'): '!', ('9', '$'): '!', ('9', '('): '!', ('9', ')'): 's11', ('10', '$'): '!', ('10', '('): '!', ('10', ')'): 'r5', ('11', '$'): '!', ('11', '('): '!', ('11', ')'): 'r4'}
Goto={('0', 'L'): '1', ('0', 'P'): '2', ('1', 'L'): '!', ('1', 'P'): '4', ('2', 'L'): '!', ('2', 'P'): '!', ('3', 'L'): '!', ('3', 'P'): '5', ('4', 'L'): '!', ('4', 'P'): '!', ('5', 'L'): '!', ('5', 'P'): '!', ('6', 'L'): '!', ('6', 'P'): '9', ('7', 'L'): '!', ('7', 'P'): '!', ('8', 'L'): '!', ('8', 'P'): '!', ('9', 'L'): '!', ('9', 'P'): '!', ('10', 'L'): '!', ('10', 'P'): '!', ('11', 'L'): '!', ('11', 'P'): '!'}
Inputs: 	i.	()	Accepted
		ii.	(())()	Accepted
		iii.	((()) 	Not Accepted
'''	
	
