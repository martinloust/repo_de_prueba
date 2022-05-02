#Ejercicio 1
 # tenes que obretener los substring que estan entre aa y gg, 
 # menos las letras c en "ttaatatggttaacatgg"
 # cuantas veces aparece bc9 en xsabc9cabcb3sabc9
import re
def aparece_bc9(string):
    return len(re.findall("bc9", string))

print(aparece_bc9("xsabc9cabcb3sabc9"))

def entre_letras(string):
    return re.findall("aa([^c]*?)gg", string)

print(entre_letras("ttaatatggttaacatgg"))

# Ejercicio 2


# class Auto():
#     def __init__(self):
#         self.consumo = 0.05
#         self.rpm = 0
#         self.cambio = None

#     def arrancar(self):
#         self.cambio = 1
#         self.rpm = 500

#     def subirCambio(self):
#         if self.cambio < 5:
#             self.cambio += 1
        
#     def bajarCambio(self):
#         if self.cambio > 1:
#             self.cambio -= 1

#     def subirRpm(self, cantidad):
#         self.rpm < 5000
#         self.rpm += cantidad

#     def velocidad(self):
#         return((self.rpm/100) * (0.5 + (self.cambio / 2)))

#     def consumoActualPorKm(self):
#         if self.rpm > 3000:
#             if self.cambio == 1:
#                 return round((self.consumo_actual * ((self.rpm-2500) / 500) * 3),3)
#             elif self.cambio == 2:
#                 return round((self.consumo_actual * ((self.rpm-2500) / 500) * 2),3)
#             elif self.cambio <= 5:
#                 return round((self.consumo * ((self.rpm - 2500) / 500)),3)
#         elif self.cambio == 1:
#             if self.cambio == 2:
#                 return round((self.consumo * 2),3)
#         else:
#             return self.consumo
            

# auto1 = Auto()
# auto1 = Auto()
# auto1.arrancar()
# auto1.subirRpm(3500)
# auto1.subirCambio()
# auto1.subirCambio()
# auto1.subirCambio()
# auto1.bajarCambio()
# print(auto1.consumoActualPorKm())
# print(auto1.velocidad())

# Ejercicio 3
# ¿Qué tipo de error tira? ¿Cómo solucionarlo?
# 1. ZeroDivisionError
# 2:
# def obtener_media(lista):
#     sumatoria = 0

#     for valor in lista:
#         sumatoria += valor
#     longitud = legend(lista)

#     try:
#         return sumatoria / longitud
#     except ZeroDivisionError:
#         print("No se puede dividir por 0")

# print(obtener_media("hola como estas"))

# Ejercicio 4
# import os
# import glob

# def unir_txt():
#     os.mkdir("Resultado") # Crea la carpeta resultado
#     txt = glob.glob("*.txt") # Agarra todos los txt
#     salida = open("Resultado/texto_completo.txt", "a")    
#     for i in txt:
#         arch = open(i, "r")
#         salida.write(arch.read())
#         arch.close()
#     salida.close()

#Alternativa:
# def unir_txt():
#     os.mkdir("Resultado")
#     txt = glob.glob("*.txt")
#     with open("Resultado/texto_completo.txt", "a") as salida:
#         for i in txt:
#             with open(txt, "r") as archivo:
#                 salida.write(archivo.read())









