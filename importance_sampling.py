import numpy as np
import matplotlib.pyplot as plt


def generate_probs():
  n = 10**6
  values = np.arange(1, n+1)
  ssum = (n*(n+1))/2
  return values/ssum


def func_h(x):
  n = 10**6
  ssum = (n*(n+1))/2
  return x/ssum


def func_g(x):
  return x*np.log(x)


def exact_value(n):
  ssum = 0
  for i in range(1, n+1):
    ssum += i*np.log(i)
  return ssum


def generate_gn(n, probs, values):
  S = 0
  samples = np.random.choice(values, size=n, p=probs)
  S+=sum(func_g(samples)/func_h(samples))
  return S/n

n = np.linspace(1, 10**7, 1000, dtype=np.int32)
estimate_gn = []
probs = generate_probs()
values = np.arange(1, 10**6+1)
ex_value = exact_value(10**6)
for i in n:
  estimate_gn.append((abs(generate_gn(i, probs, values)-ex_value))/ex_value)

plt.figure(figsize=(12,8))
plt.plot(np.log(n),np.log(estimate_gn))
plt.title("Relative error between Gn and the exact value of the sum")
plt.xlabel("Number of samples")
plt.ylabel("Relative error")
plt.show()