class Inventario: 
  def __init__(self, id_producto, fecha_vencimiento, precio, stock):
   self.id_producto = id_producto
   self.fecha_vencimiento = fecha_vencimiento
   self.precio = precio
   self.stock = stock

  def cambiar_datos(self, fecha_vencimiento, precio, stock):
    self.fecha_vencimiento = fecha_vencimiento
    self.precio = precio
    self.stock = stock

  def calcular_dias(self):
    hoy = date.today()
    dias = (self.fecha_vencimiento - hoy).days
    if dias < 0:
      print("El producto ha caducado")
      self.stock = 0
    else:
      print(f"Faltan {dias} días para que el producto caduque")
    

