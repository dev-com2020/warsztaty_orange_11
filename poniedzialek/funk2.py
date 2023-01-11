from collections.abc import Sequence, Callable

s = 100


def sum_numeric(limit=10) -> int:
    s = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    return s


def suma(seq: Sequence[int]) -> int:
    if len(seq) == 0:
        return 0
    return seq[0] + suma(seq[1:])


def until(
        limit: int,
        filter_func: Callable[[int], bool],
        v: int
) -> list[int]:
    if v == limit:
        return []
    elif filter_func(v):
        return [v] + until(limit, filter_func, v + 1)
    else:
        return until(limit, filter_func, v + 1)


def mult_3_5(x: int) -> bool:
    return x % 3 == 0 or x % 5 == 0


def sum_fun(limit=10):
    return suma(until(limit, mult_3_5, 0))


print(until(10, mult_3_5, 0))
print(sum_fun())

wyniki = []
wyniki.append(sum_numeric(20))
wyniki.append(sum_numeric(30))
wyniki.append(sum_numeric(50))
wyniki.append(sum_numeric(60))
wyniki.append(sum_numeric(33))
wyniki.append(sum_numeric(23))
wyniki.sort()
# print(wyniki)
# print(suma(wyniki))
# print(suma([5, 6]))
# print(suma([5]))
# print(suma([]))
