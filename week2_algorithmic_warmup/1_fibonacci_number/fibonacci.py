# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n
    
    if (n not in cache):
      cache[n] = calc_fib(n - 1) + calc_fib(n - 2)
      return cache[n]
    return cache[n]

if __name__ == '__main__':
  cache = {}
  input = sys.stdin.read()
  n = int(input)
  print(calc_fib(n))