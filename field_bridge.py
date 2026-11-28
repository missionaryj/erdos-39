"""Test shared vector differences across degrees two and three."""
from itertools import combinations, product

from endpoint_labels import reduce_equations


def square(x, modulus, prime):
    degree = len(modulus)
    terms = [0] * (2 * degree - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(x):
            terms[i+j] += a*b
    # modulus lists the low coefficients of a monic polynomial.
    for i in range(len(terms) - 1, degree - 1, -1):
        for j, coefficient in enumerate(modulus):
            terms[i-degree+j] -= terms[i] * coefficient
    return tuple(a % prime for a in terms[:degree])


def graph_points(prime, modulus):
    return [(x, square(x, modulus, prime))
            for x in product(range(prime), repeat=len(modulus))]


def gap_table(points, prime):
    table = {}
    for i, (x, y) in enumerate(points):
        for j, (xx, yy) in enumerate(points):
            if i == j:
                continue
            delta = tuple((b-a) % prime for a, b in zip(x+y, xx+yy))
            assert delta not in table
            table[delta] = (i, j)
    return table


def lift(point, prime):
    # Least significant fields use the two low horizontal and two low vertical
    # components; the larger block alone has the final pair of fields.
    x, y = point
    digits = x[:2] + y[:2] + x[2:] + y[2:]
    return sum(value * (2*prime)**i for i, value in enumerate(digits))


def integer_gaps(points, prime):
    marks = [lift(point, prime) for point in points]
    gaps = {abs(a-b) for a, b in combinations(marks, 2)}
    assert len(gaps) == len(marks) * (len(marks)-1) // 2
    return gaps


def check(prime, small_modulus, large_modulus, expected):
    small = graph_points(prime, small_modulus)
    large = graph_points(prime, large_modulus)
    first, second = gap_table(small, prime), gap_table(large, prime)
    equations = []
    for (i, j, k, l), (a, b) in first.items():
        if a < b:
            c, d = second[i, j, 0, k, l, 0]
            equations.append({a: 1, b: 1, len(small)+c: -1, len(small)+d: -1})
    assert len(equations) == len(small) * (len(small)-1) // 2
    variables = len(small) + len(large)
    nullities = [variables-len(reduce_equations(equations, characteristic))
                 for characteristic in (prime, 101)]
    assert nullities == [expected, expected]
    shared = len(integer_gaps(small, prime) & integer_gaps(large, prime))
    print(prime, len(equations), shared, *nullities)


if __name__ == "__main__":
    print("Prime, modular conflicts, integer conflicts, nullities in F_p and F_101")
    check(3, (1, 0), (1, 2, 0), 9)
    check(5, (2, 0), (1, 1, 0), 1)
    check(7, (1, 0), (2, 0, 0), 1)
