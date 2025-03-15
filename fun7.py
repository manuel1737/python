def promedio(*args):
    return sum(args) / len(args) if args else 0

print(promedio(3, 5, 7))
print(promedio(10, 20, 30, 40))
print(promedio())
