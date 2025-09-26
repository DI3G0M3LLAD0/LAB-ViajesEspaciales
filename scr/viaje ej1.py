distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")

#con una barra es decir: '/' sale el número con decimales como '2.3 , 4.5 , 5.9 , ...'
#con dos barras es decir: '//' sale el número entero como '1 , 2 , 3 , 4 , ...'