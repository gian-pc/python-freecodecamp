def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n <= 0:
        return 'Argument must be an integer greater than 0.'

    result = []
    for x in range(1, n + 1):
        result.append(str(x))
    return ' '.join(result)


print(number_pattern(4))  # 1 2 3 4
print(number_pattern(12))  # 1 2 3 4 5 6 7 8 9 10 11 12
print(number_pattern('a'))  # Argument must be an integer value.
print(number_pattern(-1))  # Argument must be an integer greater than 0.