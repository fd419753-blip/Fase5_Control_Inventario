# Programa para el control de inventario y reabastecimiento

# Matriz con los datos de los productos
# [Codigo, Nombre, Stock actual, Stock minimo]

inventario = [
    [101, "Arroz", 5, 20],
    [102, "Aceite", 10, 15],
    [103, "Azucar", 30, 20],
    [104, "Leche", 3, 12],
    [105, "Cafe", 15, 15]
]


# Funcion para calcular la cantidad que se debe pedir
def calcular_reabastecimiento(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


# Mostrar los resultados del inventario
print("CONTROL DE INVENTARIO Y REABASTECIMIENTO")
print("------------------------------------------")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    print("Codigo:", codigo)
    print("Producto:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock minimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("------------------------------------------")