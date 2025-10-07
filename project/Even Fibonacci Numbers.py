def fib(val):
    list1 = [1,2]
    
    while list1[-1] < val:
        new_val = list1[-1] + list1[-2]
        list1.append(new_val)
    list1.pop()
    return list1

    
fib_seq = fib(4000000)
even_sum = 0
for i in fib_seq:
    if i % 2 == 0:
        even_sum += i   
print(even_sum)

