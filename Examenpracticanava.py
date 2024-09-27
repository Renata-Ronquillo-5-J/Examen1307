class Productos1307:   ##   Renata Ronquillo Lopez 1307
   
    id_producto1307 = 0       
    nombre1307 = " "
    stock1307 = 0
    proveedores1307 = " "
    prec_venta1307 = 0
    prec_mayo1307 = 0
    descri1307 = " "
 
    def mostrardatos(self):
         print("\n Mostrar datos")   ##Función

         print(f" Id del producto: {self.id_producto1307}")
         print(f" Nombre del producto: {self.nombre1307}")
         print(f" Stock del producto: {self.stock1307}")
         print(f" Proveedores: {self.proveedores1307}")
         print(f" Precio a la venta (c/1): {self.prec_venta1307}")
         print(f" Precio Mayoreo : {self.prec_mayo1307}")
         print(f" Descripción del prducto : {self.descri1307}")



##Lista
def lista_Idproducto1307():
    Productos=[1389356, 48936, 19483786, 194883756, 14988376, 147837568, 2948783 ]
    print(Productos)
    
    for pro in Productos:
        print(pro)


def tupla_nombres1307():
    name=(" Labiales ", " Perfumes ", " Peluches ", " Mascarillas ", " Audifonos ", " Rubor ", " Loncheras" )
    print(name)

    for nombres in name:
        print(nombres)

def diccionario_stock1307():
    stock = {
        " Labiales: ": 138,
        " Perfumes: ": 56,
        " Peluches: ": 200,
        " Mascarillas: ": 90,
        " Audifonos: ": 80,
        " Rubores: ": 100,
        " Loncheras: ": 28
    }
    print(stock)
    for producto, stocki in stock.items():
        print(producto, stocki)

def alta1307():
    print("  Se dio de alta la información correctamente")


def baja1307():
    print("  Se de baja la información ")






##Espacio

obj = Productos1307()
##darle valor
obj.id_producto1307 = 23989392
obj.nombre1307 = " Audifonos inhalambricos de my melody"
obj.stock1307 = 145
obj.proveedores1307 =" Sr. Francisco Aguirre, Sr. Luis Maldonado"
obj.prec_venta1307= " $250 "
obj.prec_mayo1307= "$20,900 "
obj.descri1307 =" Audifonos inhalambricos con diseño de My melody, duración de la bateria 9hr, 1m de distancia "


print(" \n ")
obj.mostrardatos()

print(" \n Id de productos: ")
lista_Idproducto1307()


print(" \n  Nombre de productos: ")
tupla_nombres1307()

print( " \n Stock de los productos:  ")
diccionario_stock1307()

print(" \n Alta: ")
alta1307()


print(" \n Baja  ")
baja1307()