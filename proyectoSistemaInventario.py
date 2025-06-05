import keyword
print ("Bienvenid@ al Sistema de Control de Inventario")
nombreProducto = input("Ingrese nombre del producto:").title()
cantidadProducto = int (input("Ingresar cantidad:"))
precioUnitario = float(input("Ingresar precio unitario:"))
valorInventarioInicial = cantidadProducto * precioUnitario

print("\n Inventario Inicial")
print("Nombre del Producto:",nombreProducto)
print(f"Cantidad de unidades de {nombreProducto}: {cantidadProducto}")
print(f"Precio por unidad: $ {precioUnitario:.2f}")
print (f"Valor total del inventario inicial: $ {valorInventarioInicial:.2f}")
print ("Bienvenid@ al Sistema de Control de Inventario")

print("." * 30)

nombreProducto = input("Ingrese nombre del producto:").title()
cantidadProducto = int (input("Ingresar cantidad:"))
precioUnitario = float(input("Ingresar precio unitario:"))
valorInventarioInicial = cantidadProducto * precioUnitario

print("\n Inventario Inicial")
print("Nombre del Producto:",nombreProducto)
print(f"Cantidad de unidades de {nombreProducto}: {cantidadProducto}")
print(f"Precio por unidad: $ {precioUnitario:.2f}")
print (f"Valor total del inventario inicial: $ {valorInventarioInicial:.2f}")

print("." * 30)