import numpy as np
import matplotlib.pyplot as plt


def generate_probs(n):
  values = np.arange(1, n+1)
  ssum = (n*(n+1))/2
  return values/ssum


def func_h(x, n):
  ssum = (n*(n+1))/2
  return x/ssum


def func_g(x):
  return x*np.log(x)


def exact_value(n):
  ssum = 0
  for i in range(1, n+1):
    ssum += i*np.log(i)
  return ssum


def generate_gn(n=10**6):
  S = 0
  for i in range(1, n+1):
    probs = generate_probs(n)
    sample = np.random.choice(np.arange(1, n+1), p=probs)
    S += func_g(sample)/func_h(sample, n)
  return S/n

n = np.arange(1, 10**6, 100000)
estimate_gn = []
for i in n:
  ex_value = exact_value(i)
  estimate_gn.append((abs(generate_gn(i)-ex_value))/ex_value)

plt.figure(figsize=(12,8))
plt.plot(n, estimate_gn)
plt.title("Relative error between Gn and the exact value of the sum")
plt.xlabel("Number of samples")
plt.ylabel("Relative error")
plt.show()