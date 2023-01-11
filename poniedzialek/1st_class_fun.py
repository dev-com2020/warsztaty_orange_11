def example(a, b, **kwargs):
    return a * b - kwargs


# print(type(example))
# print(example.__code__.co_varnames)
# print(example.__code__.co_argcount)

liczymy = lambda x, y: y * x - 1

# print(liczymy(100, 99))

r_0 = {'miasto': 'Kielce'}
r_1 = {'miasto': 'Kielce', 'ZIP': '25-900'}

d_zip = lambda row: row.setdefault('ZIP', '00-000')
# print(d_zip(r_0))
# print(r_0)
# print(d_zip(r_1))
# print(r_1)

lata = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
        (2004, 31.33), (2008, 32.84), (2009, 33.02), (2010, 32.92)]

# print(max(lata))
# print(max(lata, key=lambda c: c[1]))
# print(max(map(lambda c: (c[1], c), lata))[1])

print(0 and 'right')
print(True and 'right')