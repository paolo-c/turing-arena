# evaluation_assert data["goals"]["correct"]

# Funzione ricorsiva chiamata dalla funzione lists_checkouts(N)
#
# N e' il numero del quale si vuole calcolare il numero di checkouts
# depth rapressenta il numero di freccette coinvolte
# current e' il checkout che sta calcolando in quel momento
# current e' una lista di string, ogni elemento e' del tipo
# Sx, Dx, o Tx  dove S sta per Single, D per Double e T per Triple
# mentre x e' lo spicchio centrato dalla freccetta 
def lists(N,depth,current):

	result=[]

	#se N<0 o tutte le freccette sono gia' state utilizzate
	# non esiste alcun checkout con N
	if N<0 or depth==3:
		return []
		
	#Avvio la ricorsione nel caso in cui la freccetta prenda un triplo
	for i in range(1,min(int(N/3)+1,21)):
		if i*3==N:
			result+=[["T "+str(i)]+current]
		else:
			result+=lists(N-i*3,depth+1,["T "+str(i)]+current)

	
	#Avvio la ricorsione nel caso in cui la freccetta prenda un doppio
	#qua e' necessario aggiungere il bull con un if dedicato
	Range=list(range(1,min(int(N/2)+1,21)))
	if N>=50:
		Range+=[25]
	for i in Range: 
		if i*2==N:
			result+=[["D "+str(i)]+current]
		else:
			result+=lists(N-i*2,depth+1,["D "+str(i)]+current)


	#Avvio la ricorsione nel caso in cui la freccetta prenda un singolo
	#qua e' necessario aggiungere il bull con un if dedicato
	Range=list(range(1,min(int(N)+1,21)))
	if N>=25:
		Range+=[25]
	for i in Range:
		if i==N:
			result+=[["S "+str(i)]+current]
		else:
			result+=lists(N-i,depth+1,["S "+str(i)]+current)
		
	return result
	


#funzione chiamata da lists_checkouts
#Ritorna true se i due checkouts di input, hanno lo stesso doppio finale
# e differiscono solo per l'ordine delle prime due freccette 
def is_equal(a,b):
	if len(a)!=3 or len(b)!=3:
		return False
	
	if a[2]==b[2] and a[0]==b[1] and a[1]==b[0]:
		return True
	return False


#ritorna la lista di tutti i possibili checkouts per N
def lists_checkouts(N):
	result=[]

	#nel caso in cui N sia almeno 50, anche il bull e' utilizzabile
	Range=list(range(1,min(int(N/2)+1,21)))
	if N>=50:
		Range+=[25]

	#avvio la ricerca, l'ultima freccetta e' necessariamente un doppio
	for i in Range:
		if i*2==N:
			result=[["D "+str(i)]]+result
		else:
			result=lists(N-i*2,1,["D "+str(i)])+result
			

	#elimino i checkouts doppioni
	i=0
	while i<len(result)-1:
		a=result[i]
		for b in result[i+1:]:
			if is_equal(a,b):
				result.pop(i)		
				i-=1
		i+=1
	return result


# funzione richiesta da interface.txt
def count_checkouts(N):
	return len(lists_checkouts(N))


def print_checkouts(N):
	res=lists_checkouts(N)
	print(f"There are {len(res)} checkouts for {N}")
	for i in res:
		print(i)
	return


#Solution to problem 109 of project Euler
def solution_pEuler():
	tot=0
	for i in range(1,100):
		print("Computing ",i)
		tot+=count_checkouts(i)
	return tot
