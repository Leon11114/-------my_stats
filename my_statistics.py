def my_max(p):
  p.sort()
  return p[-1]

def my_min(p):
  p.sort()
  return p[0]

def my_mean(p):
  return sum(p)/len(p)

def my_median(p):
  p.sort()
  n = len(p)
  ind = n//2
  if n%2 != 0:
    return p[ind]
  else:
    return (p[ind-1] + p[ind])/2
  
def my_mode(p):
  import statistics as st
  try:
    return st.mode(p)
  except:
    return "Нет однозначной моды"

def quantil(p):
  import pandas as pd
  df = pd.Series(p)
  qwanta = df.quantile([.25, .5, .75])
  z = []
  for i in qwanta:
    z.append(i)
  return z

def my_square(p):
  s = 0
  for i in p:
    s+= (i - my_mean(p))**2
  return round(s/(len(p)-1)**0.5,2)

def simmetric(p):
  raznost = abs(my_median(p) - my_mean(p))
  if raznost <= 3 * ((my_square(p)/len(p))**0.5):
    return True
  else:
    return False

def quantil_raz(p):
  q = quantil(p)
  s = []
  for i in p:
    if i>q[0] and i < q[2]:
      s.append(i)
  return s

def delete():
  print("don't delete pls")