import random

def concurso_puertas(num_simulaciones):
  """Simularemos el concurso de las tres puertas un número determinado de veces.

  Args:
    num_simulaciones: Número de veces que se simula el juego.

  Returns:
    Una tupla con el número de veces que se gana el coche cambiando de puerta y sin cambiar.
  """

  ganancias_cambiando = 0
  ganancias_sin_cambiar = 0

  for _ in range(num_simulaciones):
    # Inicializamos las puertas
    puertas = [0, 0, 1]  # 1 representa el coche
    random.shuffle(puertas)

    # Elegimos una puerta al azar
    eleccion_inicial = random.randint(0, 2)

    # El presentador abre una puerta con una cabra
    puertas_restantes = [i for i in range(3) if i != eleccion_inicial and puertas[i] == 0]
    puerta_abierta = random.choice(puertas_restantes)

    # Opción de cambiar de puerta
    eleccion_final = 2 - eleccion_inicial - puerta_abierta

    # Contabilizamos los resultados
    if puertas[eleccion_final] == 1:
      ganancias_cambiando += 1
    else:
      ganancias_sin_cambiar += 1

  return ganancias_cambiando, ganancias_sin_cambiar

# Ejecutamos la simulación 10,000 veces
resultados = concurso_puertas(10000)

# Imprimimos los resultados
print("Ganando al cambiar de puerta:", resultados[0], f"({resultados[0]/10000:.2%})")
print("Ganando sin cambiar de puerta:", resultados[1], f"({resultados[1]/10000:.2%})")