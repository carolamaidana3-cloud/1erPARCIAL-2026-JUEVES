class ProductoKwikE:
  def __init__(self, id_producto, descripcion, precio, stock):
    self.id_producto = id_producto
    self.descripcion = descripcion
    self.precio = precio
    self.stock = stock
  def __str__(self):
    return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock}"
  def __eq__(self, other):
    return self.id_producto == other.id_producto and self.descripcion == other.descripcion
    
producto1= ProductoKwikE(123, "Azucar", 1.50, 50)
producto2= ProductoKwikE(123, "Azucar", 1.50, 50)
producto3= ProductoKwikE(134, "Fideos", 2.50, 30)
print(producto1)
print(producto2)
print(producto1 == producto2)
print(producto3)
print(producto2 == producto3)
