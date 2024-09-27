class miniso1307():
        id_producto1307 = 0       
        nombre1307 = " "
        stock1307 = 0
        proveedores1307 = " "
        prec_venta1307 = 0
        prec_mayo1307 = 0
        descri1307 = " " 

        
    
def Dic_Producto1307():
        dicci_producto = {
        " \n  Id del producto: ": 3598356,
        " Nombre: ": "Audifonos inhalambricos my melody ",
        " Stock: ": 1353,
        " Proveedor: ": "Sr.Francisco aguirre ",
        " Precio de venta: ": "$278",
        " Precio Mayoreo: ": "$ 20,000",
        " Descripción: ": " Audifonos inhalambricos de my melody, duración de bateria 5hrs y con una distancia de 1.5m "}
        print(dicci_producto)
        for id,des in dicci_producto.items():
            print(id, des)



def Dic_Pro1307():
        diccionario_Proveedores_1307 =  {
        " \n Id Del proveedor: ": 94383586,
        " Nombre: ":" Sra. Ailin Miscles ",
        " RFC: ":" FUGUB38853DHGUH",
        " Curp: ": "ROLR0708MVHNPA",
        " Edad: ": 34,
        " Sexo: ": "Femenino ",
        " No. Telefono: ": "656 577 5685"
}
        print(diccionario_Proveedores_1307)
        for Id, No in diccionario_Proveedores_1307.items():
            print(Id,No)

    
def dic_Cliente1307():
        Diccionario_Clientes1307 = {
    
    "\n  Id del cliente: ": 2848375,
    "No. Telefono: ": "656 4596 468",
    "Correo: ": "Ronquitos@gmail.com",
    "Edad: ": 25,
    "Curp: ": "ROLR706485MVHNPA",
    "RFC: ": "ROR46OLTOJ868",
    "Sexo:": " Femenino "
}
        print(Diccionario_Clientes1307)
        for id, No in Diccionario_Clientes1307.items():
            print(id,No)

def Dic_Venta1307():
        Diccioonario_Venta1307 = {
    " \n Id del producto:": 3487486,
    "Stock: ": 234,
    "Vendedor:": " Ailin ",
    "Fecha de venta:": "27/09/2024 hrs: 09:19:22",
    "Precio: ": "$300",
    "Nombre del producto: ": "Audifonos",
    "Descuento:" : "5%"
    
}
        print(Diccioonario_Venta1307)
        for id, No in Diccioonario_Venta1307.items():
            print(id,No)


obj = miniso1307()
obj.id_producto1307= 293857
obj.nombre1307 = " Audifonos"
obj.stock1307 = 2335
obj.proveedores1307= "Ailin, Alexis"
obj.prec_venta1307= " $3456"



print("\n ♥ Producto: ")
Dic_Producto1307()
print("\n ♥ Provedores: ")
Dic_Pro1307()
print("\n ♥ Clientes: ")
dic_Cliente1307()
print("\n ♥ Venta:")
Dic_Venta1307()

