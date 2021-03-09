# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n
    
    if (n not in cache):
      cache[n] = calc_fib(n - 1) + calc_fib(n - 2)
      return cache[n]
    return cache[n]

cache = {}
n = int(input())
print(calc_fib(n))