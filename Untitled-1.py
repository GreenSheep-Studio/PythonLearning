def f(a, *b):
    n = 0
    for i in b:
        n += i
    return n
res = f(1, 3, 5, 7)
print(res)

import 