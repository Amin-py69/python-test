def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


def expand_binomial(n):
    result = ""
    for i in range(n + 1):
        coefficient = binomial_coefficient(n, i)
        if coefficient > 1:
            result += str(coefficient)
        if n - i > 0:
            result += "x"
            if n - i > 1:
                result += "^{" + str(n - i) + "}"
        if i > 0:
            result += "y"
            if i > 1:
                result += "^" + str(i)
        if i < n:
            result += "+"
    return result


n = int(input())
print(expand_binomial(n))
