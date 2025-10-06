list1=[]
list2=[]
for num1 in range(1000):
    for num2 in range(1000):
        product = num1 * num2
        if str(product) == str(product)[::-1]:
            list1.append(product)
            list2.append((num1,num2))
print(max(list1))
print(list2[list1.index(max(list1))])

