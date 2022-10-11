class Producto(): 
    dicc={} 
    def __init__(self, cod_articulo: int, nombre: str, descripcion: str, precio: int): 
        #Cojo los atributos y monto sobre la marcha el diccionario que voy a meter en la lista
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
    cesta_prod = [] 
     
    def alta(self, nuevoArticulo): 
        '''Añadir producto al array cesta_prod'''
        self.cesta_prod.append(nuevoArticulo.dicc) 
         
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
     
#Comprobaciones de cada uno de los métodos 
nuevoArticulo = Producto(1, "teléfono", "es un teléfono",25) 
cesta_prod1 = Cesta() 
cesta_prod1.alta(nuevoArticulo) 
cesta_prod1.baja(2) 
#cesta_prod1.modificar(2) 
# codigo_prod = 2
# cesta_prod1.buscar(codigo_prod)
cesta_prod1.listar() 

