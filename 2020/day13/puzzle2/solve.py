
import operator
import functools

with open('./input') as input_file:
    raw_lines = input_file.readlines()

raw_buses = raw_lines[1].strip().split(',')
buses = [((int(n) - i) % int(n) + 1, int(n))
         for i, n in enumerate(raw_buses) if n != "x"]
# buses = [(3, 5), (6, 7), (4, 11)]


def get_mod_inverse(n, m):
    if n == 0:
        return 0
    x = 1

    while (n * x) % m != 1:
        x += 1

    return x


assert get_mod_inverse(56, 5) == 1
assert get_mod_inverse(40, 7) == 3
assert get_mod_inverse(35, 8) == 3


def debug(s, x):
    print(s, repr(x))


debug("buses", buses)
b = [bi for (bi, _) in buses]
debug("b", b)
n = [bus for (_, bus) in buses]
debug("n", n)
N = functools.reduce(operator.mul, n, 1)
debug("N", N)
Ni = [N//ni for ni in n]
debug("Ni", Ni)
xi = [get_mod_inverse(Ni[i], m) for i, (n, m) in enumerate(buses)]
debug("xi", xi)
x_ = [a * b * c for a, b, c in zip(b, Ni, xi)]
debug("x_", x_)
X = sum(x_)
debug("x", X)
print(X % N - 1)

# assert X % N == 1068781
