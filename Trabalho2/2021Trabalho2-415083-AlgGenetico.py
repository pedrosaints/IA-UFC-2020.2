import numpy as np

n = 4
Tam = 10


def verificaConflito(A):
	cont = 0
	for i in range(n):
		for j in range(n):
			if A[i][j] == 1:
				#verifica linha
				for k in range(n):
					if k != j:
						if A[i][k] == 1:
							cont+=1
				#verifica coluna
				for k in range(n):
					if k != i:
						if A[k][j] == 1:
							cont+=1
				#verifica diagonais
				for k in range(1,n-i):
					if j+k < n and i+k < n:
						if A[i+k][j+k] == 1:
							cont+=1				
				for k in range(1,i+1):
					if j-k > -1 and i-k > -1:
						if A[i-k][j-k] == 1:
							cont+=1	
				for k in range(1,i+1):
					if i-k > -1and j+k < n:
						if A[i-k][j+k] == 1:
							cont+=1
				for k in range(1,n-i):
					if j-k > -1and i+k < n:
						if A[i+k][j-k] == 1:
							cont+=1
	return cont

def produzElemento():
	A = np.array((1, 1, 1, 1
				  , 0, 0, 0, 0
				  , 0, 0, 0, 0
				  , 0, 0, 0, 0))
	np.random.shuffle(A)
	A = A.reshape((n, n))
	return A

def criaPopulacao(tamanho):
	p = []
	for i in range(tamanho):
		p.append(produzElemento())
	return p

def calculaAptidao(P):
	a = []
	for elem in P:
		print()
		print("ENTRADA:")
		print(elem)
		print()
		print("NUMERO DE COLISOES:")
		a.append(verificaConflito(elem))
	return a

def escolhePai(A):
	# print(A)
	Roleta = np.copy(A)
	s = np.cumsum(a)
	# print("ROLETA prob normal")
	# print(s)
	total = s[Tam - 1]
	# invertendo prob
	for i in range(Tam):
		Roleta[i] = total/A[i]
	s = np.cumsum(Roleta)
	# print("ROLETA c/ PROB INVERTIDA")
	print("ROLETA")
	print(s)
	total = s[Tam - 1]
	pai = np.random.randint(total)
	print("NUMERO SORTEADO")
	print(pai)
	for i in range(Tam):
		if pai < s[i]:
			return i

def localizaRainhas(T):
	L = []
	for i in range(n):
		for j in range(n):
			if T[i][j] == 1:
				L.append((i,j))
	return L

def produzFilho(loc):
	F = np.zeros((n,n))
	for k in range(n):
		i,j = loc[k]
		F[i][j] = 1
	return F

def selecionaMelhores(a):
	melhor1 = 0
	if a[1] < a[melhor1]:
		melhor1 = 1
		melhor2 = 0
	else:
		melhor2 = 1
	for i in range(2,len(a)):
		if a[i]<a[melhor1]:
			melhor2 = melhor1
			melhor1 = i
		elif a[i]<a[melhor2]:
			melhor2 = i
	return melhor1,melhor2

def cruzamento(pop,a):
	ipai1 = escolhePai(a)
	ipai2 = escolhePai(a)
	while ipai1 == ipai2:
		pai2 = escolhePai(a)
	pai1 = pop[ipai1]
	pai2 = pop[ipai2]
	loc1 = localizaRainhas(pai1)
	loc2 = localizaRainhas(pai2)
	print("PAI 1")
	print(pai1)
	print()
	print("PAI 2")
	print(pai2)
	print()
	corte = np.random.randint(n)
	print(corte)
	print()
	# CORTE - ERRO - NEM SEMPRE FICA COM N RAINHAS
	locaux = np.copy(loc1)
	for i in range(n):
		if i < corte:
			loc1[i] = loc2[i]
			loc2[i] = locaux[i]

	# MUTACAO AQUI
	# TO DO

	print("FILHO 1")
	filho1 = produzFilho(loc1)
	print(filho1)
	print()
	print("FILHO 2")
	filho2 = produzFilho(loc2)
	print(filho2)

	# PELO ALGORITMO DA AULA RETIRO OS PAIS E COLOCO OS FILHOS
	# MAS VOU ESCOLHER OS 2 MELHORES DOS 4 PARA UM ELITISMO BASICO
	paiefilhos = [pai1,pai2,filho1,filho2]
	apt = calculaAptidao(paiefilhos)
	print()
	print(apt)
	print()
	melhor1, melhor2 = selecionaMelhores(apt)
	print(melhor1)
	print(melhor2)
	pop[ipai1]=paiefilhos[melhor1]
	a[ipai1]=apt[melhor1]
	pop[ipai2] = paiefilhos[melhor2]
	a[ipai2] = apt[melhor2]
	return pop,a



pop = criaPopulacao(Tam)
print("POPULACAO")
print(pop)
a = calculaAptidao(pop)
print("APTIDAO")
print(a)
for i in range(len(pop)):
	print()
	print("ENTRADA:")
	print(pop[i])
	print()
	print("NUMERO DE COLISOES:")
	print(a[i])

print()
print()

pop,a = cruzamento(pop,a)
# print()
# for i in range(len(pop)):
# 	print()
# 	print("ENTRADA:")
# 	print(pop[i])
# 	print()
# 	print("NUMERO DE COLISOES:")
# 	print(a[i])
