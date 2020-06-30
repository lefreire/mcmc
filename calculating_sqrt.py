import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


def func_curve(x, y):
  '''
  This function tests with the point (x, y) is inside the curve
  '''
  return 2-x**2 - y >= 0

def generate_points(n):
  x = np.random.uniform(low=0, high=2, size=n)
  y = np.random.uniform(low=0, high=2, size=n)

  inside_curve_x = []
  inside_curve_y = []
  outside_curve_x = []
  outside_curve_y = []

  for i in range(0, n):
    if func_curve(x[i], y[i]):
      inside_curve_x.append(x[i])
      inside_curve_y.append(y[i])
    else:
      outside_curve_x.append(x[i])
      outside_curve_y.append(y[i])
  return inside_curve_x, inside_curve_y, outside_curve_x, outside_curve_y

def estimate_sqrt2(n):
  in_x, _, _, _ = generate_points(n)
  return 3*len(in_x)/n


in_x, in_y, out_x, out_y = generate_points(10**6)

plt.figure(figsize=(12,8))
plt.plot(in_x, in_y, "+", color='pink')
plt.plot(out_x, out_y, "bo", color='green')
plt.title("Square with curve inside")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

n = np.arange(1, 10**6, 1000)
estimate_sqrt = []
for i in n:
  estimate_sqrt.append((abs(estimate_sqrt2(i)-np.sqrt(2)))/np.sqrt(2))

plt.figure(figsize=(12,8))
plt.plot(np.log10(n), np.log10(estimate_sqrt))
plt.title("Relative error between estimation and the square root of 2")
plt.xlabel("Number of samples (log10)")
plt.ylabel("Relative error with 2^(1/2) (log10)")
plt.show()