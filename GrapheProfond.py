def dfs(G,s) :
	couleur=dict()
	for v in G :couleur[v]='blanc'
	P=dict()
	P[s]=None
	couleur[s]='gris'
	Q=[s]
	while Q :
		u=Q[-1]
		R=[y for y in G[u] if couleur[y]=='blanc']
		if R :
			v=R[0]
			couleur[v]='gris'
			P[v]=u
			Q.append(v)
		else :
			Q.pop()
			couleur[u]='noir'
	return P

 
	
	
# G=dict()
# G['a']=['b','c']
# G['b']=['a','d','e']
# G['c']=['a','d']
# G['d']=['b','c','e']
# G['e']=['b','d','f','g']
# G['f']=['e','g']
# G['g']=['e','f','h']
# G['h']=['g']


# print(dfs(G,'g'))
