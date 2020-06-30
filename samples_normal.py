import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, uniform
from scipy.interpolate import UnivariateSpline

def normal_pdf(x):
  return np.e**((-x**2)/2)/(np.sqrt(2*np.pi))

def generate_normal(n=10000):
  samples = []
  px_exponential = []
  for i in range(0, n):
    px = expon.rvs(size=1)
    unif = uniform.rvs(loc=0, scale=px, size=1)
    px_exponential.append(px[0])
    if unif <= normal_pdf(px[0]): samples.append(px[0])
  new_value = np.random.binomial(1, 0.5, len(samples))
  new_samples = []
  for i in range(0, len(samples)):
    if new_value[i] == 1: new_samples.append(-1*samples[i])
    else: new_samples.append(samples[i])
  new_exp = []
  new_value = np.random.binomial(1, 0.5, n)
  for i in range(0, n):
    if new_value[i] == 1: new_exp.append(-1*px_exponential[i])
    else: new_exp.append(px_exponential[i])
  return new_samples, new_exp


samples, exp_dist = generate_normal()
samples.sort()

plt.figure(figsize=(12,8))
p, x  = np.histogram(samples,bins=30)
x = x[:-1] + (x[1] - x[0])/2 
f = UnivariateSpline(x, p, s=30)
plt.plot(x, f(x), label="normal distribution")

p, x  = np.histogram(exp_dist,bins=30)
x = x[:-1] + (x[1] - x[0])/2 
f = UnivariateSpline(x, p, s=30)
plt.plot(x, f(x), label="exponential distribution")

plt.title("Generating samples to Normal distribution")
plt.xlabel("x")
plt.ylabel("number of samples")
plt.legend(loc="upper left")
plt.show()