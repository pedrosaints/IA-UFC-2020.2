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

pop = criaPopulacao(Tam)
# print("POPULACAO")
# print(pop)
a = calculaAptidao(pop)
# print("APTIDAO")
# print(a)
for i in range(len(pop)):
	print()
	print("ENTRADA:")
	print(pop[i])
	print()
	print("NUMERO DE COLISOES:")
	print(a[i])

print()
print()
pai1 = escolhePai(a)
print("PAI 1")
print(pop[pai1])

pai2 = escolhePai(a)
print("PAI 2")
print(pop[pai2])


