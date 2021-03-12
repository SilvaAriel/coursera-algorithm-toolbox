# Uses python3
import sys

def fib(n):
    if n <= 1:
        return n
    previous  = 0
    current   = 1
    sum       = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum

def pisano_period(m):
  previous, current = 0, 1
  for i in range (0, m * m):
    previous, current = current, (previous + current) % m
    if previous == 0 and current == 1:
      return i + 1

def fib_modulo(n, m):
  m_pisano = pisano_period(m)
  print(f'm_pisano: {m_pisano}')
  n_modulo_m_pisano = n % m_pisano
  print(f'n_modulo_m_pisano: {n_modulo_m_pisano}')
  new_fib = fib(n_modulo_m_pisano)
  print(f'new_fib: {new_fib}')
  return new_fib % m

if __name__ == '__main__':
    # input = sys.stdin.read();
    # n, m = map(int, input.split())

    n, m = 100, 10

    print(fib_modulo(n,m))