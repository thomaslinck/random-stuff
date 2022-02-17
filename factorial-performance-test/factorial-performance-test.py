from functools import reduce 
import time 
import doctest 

def recursive_factorial(n): 
  """Recursive implementation of a factorial: 
  >>> recursive_factorial(10)
  3628800
  """
  def _recursive_factorial(v, n): 
    return v if n == 1 else _recursive_factorial(v * n , n-1)

  return _recursive_factorial(1, n)

def reduce_factorial(n): 
  """Functional (reduce) implementation of a factorial: 
  >>> reduce_factorial(10)
  3628800
  """
  return reduce(lambda a,b: a*b, list(range(1,n+1)))

def iterative_factorial(n): 
  """Iterative implementation of a factorial: 
  >>> iterative_factorial(10)
  3628800
  """
  result = 1 
  for v in range(1,n): 
    result *= v + 1 
  return result 

functions = { 
  "Recursive": recursive_factorial, 
  "Iterative": iterative_factorial, 
  "Reduce": reduce_factorial
}

def all_functions(): 
  n = 700 #greater n generate stack overflow in the recursive function  
  print('Testing for n = ' + str(n))

  for k,v in functions.items(): 
    s = time.perf_counter()
    r = v(n)
    e = time.perf_counter()

    print(k + ' = ' + str(e-s))

def excluding_functional():
  n = 10000 
  print('Testing for n = ' + str(n))

  for k,v in functions.items(): 
    if k == "Recursive": 
      continue 

    s = time.perf_counter()
    r = v(n)
    e = time.perf_counter()

    print(k + ' = ' + str(e-s))

all_functions() 
excluding_functional()

if __name__ == "__main__":
    doctest.testmod()