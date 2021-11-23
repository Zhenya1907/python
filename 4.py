src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]


lst = [num for i, num in enumerate(src)if i != 0 and num > src[i-1]]
print(lst)
