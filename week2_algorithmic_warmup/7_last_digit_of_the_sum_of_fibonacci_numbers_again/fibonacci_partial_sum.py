# Uses python3
import sys

def fib_mod_10(n):
    if (n <= 1):
        return n
    
    if (n not in cache):
      cache[n] = fib_mod_10(n - 1) + fib_mod_10(n - 2)
      return cache[n]
    return cache[n]

def last_digit_sum_fibonacci(b, n):
  b = b % 60
  n = b + (n - b) % 60
  sum = 0
  for i in range (b, n + 1):
    sum += fib_mod_10(i)
  return sum % 10

if __name__ == '__main__':
    cache = {}
    input = sys.stdin.read()
    b, n = map(int, input.split())
    print(last_digit_sum_fibonacci(b, n))