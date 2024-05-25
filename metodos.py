Numero = 2+3
print(Numero)
cadena1 = "SOy la primer cadena"
cadena1_en_mayusculas= cadena1.upper ()
print(cadena1)
print (cadena1_en_mayusculas)
cadena1_en_minusculas= cadena1.lower ()
cadena1_en_modo_titulo= cadena1.title ()
print (cadena1_en_modo_titulo)
cadena1_en_modo_pararfo= cadena1.capitalize ()
print (cadena1_en_modo_pararfo)
print (cadena1.count (" "))
print (cadena1.find ("  "))
print (cadena1.find (" "))
print (cadena1.find ("i"))
print (cadena1.rfind ("  "))
print (cadena1.rfind (" "))
print (cadena1.rfind ("i"))
lista= ["segunda", "cadena", "al" ,"rescate"]
cadena= "<><><>solito<><><>". join (lista)
print (cadena)
password= input ("ingrese su password :")
print (password.strip ( ))
palabra_repetida = "cadena_cadena_cadena_cadena"
palabra_repetida_modificada = palabra_repetida .replace ("cadena", "otra", 3)
print (palabra_repetida)
print (palabra_repetida_modificada)
lista3 = [1, 8, 2,9,3]
lista3.sort (reverse= True)
print (lista3)
Auto= {"motor": "V8" , 
       "color" : "negro",
       "vidrios": (6 ,"blindadas"),
       "pasajeros": 4}


print (Auto.keys())
print (Auto.values())
print (Auto.items())

conjunto1=   {1, "valor1", (1,True) } 
iterable1 = (1,"valor1", (1,True), 45)   
print (conjunto1.intersection_update (iterable1))
    