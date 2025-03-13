import random
 
denoms = list(range(10))
random.shuffle(denoms)
 
denoms

try:
  y = 5 / x
except ZeroDivisionError:
  print(f"Warning: denominator of 0. Returning 0 instead of infinity.")
  y = 0  