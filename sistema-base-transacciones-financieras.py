operaciones=[]
lista_retiros=[]
retiros = 0
depositos = 0

while True:
    
    print("Deposito......1")
    print("Retiro........2")
    print("Salir.........3")
    i=input("¿Qué deseas hacer hoy?" )
    i=int(i)
    

    if i==1:
     operacion=input("¿Cuanto deseas depositar?")
     operacion= int(operacion)
     operaciones.append(operacion)
     depositos+=1
     print("")
    
    elif i==2:
     operacion=input("¿Cuanto deseas retirar?")
     operacion= int(operacion)
     operaciones.append(-operacion)
     retiros+=1
     print("")

    elif i==3:
     break

    else:
       print("Por favor elige una opcion valida")
       print("")


retirosmenores=0
balance = 0

for operacion in operaciones:
    balance= balance + operacion
    if operacion <-500:
       retirosmenores+=1
    if operacion <0:
      lista_retiros.append(operacion)



if len(operaciones)==0:
    print("No se realizó ningun movimiento")
else:
    promedio = balance/len(operaciones)
    
    if len(lista_retiros)>0:
        mayor_retiro=min(lista_retiros)
    else:
       mayor_retiro=0
    
    print("Balance total: $",balance)
    print("Número de depositos: ", depositos)
    print("Número de retiros: ", retiros)
    print("Promedio: $",promedio)
    print("Mayor retiro: $",-mayor_retiro)
    print("Retiros mayores a $500: ", retirosmenores)

    




