#python3
import random
import time

def max_pairwise_product_faster(numbers):
    n = len(numbers)
    biggest = 0
    second_biggest = 0
    for i in range (n):
        if numbers[i] > biggest:
            if biggest > second_biggest:
                second_biggest = biggest
            biggest = numbers[i]
        else:
            if numbers[i] > second_biggest:
                second_biggest = numbers[i]
    return biggest * second_biggest

if __name__ == '__main__':

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    product = max_pairwise_product_faster(input_numbers)
    print(product)

# ----------------------------------------------------------------------------------------------
# #python3
# import random
# import time

# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])

#     return max_product

# def max_pairwise_product_faster(numbers):
#     n = len(numbers)
#     biggest = 0
#     second_biggest = 0
#     for number in range (n):
#         if number > biggest:
#             if biggest > second_biggest:
#                 second_biggest = biggest
#             biggest = number
#         else:
#             if number > second_biggest:
#                 second_biggest = number
#     return biggest * second_biggest

# if __name__ == '__main__':

#     print("Python --------------------------------------")
#     while(True):
#         n = random.randint(1,10000)
#         values = [int(num) for num in range(n)]

#         if(len(values) < 8000):
#             continue

#         print(f'Total values: {len(values)}')

#         start_common = time.process_time_ns()
#         max_common_return = max_pairwise_product(values)
#         elapsed_common = (time.process_time_ns() - start_common)
#         print("Max Common took: %.2f" % elapsed_common)

#         start_faster = time.process_time_ns()
#         max_faster_return = max_pairwise_product_faster(values)
#         elapsed_fast = (time.process_time_ns() - start_faster)
#         print("Max Faster took: %.2f" % elapsed_fast)

#         print("Max faster is %.1f faster than Max Common" % (elapsed_common/elapsed_fast))

#         print("---------------------")

#         if max_common_return != max_faster_return:
#             print(f'Max Diff Common: {max_common_return}')
#             print(f'Max Diff Faster: {max_faster_return}')
#             break



#     input_n = int(input())
#     input_numbers = [int(x) for x in input().split()]
#     print(max_pairwise_product(input_numbers))

