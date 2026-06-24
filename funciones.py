personajes = []

def buscar(nombre):
    for i in range(len(personajes)):
        if personajes[i]["nombre"] == nombre:
            return i
    return -1

def agregar(nombre, clase, nivel):
    #validar
    if len(nombre.strip())==0 or len(nombre.strip())>20:
        print("Nombre no válido")
        return
    elif buscar(nombre)>=0:
        print("El nombre ya existe")
        return
    elif clase not in ("Guerrero", "Mago", "Pícaro"):
        print("Clase no válida, debe ser Guerrero, Mago, o pícaro")
        return
    elif nivel<=0 or nivel>50:
        print("El nivel debe estar entre 1 y 50")
        return
    #registrar
    rango = "Recluta"
    if nivel>=30: rango = "Élite"
    pj = {"nombre":nombre,"clase":clase,"nivel":nivel,"rango":rango}
    personajes.append(pj)
    print("Personaje registrado")

def mostrar(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        print(f"Personaje encontrado : {personajes[posicion]}")
    else:
        print("Nombre no existente")

def listar():
    if len(personajes)>0:
        print(f"{"N°":<3}.- {"Nombre":<20} {"Clase":<10} {"Nivel":<4} {"Rango":<10}")
        for i in range(len(personajes)):
            print(f"{i+1:<3}.- {personajes[i]["nombre"]:<15} {personajes[i]["clase"]:<10} {personajes[i]["nivel"]:<4} {personajes[i]["rango"]:<10}")
    else:
        print("No hay personajes registrados")

def eliminar(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        personajes.remove(personajes[posicion])
        print("Personaje eliminado")
    else:
        print("Personaje no existente")

def subir_nivel(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        nivel = personajes[posicion]["nivel"]
        if nivel < 50:
            personajes[posicion]["nivel"] = nivel+1
            print("Nivel aumentado")
            if nivel >= 30:
                personajes[posicion]["rango"] = "Élite"
        else:
            print("Ya ha alcanzado el nivel máximo")
    else:
        print("Personaje no existente")