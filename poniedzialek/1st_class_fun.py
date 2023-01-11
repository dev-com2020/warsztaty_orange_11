def example(a, b, **kwargs):
    return a * b - kwargs


print(type(example))
print(example.__code__.co_varnames)
print(example.__code__.co_argcount)

liczymy = lambda x, y: y * x - 1

print(liczymy(100, 99))

