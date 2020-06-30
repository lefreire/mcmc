import string
import requests
import numpy as np
import matplotlib.pyplot as plt


alfabeto = list(string.ascii_lowercase)


def generate_doms(n, k=4):
  doms = []
  for i in range(0, n):
    len_dom = np.random.randint(low=1, high=k+1, size=1)[0]
    index = np.random.randint(low=0, high=len(alfabeto), size=len_dom)
    doms.append("".join([alfabeto[j] for j in index]))
  return doms


def test_dom(name):
  try:
    request = requests.get('http://www.'+name+'.ufrj.br', verify=False)
  except requests.ConnectionError:
    return False
  if request.status_code == 200:
    return True


def count_valid_doms(n, k):
  doms = generate_doms(n, k)
  valid_doms = []
  invalid_doms = []
  for dom in doms:
    if test_dom(dom): valid_doms.append(dom)
    else: invalid_doms.append(dom)
  return valid_doms, invalid_doms


  n = np.arange(1, 10**4, 1000)
  all_valid = []
  for num_total in n:
    v, i = count_valid_doms(num_total, 4)
    all_valid.append(len(v))

  plt.figure(figsize=(12,8))
  plt.plot(n, all_valid)
  plt.title("Valid Web domains")
  plt.xlabel("Total number of generated domains")
  plt.ylabel("Total number of valid domains")
  plt.show()