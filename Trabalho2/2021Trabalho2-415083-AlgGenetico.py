import numpy as np

# TAMANHO TABULEIRO
n = 40
# TAMANHO POPULAÇÃO
Tam = 1000
# TAXA MUTAÇÃO (10 = 10%)
Tmut = 10
# NUMERO MAX DE ITERACAO
IT = 50000


def verificaConflito(A):
	cont = 0
	for i in range(n):
		#verifica linha nao precisa, entradas ja nao tem essas colisoes
		#verifica coluna
		for k in range(n):
			if k != i:
				if A[k] == A[i]:
					cont+=1
		#verifica diagonais
		for k in range(n):
			# print(k)
			if k != i:
				if abs(A[k] - A[i]) == abs(k-i):
					cont+=1
	return cont

def produzElemento():
	A = np.arange(n)
	np.random.shuffle(A)
	return A

def criaPopulacao(tamanho):
	p = []
	for i in range(tamanho):
		p.append(produzElemento())
	return p

def calculaAptidao(P):
	a = []
	for elem in P:
		# print()
		# print("ENTRADA:")
		# print(elem)
		# print()
		# print("NUMERO DE COLISOES:")
		apt = verificaConflito(elem)
		# print(apt)
		a.append(apt)
	return a

def escolhePai(A,pai1 = -1):
	# print(A)
	Roleta = np.copy(A)
	s = np.cumsum(a)
	# print("ROLETA prob normal")
	# print(s)
	total = s[Tam - 1]
	# invertendo prob
	for i in range(Tam):
		# SE FOR SOLUCAO RETORNA SEMPRE ESSE ELEM
		if A[i] == 0 and i != pai1:
			return i
		if A[i] == 0:
			Roleta[i] = 0
		else:
			Roleta[i] = total/A[i]
	s = np.cumsum(Roleta)
	# print("ROLETA c/ PROB INVERTIDA")
	# print("ROLETA")
	# print(s)
	total = s[Tam - 1]
	pai = np.random.randint(total)
	# print("NUMERO SORTEADO")
	# print(pai)
	for i in range(Tam):
		if pai < s[i]:
			return i

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
	ipai2 = escolhePai(a,ipai1)
	while ipai1 == ipai2:
		ipai2 = escolhePai(a)
	pai1 = pop[ipai1]
	pai2 = pop[ipai2]
	filho1 = np.copy(pai1)
	filho2 = np.copy(pai2)
	# print("PAI 1")
	# print(pai1)
	# print()
	# print("PAI 2")
	# print(pai2)
	# print()
	corte = np.random.randint(n)
	# print(corte)
	# print()
	# CORTE
	for i in range(n):
		if i < corte:
			filho1[i] = pai2[i]
			filho2[i] = pai1[i]

	# MUTACAO
	# P/ FILHO 1
	mut = np.random.randint(100)
	# print()
	# print(mut)
	# print()
	if mut < Tmut:
		iAleat = np.random.randint(n)
		# print(iAleat)
		numAleat = np.random.randint(n)
		# print(numAleat)
		filho1[iAleat] = numAleat
		# print()
	# P/ FILHO 2
	mut = np.random.randint(100)
	# print()
	# print(mut)
	# print()
	if mut < Tmut:
		iAleat = np.random.randint(n)
		# print(iAleat)
		numAleat = np.random.randint(n)
		# print(numAleat)
		filho2[iAleat] = numAleat
		# print()

	# print("FILHO 1")
	# print(filho1)
	# print()
	# print("FILHO 2")
	# print(filho2)

	# PELO ALGORITMO DA AULA RETIRO OS PAIS E COLOCO OS FILHOS
	# MAS VOU ESCOLHER OS 2 MELHORES DOS 4 PARA UM ELITISMO BASICO
	paiefilhos = [pai1,pai2,filho1,filho2]
	apt = calculaAptidao(paiefilhos)
	# print()
	# print(apt)
	# print()
	melhor1, melhor2 = selecionaMelhores(apt)
	# print(melhor1)
	# print(melhor2)
	pop[ipai1]=paiefilhos[melhor1]
	a[ipai1]=apt[melhor1]
	pop[ipai2] = paiefilhos[melhor2]
	a[ipai2] = apt[melhor2]
	return pop,a

def aGMain(pop,a):
	for i in range(IT):
		if i%1000 == 0:
			print(i)
		pop,a = cruzamento(pop,a)
	return pop,a

def printTabuleiro(T):
	tab11 = ""
	for i in range(n):
		tab11 += " ---"
	print(tab11)
	for i in range(n):
		tab1 = ""
		tab2 = "|"
		for j in range(n):
			tab1 += " ---"
			tab2 += " "
			if j == T[i]:
				tab2 += "R"
			else:
				tab2 += " "
			tab2 += " |"
		print(tab2)
		print(tab1)

pop = criaPopulacao(Tam)
print("POPULACAO INCIAL")
# print(pop)
a = calculaAptidao(pop)
print("APTIDAO INICIAL")
print(a)
print("MEDIA")
print(np.median(a))

print()
print()

popf,af = aGMain(pop,a)
print("POPULACAO FINAL")
# print(popf)
print("APTIDAO FINAL")
print(af)
print("MEDIA")
print(np.median(a))
print()
imelhor1, imelhor2 = selecionaMelhores(a)
print()
melhor1 = pop[imelhor1]
melhor2 = pop[imelhor2]
print("MELHORES ELEMENTOS:")
print()
print("ELEMENTO:")
print(melhor1)
print("NUMERO DE COLISOES:")
print(a[imelhor1])
printTabuleiro(melhor1)
print()
print("ELEMENTO:")
print(melhor2)
print("NUMERO DE COLISOES:")
print(a[imelhor2])
printTabuleiro(melhor2)
print()

