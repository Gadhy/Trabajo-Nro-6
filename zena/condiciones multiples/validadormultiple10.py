import os
#INPUT
frecuencia= float(input("FRECUENCIA: "))

#PROCESSING
velocidad_angular= 2*frecuencia

#VALIDADOR
validador_de_la_velocidad_angular=(velocidad_angular<30)

#OUTPUT
print("#################################################")
print("################## VELOCIDAD ANGULAR ############")
print("#################################################")
print("############# frecuencia:", frecuencia,"############")
print("############ velocidad angular:", velocidad_angular,"###########")
print("#################################################")

#CONDICION MULTIPLE
if ( validador_de_la_velocidad_angular>=30 and validador_de_la_velocidad_angular>20 ):
    print("VEBTILADOR EN BUEN ESTADO")
#fin_if

if ( validador_de_la_velocidad_angular<20 and validador_de_la_velocidad_angular<10 ):
    print("VENTILADOR MALOGRADO")
