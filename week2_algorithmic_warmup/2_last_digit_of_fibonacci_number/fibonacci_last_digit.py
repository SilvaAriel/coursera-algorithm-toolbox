# Uses python3
import sys

def fib(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
      previous, current = current, previous + current

    return current % 10

def pisano_period(m):
  previous, current = 0, 1
  for i in range (0, m * m):
    previous, current = current, (previous + current) % m
    if previous == 0 and current == 1:
      return i + 1

def fib_modulo(n):
  m_pisano = pisano_period(10)
  n_modulo_m_pisano = n % m_pisano
  new_fib = fib(n_modulo_m_pisano)
  return new_fib % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_modulo(n))