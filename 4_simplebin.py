def meta():
   print("Para convertir un entero a binario")

def isNum (cad):
   try: 
      int (cad)
      return True
   except ValueError:
      print ("Solo se aceptan numeros enteros\n")
      return False
    
def data():
   global decimal
   
   decimal = ""
   while not isNum(decimal):
      decimal = input("De un entero:")
   decimal = int(decimal)   
          
def sale():               
   print(bin(decimal).replace('0b',''))

respuesta = ''
meta()
while(respuesta in "sS"):      
   data()
   sale()
   respuesta = input('convertir otro entero a binario? s/n:')

