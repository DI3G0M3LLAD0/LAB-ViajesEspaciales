distancia_km = int(input("Introduzca la distancia en Km"))  # distancia Tierra - Luna
velocidad_kmh = int(input("Introduca la velocidad en Km/h"))
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")