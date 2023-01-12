generator_1 = (x for x in [1, 2, 3, 4, 5])

print(type(generator_1))
print(generator_1)

def generator_2():
    i = 1
    while True:
        yield i*i
        i += 1

# for num in generator_2():
#     if num > 100:
#         break
#     print(num)

def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibo()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print("coś.....")
print("coś.....")
print(next(fib))
print("coś.....")
print("coś.....")
print(next(fib))

