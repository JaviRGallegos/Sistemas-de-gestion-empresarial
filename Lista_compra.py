class Producto(): 
     
    def __init__(self, cod_articulo: int, nombre: str, descripcion: str, precio: int): 
        #Cojo los atributos y monto sobre la marcha el diccionario que voy a meter en la lista
        self.dicc = {}
        self.cod_articulo = cod_articulo 
        self.nombre = nombre 
        self.descripcion = descripcion 
        self.precio = precio 
        self.dicc["codigo"]= self.cod_articulo 
        self.dicc["nombre"]= self.nombre 
        self.dicc["descripcion"]= self.descripcion 
        self.dicc["precio"]= self.precio
         

class Cesta: 
    #Lista donde voy a almacenar los diccionarios que contienen los datos de la clase Producto
    def __init__(self) -> None:
        self.cesta_prod = []
         
    def alta(self, nuevoProducto): 
        '''Añadir producto al array cesta_prod'''
        self.cesta_prod.append(nuevoProducto.dicc)

    def listar(self): 
        '''Imprimir todos los articulos que hay en la lista cesta_prod'''
        for producto in self.cesta_prod:
            print("Código:", producto["codigo"], "|", end = ' ') #Quiero imprimir todo en la misma línea, el end por defecto en python vale "\n"
            print("Nombre:", producto["nombre"], "|", end = ' ')
            print("Descripcion:", producto["descripcion"], "|", end = ' ')
            print("Precio:", producto["precio"],"\n")

    def baja(self,codigo):
        '''Quitar un producto del array cesta_prod'''
        for i in range (len(self.cesta_prod)):
            if self.cesta_prod[i]["codigo"] == codigo:
                self.cesta_prod.remove(self.cesta_prod[i])
                      
    def modificar(self,codigo_mod):
        '''Modificar un atributo del diccionario, buscado por código del artículo, a elección del usuario'''
        resul = int(input("Introduce qué quieres modificar (1->nombre | 2->descripcion | 3->precio)"))
        for producto in self.cesta_prod:
            if producto["codigo"] == codigo_mod:
                if resul == 1:
                    producto["nombre"] = input("Introduce el nuevo nombre del producto: ") 
                elif resul == 2:
                    producto["descripcion"] = input("Introduce la nueva descripción del producto: ") 
                elif resul == 3:
                    producto["precio"] = int(input("Introduce el nuevo precio del producto: "))
                print("Código", producto["codigo"]) 
                print("Nombre", producto["nombre"]) 
                print("Descripcion", producto["descripcion"]) 
                print("Precio", producto["precio"],"\n") 
            else: 
                print("No se ha modificado el producto") 
    
    def buscar(self,codigo): 
        '''Buscar producto en el array cesta_prod por código y se muestra'''
        for articulo in self.cesta_prod: 
            if articulo["codigo"] == codigo: 
                print("Codigo", articulo["codigo"]) 
                print("Nombre", articulo["nombre"]) 
                print("Descripcion", articulo["descripcion"]) 
                print("Precio", articulo["precio"],"\n") 
     



cesta_prod1 = Cesta()

# Meto varios artículos para comprobar que funciona
nuevoArticulo = Producto(1, "teléfono", "es un teléfono",25)

# cesta_prod1.cesta_prod = []
cesta_prod1.alta(nuevoArticulo)
nuevoArticulo2 = Producto(2, "ordenador", "es un ordenador",25)
nuevoArticulo3 = Producto(3, "televisor", "es un televisor",25)
cesta_prod1.alta(nuevoArticulo3)
cesta_prod1.listar() # 1, 3

print("========================================================================")
nuevoArticulo4 = Producto(4, "portátil", "es un portátil",25)
cesta_prod1.alta(nuevoArticulo2)
cesta_prod1.alta(nuevoArticulo4)

cesta_prod1.listar() # imprime 1, 3, 2 y 4 (en ese orden)
#Comprobaciones de cada uno de los métodos 
#### DESCOMENTAR USANDO CONTROL + Ç ####
#cesta_prod1.baja(2)
#cesta_prod1.modificar(3)
#codigo_prod = 2
#cesta_prod1.buscar(codigo_prod)

#######################################################################################


accion = input("Introduzca acción a realizar (1 -> alta, 2 -> baja, 3 -> modificar, 4-> buscar, 5 -> listar, salir mata el programa)")
while accion != "salir":
    if accion == "1":
        codigo = int(input("Introduzca el código del nuevo artículo: "))
        nombre = input("Introduzca el nombre del artículo: ")
        desc = input("Introduzca la descripción del artículo: ")
        precio = int(input("Introduzca el precio del artículo (no números racionales)"))
        nuevoProducto = Producto(codigo, nombre, desc, precio)
        cesta_prod1.alta(nuevoProducto)
        cesta_prod1.listar()
        accion = input("Introduzca acción a realizar (1 -> alta, 2 -> baja, 3 -> modificar, 4-> buscar, 5 -> listar, salir mata el programa)")
    elif accion == "2":
        cod_baja = int(input("Intruzca código del producto a retirar (solo enteros): "))
        cesta_prod1.baja(cod_baja)
        accion = input("Introduzca acción a realizar (1 -> alta, 2 -> baja, 3 -> modificar, 4-> buscar, 5 -> listar, salir mata el programa)")
    elif accion == "3":
        cod_modificar = int(input("Intruzca código del producto a modificar (solo enteros): "))
        cesta_prod1.modificar(cod_modificar)
        accion = input("Introduzca acción a realizar (1 -> alta, 2 -> baja, 3 -> modificar, 4-> buscar, 5 -> listar, salir mata el programa)")
    elif accion == "4":
        cod_buscar = int(input("Intruzca código del producto a buscar (solo enteros): "))
        cesta_prod1.buscar(cod_buscar)
        accion = input("Introduzca acción a realizar (1 -> alta, 2 -> baja, 3 -> modificar, 4-> buscar, 5 -> listar, salir mata el programa)")
    elif accion == "5":
        cesta_prod1.listar()
        accion = input("Introduzca acción a realizar (1 -> alta, 2 -> baja, 3 -> modificar, 4-> buscar, 5 -> listar, salir mata el programa)")