def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num

a = odd_nums(5)
print(next(a))
print(next(a))