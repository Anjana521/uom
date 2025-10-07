import itertools

for i in itertools.count(1):
    for j in range(1,21):
        if i % j != 0:
            break

    else:
        if j == 20:
            print(i)
            exit()    
            