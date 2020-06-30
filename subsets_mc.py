import numpy as np
import matplotlib.pyplot as plt
import time


def generate_one_sample(V, n, k):
	# n = total number of objects
	# k = number of objects to be selected
  for i in range(0, k):
    index = np.random.randint(low=0, high=n-i, size=1)[0]
    V[index], V[n-i-1] = V[n-i-1], V[index]
  return V[n-k:len(V)]


def generate_many_samples(n, k, M):
  total_time = 0
  V = list(range(0, n))
  for i in range(0, M):
    start = time.time()
    generate_one_sample(V, n, k)
    total_time += time.time()-start
  return total_time/M


ttime = []
n = [10**4, 10**6, 10**8]
k = [10, 10**2, 10**3, 10**4]
for i in n:
  time_k = []
  for j in k:
    time_k.append(generate_many_samples(i, j, 10**3))
  ttime.append(time_k)

plt.figure(figsize=(12,8))
for i in ttime:
    plt.plot(k, i)
plt.title("Relative error between estimation and the analytical value")
plt.xlabel("Number of samples (log10)")
plt.ylabel("Relative error (log10)")
plt.show()