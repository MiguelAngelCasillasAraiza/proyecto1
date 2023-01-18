from datetime import datetime

def Meta(): 
   print("\nPara automatizar el examen de diagnostico.\n")
   
def isDate(test_str, format):
   try:
      return bool(datetime.strptime(test_str, format))
   except ValueError:
      return False
  
def displayDate(f):
   today = datetime.now()
   if f != None: 
      dateOut = f.strftime("%d-%m-%Y")
   else:
      dateOut = datetime.datetime(today)
   print(dateOut, end="")
   return today   

def Datos(): 
   global nombre, fecha, ListaCursos, Lenguajes
   
   format = "%d-%m-%Y"
   faux = ""
   while not isDate(faux, format):
      faux = input("Diga la fecha de hoy con formato \"dd-mm-yyyy\":")
   fecha = datetime.strptime(faux, format)     
   nombre = input("Diga su nombre:") 
   curso = input("Diga curso que impartió en Ago/Dic 2022 o <fin>:") 
   ListaCursos = []
   while (curso != "fin"):
      ListaCursos.append(curso)
      curso = input("Un curso que impartió en Ago/Dic 2022 o <fin>:")           
   lang = input("Lenguaje de programacion? o <fin>:") 
   Lenguajes= []
   while(lang != "fin"): 
      Lenguajes.append(lang)
      lang = input("Lenguaje de programacion? o <fin>:") 
           
#3. Sin calculos

def Resultados(): 
   print("\nEl profesor:", nombre)
   print("El dia de hoy:", end="")
   displayDate(fecha)
   print()
   if len(ListaCursos) >= 1:
      print("impartio los cursos: ", ListaCursos)
      print("durante el semestre ago-dic 2022")
   if (len(Lenguajes) >= 1): 
      print("programa en:", Lenguajes)
   print()                   
#5. Sin navegabilidad.

Meta()
Datos()
Resultados()

