# Uses python3
import sys

def fib(b, n):

    previous = 0
    current = 1
    sum = 0
    for i in range(n):
        if i >= b - 1:
          sum += current
        previous, current = current, previous + current
    return sum % 10

def pisano_period(m):
  previous, current = 0, 1
  for i in range (0, m * m):
    previous, current = current, (previous + current) % m
    if previous == 0 and current == 1:
      return i + 1

def fib_modulo(b, n):
  m_pisano = pisano_period(10)
  n_modulo_m_pisano = n % m_pisano
  new_fib = fib(b, n_modulo_m_pisano)
  return new_fib % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    b, n = map(int, input.split())
    print(fib_modulo(b, n))