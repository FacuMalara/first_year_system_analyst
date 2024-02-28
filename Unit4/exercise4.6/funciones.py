producto_1_nombre = 'producto_1'
producto_2_nombre = 'producto_2'
producto_3_nombre = 'producto_3'

producto_1_precio = 300
producto_2_precio = 400
producto_3_precio = 500

producto_1_stock = 5
producto_2_stock = 4
producto_3_stock = 7

# medio_pago = ''


def mostrar_productos():
    print(f'nombre \t\t precio \t stock')
    print(f'{producto_1_nombre} \t {producto_1_precio} \t\t {producto_1_stock}')
    print(f'{producto_2_nombre} \t {producto_2_precio} \t\t {producto_2_stock}')
    print(f'{producto_3_nombre} \t {producto_3_precio} \t\t {producto_3_stock}')
    input("Presione enter para continuar...")


def comprar_producto():
    producto_comprar = input('eliga el producto a comprar "1" "2" "3": ')
    match producto_comprar:
        case "1":
            return producto_1_precio
        case "2":
            return producto_2_precio
        case "3":
            return producto_3_precio
        case _:
            print("\nIngreso incorrecto")
            input("Presione enter para continuar...")

    # verificar si el producto es un producto con las variables


def elegir_medio_pago():
    global producto_1_precio
    global producto_2_precio
    global producto_3_precio
    while True:
        opcion_1 = input('''
Eliga el medio de pago
- Efectivo (E)
- Tarjeta debito (TD))
- Tarjeta credito (TC))
Opcion: ''')
        if opcion_1.lower() == 'e':
            return 0.9
        elif opcion_1.lower() == 'td':
            return 1
        elif opcion_1.lower() == 'tc':
            return 1.1
        else:
            print('\nopcion incorrecta')
            input("Presione enter para continuar...")


def precio():
    try:
        global producto_1_precio
        global producto_2_precio
        global producto_3_precio
        producto = input("Seleccione producto 'P1' 'P2' 'P3': ")
        nuevo_precio = float(input("Ingrese nuevo monto: "))
        match producto:
            case 'P1':
                producto_1_precio = nuevo_precio
                print(f"\nProducto 1 precio: {nuevo_precio}")
                input("Presione enter para continuar...")
                return nuevo_precio
            case 'P2':
                producto_2_precio = nuevo_precio
                print(f"\nProducto 2 precio: {nuevo_precio}")
                input("Presione enter para continuar...")
                return nuevo_precio
            case 'P3':
                producto_3_precio = nuevo_precio
                print(f"\nProducto 3 precio: {nuevo_precio}")
                input("Presione enter para continuar...")
                return nuevo_precio
            case _:
                print("\nIngrese datos validos")
                input("Presione enter para continuar...")
    except ValueError as e:
        print(f"\nIngresaste cualquier cosa {e}")


def precio_fin():
    precio_producto = comprar_producto()
    medio_pago = elegir_medio_pago()
    precio_final = precio_producto * medio_pago
    print(f"\nEl costo es {precio_final}")
    global producto_1_stock
    global producto_2_stock
    global producto_3_stock
    if precio_producto == producto_1_precio and producto_1_stock != 0:
        producto_1_stock -= 1
        print(f"\nProducto 1 stock: {producto_1_stock}")
        input("Presione enter para continuar...")
        return producto_1_stock
    elif precio_producto == producto_2_precio and producto_2_stock != 0:
        producto_2_stock -= 1
        print(f"\nProducto 2 stock: {producto_2_stock}")
        input("Presione enter para continuar...")
        return producto_2_stock
    elif precio_producto == producto_3_precio and producto_3_stock != 0:
        producto_3_stock -= 1
        print(f"\nProducto 3 stock: {producto_3_stock}")
        input("Presione enter para continuar...")
        return producto_3_stock
    else:
        print("\nNo hay stock")
        input("Presione enter para continuar...")
    return


def consultar_stock():
    global producto_1_stock
    global producto_2_stock
    global producto_3_stock
    print(f"\nproducto 1: {producto_1_stock}")
    print(f"\nproducto 2: {producto_2_stock}")
    print(f"\nproducto 3: {producto_3_stock}")
    input("Presione enter para continuar...")


def agregar_stock():
    try:
        global producto_1_stock
        global producto_2_stock
        global producto_3_stock
        agregar = input(
            "A que producto desea agregar unidades? 'P1' 'P2' 'P3': ")
        cantidad = int(input("Cuantas unidades? "))
        match agregar:
            case "P1":
                producto_1_stock += cantidad
                print(f"\nProducto 1 stock: {producto_1_stock}")
                input("Presione enter para continuar...")
            case "P2":
                producto_2_stock += cantidad
                print(f"\nProducto 2 stock: {producto_2_stock}")
                input("Presione enter para continuar...")
            case "P3":
                producto_3_stock += cantidad
                print(f"\nProducto 3 stock: {producto_3_stock}")
                input("Presione enter para continuar...")
            case _:
                print("\nIngresaste dato invalido")
                input("Presione enter para continuar...")

    except ValueError as e:
        print(f"Dato no valido ingrese numeros enteros: {e}")


def menu_general():
    while True:
        opcion = input('''
Eliga una opcion
  1. Ver menu de productos
  2. Comprar un producto
    -  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock)
    -  Pagar con tarjeta debito (se debe descontar el stock)
    -  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
  3.  consultar productos y stock
  4.  agregar stock a los productos
  5.  cambiar el precio a los productos
  6.  Salir
Opcion: ''')
        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            precio_fin()
        elif opcion == '3':
            consultar_stock()
        elif opcion == "4":
            agregar_stock()
        elif opcion == "5":
            precio()
        elif opcion == "6":
            print("Saliendo")
            return
        else:
            print('opcion incorrecta')
