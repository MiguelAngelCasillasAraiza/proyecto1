"""Saludo.py
TNM/ITL
9/Enero/2023
Diplomado: 
Automatización del despliegue de aplicaciones (DevOps) : 
"Linux y Python para DevOps"
por: Cirino Silva Tovar
LALO agrego esta línea   <--------------------------------------- :)
"""

from datetime import datetime

def meta():
    print("Para saludar\n")

def data():
    global timeObj
    
    timeObj = datetime.now()
    print("Hoy es ", end="")
    print(timeObj)
    
def resultado():
    """saludo = "Buenos Dias" if timeObj.hour < 12 else "Buenas Tardes" \
                       if timeObj.hour < 19 else "Buenas Noches"
    """
    if timeObj.hour < 12:
       saludo = "BuenosDias"
    elif timeObj.hour < 19:
       saludo = "Buenas Tardes"
    else:
       saludo = "Buenas Noches"
    print (saludo)
 
meta()   
data()
resultado()
 
 
