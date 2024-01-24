from array2D import slice_me

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

print(slice_me(family, 0, 2))
print()
print(slice_me(family, 1, -2))
print()
print(slice_me("LOL", 1, -2))                   # first parameter is a string
print()
print(slice_me([], 1, -2))                      # empty list
print()
print(slice_me([[10], [20, 10]], '1', '-2'))    # not same size list
print()
print(slice_me(family, '1', '-2'))              # last parameter not intergers
