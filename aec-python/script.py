x = 2
print(x)

my_first_list = ['apple', 1, 'banana', 2]
my_fruit_list = ['apple', 'banana']
my_int_list = [1,2,3]



cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for f in my_fruit_list:
  print(f)

for f in my_fruit_list:
  pass
print(f)

def sq_int(x):
  y = x**2
  return y

sq_int(5)

sq_int(3)

sq_int(94)

y = 4

sq_int(y)

def is_even(n):
    return n % 2 == 0  

def is_odd(n):
    return n % 2 != 0  

def describe_evenness(x):
    if is_even(x):
        print("It’s even!")
    elif is_odd(x):
        print("It’s odd!")
    else:
        print("It’s neither even nor odd!")

x = 4
y = 5

describe_evenness(x)  
describe_evenness(y)  


i = 0
while i < len(my_fruit_list):  
    print(my_fruit_list[i])  
    i += 1  

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for key in cal_lookup:  
    print(cal_lookup[key])

for item in my_first_list:
    if isinstance(item, int):  
        print(f"{item} squared is {item ** 2}")
    elif isinstance(item, str) and item in cal_lookup:  
        print(f"The calorie content of {item} is {cal_lookup[item]}")


def verarbeite_dict(input_dict):
    pass
verarbeite_dict({'apple': 95, 'banana': 105})

def verarbeite_dict(input_dict):
    for key in input_dict:
        value = input_dict[key]
        print(f"Der Wert für {key} ist {value}, und das Quadrat davon ist {value ** 2}")

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}
verarbeite_dict(cal_lookup)

i = 1
while i < 6:
  print(i)
  i += 1

  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


import random
 
denoms = list(range(10))
random.shuffle(denoms)
 
denoms

for i in range(10):
  x = denoms[i]
  result = 100 / x