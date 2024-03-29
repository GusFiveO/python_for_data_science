from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
invalid_weight = [38.4, "lol"]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print(give_bmi(height, invalid_weight))         # contain a string
print(give_bmi(height, invalid_weight[:-1]))    # not the same size
print(apply_limit(invalid_weight, 26))          # contain a string
print(give_bmi(26, 26))                         # not iterable
print(apply_limit(26, 26))                      # not iterable
