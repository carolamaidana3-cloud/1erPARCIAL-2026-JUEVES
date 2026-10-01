from datetime import date
def __init__(self):
  self.bebidas = []
  self.snacks = []
  self.conveniencia = []


 def agregar_producto(self, pasillo, producto)
  if pasillo.lower() == "bebidas":
    self.bebidas.append(producto)
  elif pasillo.lower() == "snacks":
    self.snacks.append(producto)
  elif pasillo.lower() == "conveniencia":
    self.conveniencia.append(producto)
#buscar producto por id
def buscar_producto(self, id_producto):
  for pasillo in [self.bebidas, self.snacks, self.conveniencia]:
    for producto in pasillo:
      if producto.id_producto == id_producto:
        return producto
  return None
  #eliminacion

def eliminar_producto(self, id_producto):
  for pasillo in [self.bebidas, self.snacks, self.conveniencia]:
    for producto in pasillo:
      if producto.id_producto == id_producto:
        pasillo.remove(producto)
        print(f"Producto'{producto.nombre}'eliminado.")
        return True
        print(f"Producto con ID {id_producto} no encontrado.")
  return False  
  #actualizar
  def mostrar_productos(self)
   print("\n---BEBIDAS---")
   for producto in self.bebidas:
     print(producto)
   print("\n---SNACKS---")
   for producto in self.snacks:
     print(producto)
   print("\n---CONVENIENCIA---")
   for producto in self.conveniencia:
     print(producto)
  #vecimiento en las prox 24 hs 
  def eliminar_productos_por_vencer(self):
    ahora = datetime.now()
    vencido = ahora + timedelta(hours=24)
    eliminados = []
    for pasillo in [self.bebidas, self.snacks, self.conveniencia]:
     productos_a_eliminar = []
    for producto in pasillo:
     if ahora <= producto.fecha_vencimiento <= vencido:
         productos_a_eliminar.append(producto)

    for producto in productos_a_eliminar:
         eliminados.append(producto)
         pasillo.remove(producto)
   print("\nProductos que vencen en las proximas 24hs:")
    if eliminados:
     for producto in eliminados: 
  print(producto)
    else: 
   print("No hay productos sin vencer en las proximas 24hs:")
   return eliminados
