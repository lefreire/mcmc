import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.integrate as integrate


def integration_mc(alpha, a, b, n=100000):
	#between a and b
	unif = np.random.uniform(low=a, high=b, size=n)

	sum_func_exp = 0
	for var in unif:
		sum_func_exp += var**alpha

	expected_value = sum_func_exp/n

	func_value = expected_value*(b-a)

	return func_value


def calculate_func(x, alpha):
  return x**alpha


def calculate_integral(alpha, a, b):
  return integrate.quad(calculate_func, a, b, args=(alpha))[0]


alphas = [1,2,3]
a = 0
bs = [1,2,4]
n = np.arange(1, 10**6, 10000)
all_errors = []

for alpha in alphas:
for b in bs:
  errors = []
  g = calculate_integral(alpha, a, b)
  for i in n:
    g_hat = integration_mc(alpha, a, b, i)
    errors.append((abs(g_hat - g))/g)
  all_errors.append(errors)

plt.figure(figsize=(12,8))
for i in all_errors:
  plt.plot(np.log10(n), np.log10(i))
plt.title("Relative error between estimation and the analytical value")
plt.xlabel("Number of samples (log10)")
plt.ylabel("Relative error (log10)")
plt.show()
