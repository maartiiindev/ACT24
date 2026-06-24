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