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

if __name__ == '__main__':
    input = sys.stdin.read()
    b, n = map(int, input.split())
    print(fib(b, n))