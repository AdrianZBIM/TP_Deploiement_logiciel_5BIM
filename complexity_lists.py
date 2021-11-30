import time
import random

#-----------------------------------------------
# FONCTIONS
#-----------------------------------------------

def append_time(L, k):
	clone = list(L) #fait une copie de la liste (marche comme avec les dictionnaires)


	start = time.perf_counter() # first timestamp
	for i in range(k):
		clone.append("toto")
	end = time.perf_counter() # second timestamp

	elapsed = end - start

	print("elapsed time = {:.12f} seconds".format(elapsed))
	return elapsed / k
	#print(clone)
	#print(L)

def inserthead_time(l, k):
	clone = list(l)
	start = time.perf_counter()
	for i in range(k):
		clone.insert(0, "toto")

	end = time.perf_counter() # second timestamp

	elapsed = end - start

	print("elapsed time = {:.12f} seconds".format(elapsed))
	return elapsed / k

def access_time(l,k):
	clone = list(l)

	start = time.perf_counter()

	for i in range(k):
		clone[random.randrange(0, len(l)-1)]

	end = time.perf_counter() # second timestamp


	elapsed = end - start

	print("elapsed time = {:.12f} seconds".format(elapsed))
	return elapsed / k

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

def create_big_list_from_file(fname,enc):
	sortie = []
	with open(fname, "r", 1024, encoding= enc) as fop:
		for line in fop:
			sortie.append(line)



	return sortie




#-----------------------------------------------
# MAIN
#-----------------------------------------------
k=500

print("temps moyen append : "+str(append_time([1,2,"toto"], k))+"\n")
print("temps moyen insert : "+str(inserthead_time([1,2,"toto"], k))+"\n")
print("temps moyen access : "+str(access_time([1,2,"toto"], k))+"\n")

print(create_big_list_from_file("words.txt", "utf-8"))
big_list = create_big_list_from_file("words.txt","utf-8")
with open("truc.txt", "w+", 1024, encoding="utf-8") as f:

	for i in range (1000,201000,1000):
		sublist = big_list[0:i]
		appendtime = append_time(sublist, 200)
		instime = inserthead_time(sublist, 200)
		f.write("{0:16}".format(str(i)) + "{0:28}".format(str(appendtime))+ "{0:28}".format(str(instime))+"\n")





