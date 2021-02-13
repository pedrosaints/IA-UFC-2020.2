import numpy as np

n = 4



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

pop = criaPopulacao(10)
a = calculaAptidao(pop)
for i in range(len(pop)):
	print()
	print("ENTRADA:")
	print(pop[i])
	print()
	print("NUMERO DE COLISOES:")
	print(a[i])


