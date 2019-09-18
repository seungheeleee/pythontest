shoplist = ['apples', 'mango', 'carrot','banana']
odd = 0
for item in shoplist :
    if len(item) > 5:
        break
    print(item)

for item in shoplist:
    if len(item) % 2 == 0:
        continue
    odd = odd + 1

print(odd)