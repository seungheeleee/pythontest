months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May'}
print(months)
print(months[2])
months['June'] = 6
months[5] = '5월'
print(months)
del months[1]
print(months)
if 5 in months:
    print(months[5])