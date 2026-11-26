import dataset

miBase = dataset.connect("sqlite:///inventario2.db")
tabla = miBase["Producto"]

print("Bienvenido al Inventario")

while True:
    opciones = input("""
L - Listar
A - Agregar
B - Buscar por ID 
M - Modificar Producto por ID
Q - Quitar por nombre
I - Quitar por ID
R - Reporte de stock bajo
S - Salir

""")

    match opciones:

        case "S":
            break

        case "A":
         nombreProducto = input("\nNombre:")
         descripcionProducto = input("\nDescripción:")
         cantidadProducto = int(input("\nCantidad:"))
         precioProducto = float(input("\nPrecio: "))
         categoriaProducto = input("\nCategoría:")

         ProductoAgregar = {
          "Nombre": nombreProducto,
          "Descripcion": descripcionProducto,
          "Cantidad": cantidadProducto,
          "Precio": precioProducto,
          "Categoria": categoriaProducto
           }

         tabla.insert(ProductoAgregar)

         print("\nProducto agregado con éxito")

        case "L":
            for cosa in tabla:
               print(
                 f"ID: {cosa['id']} | "
                 f"Nombre: {cosa['Nombre']} | "
                 f"Descripcion: {cosa['Descripcion']} | "
                 f"Cantidad: {cosa['Cantidad']} | "
                 f"Precio: {cosa['Precio']} | "
                 f"Categoria: {cosa['Categoria']}"
                 )



        case "B":
           buscarProducto = int(input("\nID del producto a buscar: "))

           producto = tabla.find_one(id=buscarProducto)

           if producto:
            print("\nProducto encontrado:")
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['Nombre']}")
            print(f"Descripcion: {producto['Descripcion']}")
            print(f"Cantidad: {producto['Cantidad']}")
            print(f"Precio: {producto['Precio']}")
            print(f"Categoria: {producto['Categoria']}")

           else:
            print("\nNo se encontró ningún producto con ese ID.")

        case "M":
          modificarID = int(input("\nID del producto a modificar: "))

          producto = tabla.find_one(id=modificarID)

          if producto:
            print("\nProducto encontrado. Ingresá los nuevos datos:")

            nuevoNombre = input("\nNuevo nombre: ")
            nuevaDescripcion = input("\nNueva descripción: ")
            nuevaCantidad = int(input("\nNueva cantidad: "))
            nuevoPrecio = float(input("\nNuevo precio: "))
            nuevaCategoria = input("\nNueva categoría: ")

          tabla.update({
            "id": modificarID,
            "Nombre": nuevoNombre,
            "Descripcion": nuevaDescripcion,
            "Cantidad": nuevaCantidad,
            "Precio": nuevoPrecio,
            "Categoria": nuevaCategoria}, ["id"])

          print("\nProducto modificado con éxito")

        case "R":
          limite = int(input("\nIngresá el límite de stock: "))

          productosBajos = False

          for cosa in tabla:
             if cosa["Cantidad"] <= limite:
                print(
                f"ID: {cosa['id']} | "
                f"Nombre: {cosa['Nombre']} | "
                f"Cantidad: {cosa['Cantidad']} | "
                f"Precio: {cosa['Precio']}"
                )

                productosBajos = True

          if not productosBajos:
             print("\nNo hay productos con stock bajo.")
        
        case "Q":
          quitarProducto = input("\nProducto a quitar: ")
          tabla.delete(Nombre=quitarProducto)
          print(f"*** {quitarProducto} eliminado con éxito ***")
          
        case "I":
            quitarProducto = int(input("\nId de producto a quitar: "))
            tabla.delete(id=quitarProducto)
            print(f"*** Producto con ID: {quitarProducto} eliminado con éxito ***")