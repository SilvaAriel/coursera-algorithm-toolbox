# Uses python3
import sys

def get_fibonacci_last_digit_better(n):
    if (n <= 1):
        return n

    if n not in cache:
        cache[n] = (get_fibonacci_last_digit_better(n - 1) + 
                    get_fibonacci_last_digit_better(n - 2)) % 10
        return cache[n]
    return cache[n]

if __name__ == '__main__':
    cache = {}
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_better(n))