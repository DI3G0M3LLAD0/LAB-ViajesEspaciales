km = 225000000

for velocidad in range(10000,50001,10000):
    tiempo_horas = km/velocidad
    tiempo_dias = tiempo_horas/24
    print("Velocidad:",velocidad,"Km/h -> Tiempo:",tiempo_dias)