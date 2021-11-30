import time

start = time.perf_counter() # first timestamp

# we place here the code we want to time
y = 2**0.5

end = time.perf_counter() # second timestamp

elapsed = end - start
print("elapsed time = {:.12f} seconds".format(elapsed))


