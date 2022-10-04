class Articulo():
    def _init_(self, codigo_articulo, nombre, precio, descripcion):
        self.codigo_articulo = codigo_articulo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Cesta():
    cesta = []

    def agregar_cesta(self,nuevo_articulo):
        self.cesta.append({"codigo_articulo":nuevo_articulo.codigo_articulo,"nombre":nuevo_articulo.nombre,"precio":nuevo_articulo.precio,"descripcion":nuevo_articulo.descripcion})
    def listar(self):
        for i in range(0, len(self.cesta)):
            print("ARTICULO: ",self.cesta[i]["nombre"])
            print("Codigo del articulo: " , self.cesta[i]["codigo"])
            print("nombre del articulo: " , self.cesta[i]["nombre"])
            print("precio del articulo: " , self.cesta[i]["precio"])
            print("descripcion del articulo: " , self.cesta[i]["descripcion"],"\n")

articulo1 =  Articulo(21,"Destornillador",54,"Destornillador de estrella")

milista = Cesta()

milista.agregar_cesta(articulo1)

milista.listar()