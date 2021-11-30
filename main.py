import src.complexity_lists as cmp_l





#-----------------------------------------------
# MAIN
#-----------------------------------------------
k=500

print("temps moyen append : "+str(cmp_l.append_time([1,2,"toto"], k))+"\n")
print("temps moyen insert : "+str(cmp_l.inserthead_time([1,2,"toto"], k))+"\n")
print("temps moyen access : "+str(cmp_l.access_time([1,2,"toto"], k))+"\n")

#print(cmp_l.create_big_list_from_file("src/words.txt", "utf-8"))
big_list = cmp_l.create_big_list_from_file("src/words.txt","utf-8")
k = 200
with open("truc.txt", "w+", 1024, encoding="utf-8") as f:

	for i in range (1000,201000,1000):
		sublist = big_list[0:i]
		appendtime = cmp_l.append_time(sublist, k)
		instime = cmp_l.inserthead_time(sublist, k)
		f.write("{0:16}".format(str(i)) + "{0:28}".format(str(appendtime))+ "{0:28}".format(str(instime))+"\n")


import doctest
doctest.testmod(cmp_l, verbose=True)
