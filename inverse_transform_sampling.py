import matplotlib.pyplot as plt
import numpy as np


def exponential_mc(alpha=1, n=100000):
  unif = np.random.uniform(size=n) 

  exp_values = -np.log(unif)/alpha

  p = 1. * np.arange(len(exp_values)) / (len(exp_values) - 1)
  data_sorted = np.sort(exp_values)

  plt.figure(figsize=(12,8))
  plt.plot(data_sorted, p)
  plt.title("Exponential distribution using inverse transform sampling")
  plt.xlabel("values")
  plt.ylabel("cdf")
  plt.show()


exponential_mc()


def pareto_mc(x0=1, alpha=1, n=100000):
  unif = np.random.uniform(low=x0, high=5, size=n) 
  pareto_values = x0/np.power((unif), (1/alpha))
  p = 1. * np.arange(len(pareto_values)) / (len(pareto_values) - 1)
  data_sorted = np.sort(pareto_values)

  plt.figure(figsize=(12,8))
  plt.plot(data_sorted, p)
  plt.title("Pareto distribution using inverse transform sampling")
  plt.xlabel("values")
  plt.ylabel("cdf")
  plt.show()


pareto_mc()
