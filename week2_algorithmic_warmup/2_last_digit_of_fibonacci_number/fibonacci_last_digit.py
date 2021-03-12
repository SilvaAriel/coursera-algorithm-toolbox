# Uses python3
import sys
import time

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
      previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_faster(n):
    fibonacci_number = fib(n)

    return fibonacci_number % 10

def fib(n):
    if (n <= 1):
        return n
    
    if (n not in cache):
      cache[n] = fib(n - 1) + fib(n - 2)
      return cache[n]
    return cache[n]

def get_fibonacci_last_digit_better(n):
    if (n <= 1):
        return n
    
    if (n not in cache_two):
      cache_two[n] = (fib(n - 1) + fib(n - 2)) % 10
      return cache_two[n]
    return cache_two[n]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    cache = {}
    cache_two = {}

    start_one = time.process_time_ns()
    print(get_fibonacci_last_digit_naive(200))
    elapsed_one = (time.process_time_ns() - start_one)
    print(f'Naive took: {elapsed_one}')

    start_two = time.process_time_ns()
    print(get_fibonacci_last_digit_faster(200))
    elapsed_two = (time.process_time_ns() - start_two)
    print(f'Faster took: {elapsed_two}')

    start_three = time.process_time_ns()
    print(get_fibonacci_last_digit_better(200))
    elapsed_three = (time.process_time_ns() - start_three)
    print(f'New took: {elapsed_three}')