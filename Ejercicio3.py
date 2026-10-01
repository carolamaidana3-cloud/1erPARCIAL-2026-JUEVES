def interrupciones(a, b):
   if b == 0:
     return 0
   else:
      return a + interrupciones(a, b - 1)

   a = int(input("Interrupciones por hora: "))
   b = int(input("Horas de la tarde: "))

   total = interrupciones(a, b)
   print("Total de interrupciones:", total)
