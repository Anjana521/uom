count = 0
num = 1

while count < 10001:
    num += 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        count += 1

print(num)
