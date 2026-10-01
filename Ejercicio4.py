
        
        #reso:
        def ordenar_eventos(eventos, expresion=False):
  if expresion:
    #orden descendente Z-A
    return sorted(eventos, reverse=True)
  else:
    #ascendente Z-A
    return sorted(eventos)
eventos = [
    "Kermés",
    "Concurso de Comida",
    "Reunión del Concejo Municipal"
 ]

print("Orden Ascendente:")
print(ordenar_eventos(eventos))
print("\nExpresion True:")
print(ordenar_eventos(eventos, True))
print("\nExpresion False:")
print(ordenar_eventos(eventos, False ))
    

