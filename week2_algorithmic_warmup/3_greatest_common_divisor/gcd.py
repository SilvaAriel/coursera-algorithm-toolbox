# Uses python3
import sys
import time

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_faster (a, b):
  if b == 0:
    return a
  a = a % b
  return gcd_faster(b, a)

if __name__ == "__main__":
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    # print(gcd_naive(a, b))

    a = 8
    b = 6

    start_naive = time.process_time_ns()
    print(gcd_naive(a, b))
    elapsed_naive = (time.process_time_ns() - start_naive)
    print(f'Elapsed naive: {elapsed_naive}')

    start_faster = time.process_time_ns()
    print(gcd_faster(a, b))
    elapsed_faster = (time.process_time_ns() - start_faster)
    print(f'Elapsed faster: {elapsed_faster}')