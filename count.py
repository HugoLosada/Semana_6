num = 10
print("Tienes que intentar desactivar la bomba, el cantador va a empezar en 10 e irá bajando, además puede que en el medio se salte algunos números\nLos colores de los cables son:\namarillo\nlila\nmarrón\nazul\nverde\nnaranja\nnegro\nrojo\nSuerte!")
while num >= 0:
     if num == 0:
          print("La bomba ha explotado")
          break
     if 8 > num and  2 < num:
            print("---")
            num -=1
            continue
     cable = input("Que cable quieres cortar: ")
     print(num)
     num -=1
     if  cable.lower() == "verde":
          print("Te has salvado, has desactivado la bomba")
          break

     elif  cable.lower() == "rojo":
                print("La bomba ha explotado, has muerto")
                break


    
          
        
    
