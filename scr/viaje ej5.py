
simulacion = "s"
while simulacion == "s":
    distancia_km = input("Introduzca la distancia en Km: ") #distancia tierra-luna
    distancia_km = int(distancia_km)
    velocidad_kmh = input("Introduzca la distancia en km/h: ")
    velocidad_kmh = int(velocidad_kmh)
    tiempo_horas = distancia_km/velocidad_kmh
    tiempo_dias = tiempo_horas/24
    print(f"Tardarías{tiempo_dias} dias en llegar.")
    simulacion = input("Quieres hacer otra simulación? (s/n)").lower() #lower sirve para poner todo en minúscula
