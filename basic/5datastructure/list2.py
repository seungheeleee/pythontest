squares = [1, 4, 9, 16, [25, 36]]
print(squares[:2])
print(squares[::2])
print(squares)
squares[2] = 81
print(squares)
squares[:2] = [49, 64]
print(squares)
del squares[3]
print(squares)