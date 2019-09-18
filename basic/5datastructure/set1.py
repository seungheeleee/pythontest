set1 = {2, 1, 3, 'one', 'two'}
set2 = {2, 3, 'three'}



print(set1)
set1.add('three')
print(set1)
set1.remove(2)
print (set1)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))