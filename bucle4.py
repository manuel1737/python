productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

for producto, precio in productos.items():
    print(f"{producto}: {precio}")

suma_total = sum(productos.values())

productos_mayor_a_1 = [producto for producto, precio in productos.items() if precio > 1.0]
