#las funciones en python se definen con def:

def funcion_tonta(nombre):
    separador = " "
    mensaje = separador.join(("oh", "El tonto de",nombre))
    print(mensaje)



#una funcion un poco mas compleja: calculo del digito verificador

def digito_verificador(rut):
    digito = ""
    contador = 2
    suma = 0
    multiplo = 0
    while rut > 0:
        multiplo = ( rut % 10 ) * contador
        suma = suma + multiplo
        rut = rut // 10 #division entera!
        contador = contador + 1
        if contador == 8 :
            contador = 2
    digito = 11 - (suma % 11)
    if digito == 10:
        digito = 'k'
    if digito == 11 :
        digito = 0
    return str(digito)


mi_rut = 18547493
print("-".join((str(mi_rut), digito_verificador(mi_rut))))
# y llamamos  la funcion..
funcion_tonta("francisco")
funcion_tonta("jesus")