def viajar(edad, nivel_fisico):
    if edad <= 18:
        return ("Debes ser mayor de edad")
    
    elif nivel_fisico <=5:
        return ("Debes de estar en mejor forma")
        
    else:
        return ("Listo para despegar")

edad= int(input("Introduce tu edad:"))
nivel_fisico= int(input("Introduce tu nivel fisico(1-10):"))
print(viajar(edad, nivel_fisico))
    