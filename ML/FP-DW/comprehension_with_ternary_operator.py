# Coversion using 'map' and 'filter' functions.
list1 = list(map(lambda x: x*2 if x%2==0 else -x, filter(lambda x: x%3!=0, range(15))))

# A more expressive way of achieving the same results.
list2 = [x*2 if x%2==0 else -x for x in range(15) if x%3!=0]

print(list1)
print(list2)