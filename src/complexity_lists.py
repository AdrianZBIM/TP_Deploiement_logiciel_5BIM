import time
import random

#-----------------------------------------------
# FONCTIONS
#-----------------------------------------------

def append_time(L, k):
	"""
	Fonction qui mesure avec la librairie time, le temps CPU requis pour effectuer un list.append(string)


	Args:
	    L: list to copy and append
	    k: nb of time to append "toto" (string) to the list L.

	Returns:
	    returns the mean time of operation time of "list.append("toto")""
	    prints the total time of operation time of k times "list.append("toto")""

	Raises:
	    KeyError: Raises an exception.
	>>> type(append_time(["1", "2"], 5))
	<class 'float'>
	"""
	clone = list(L) #fait une copie de la liste (marche comme avec les dictionnaires)


	start = time.perf_counter() # first timestamp
	for i in range(k):
		clone.append("toto")
	end = time.perf_counter() # second timestamp

	elapsed = end - start

	#print("elapsed time = {:.12f} seconds".format(elapsed))
	return elapsed / k
	#print(clone)
	#print(L)

def inserthead_time(l, k):
	"""
	Fonction qui mesure avec la librairie time, le temps CPU requis pour effectuer un list.insert(string)


	Args:
	    L: list to copy and insert
	    k: nb of time to insert "toto" (string) to the list L.

	Returns:
	    returns the mean time of operation time of "list.insert("toto")""
	    prints the total time of operation time of k times "list.insert("toto")""

	Raises:
	    KeyError: Raises an exception.

	"""
	clone = list(l)
	start = time.perf_counter()
	for i in range(k):
		clone.insert(0, "toto")

	end = time.perf_counter() # second timestamp

	elapsed = end - start

	#print("elapsed time = {:.12f} seconds".format(elapsed))
	return elapsed / k

def access_time(l,k):
	"""
	Fonction qui mesure avec la librairie time, le temps CPU requis pour accéder à un élément random d'une liste.


	Args:
	    L: list to copy and to access
	    k: nb of time to access random elements (string) to the list L.

	Returns:
	    returns the mean time of operation time of accessing random elements of the list L
	    prints the total time of operation time of accessing random elements of the list L

	Raises:
	    KeyError: Raises an exception.

	"""
	clone = list(l)

	start = time.perf_counter()

	for i in range(k):
		clone[random.randrange(0, len(l)-1)]

	end = time.perf_counter() # second timestamp


	elapsed = end - start

	#print("elapsed time = {:.12f} seconds".format(elapsed))
	return elapsed / k

	"""
	def access_time(l,k):
		clone = list(l)
		my_r = [random.randrange(0, len(l)) for _ in range(k)]
		start = time.perf_counter()
		for i in my_r:
			z = clone[i]
		end = time.perf_counter() # second timestamp

		elapsed = end - start

		print("elapsed time = {:.12f} seconds".format(elapsed))
		return elapsed / k
	"""

def create_big_list_from_file(fname,enc):
	"""
	Fonction qui à partir d'un fichier fname, et un encodage enc; ajoute à la liste "sortie" chaque mot du fichier fname




	Args:
	    fname: string filename ex "words.txt"
	    enc: string encoding type ex "utf-8"
	Returns:
	    returns the biglist of words present in fname

	Raises:
	    KeyError: Raises an exception.

	"""
	sortie = []
	with open(fname, "r", 1024, encoding= enc) as fop:
		for line in fop:
			sortie.append(line)



	return sortie







