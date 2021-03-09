# Uses python3
import sys

def gcd_faster (a, b):
    if b == 0:
        return a
    a = a % b
    return gcd_faster(b, a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_faster(a, b))