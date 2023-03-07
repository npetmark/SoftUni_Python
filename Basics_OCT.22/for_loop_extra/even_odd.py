import sys

iterations = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, iterations + 1):
    number = float(input())

    if i % 2 == 0:
        even_sum += number
        
        if number < even_min:
            even_min = number

        if number > even_max:
            even_max = number
    
    else:
        odd_sum += number

        if number < odd_min:
            odd_min = number
        
        if number > odd_max:
            odd_max = number

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f}," if odd_min != sys.maxsize else "OddMin=No,")
print(f"OddMax={odd_max:.2f}," if odd_max != -sys.maxsize else "OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f}," if even_min != sys.maxsize else "EvenMin=No,")
print(f"EvenMax={even_max:.2f}" if even_max != -sys.maxsize else "EvenMax=No")