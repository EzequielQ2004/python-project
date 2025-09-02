import random

def jugar_piedra_papel_tijera():
    """
    Función principal que ejecuta el juego de Piedra, Papel o Tijera
    """
    # Opciones disponibles
    opciones = ["piedra", "papel", "tijera"]
    
    # Contadores de victorias
    victorias_jugador = 0
    victorias_computadora = 0
    empates = 0
    
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("Escribe 'piedra', 'papel' o 'tijera' para jugar.")
    print("Escribe 'salir' para terminar el juego.\n")
    
    while True:
        # Elección de la computadora
        eleccion_computadora = random.choice(opciones)
        
        # Elección del jugador
        eleccion_jugador = input("Tu elección: ").lower().strip()
        
        # Verificar si el jugador quiere salir
        if eleccion_jugador == "salir":
            break
        
        # Validar la entrada del jugador
        if eleccion_jugador not in opciones:
            print("Por favor, elige entre 'piedra', 'papel' o 'tijera'.\n")
            continue
        
        print(f"Computadora eligió: {eleccion_computadora}")
        
        # Determinar el resultado
        if eleccion_jugador == eleccion_computadora:
            print("¡Empate!")
            empates += 1
        elif (
            (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or
            (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
            (eleccion_jugador == "tijera" and eleccion_computadora == "papel")
        ):
            print("¡Ganaste esta ronda!")
            victorias_jugador += 1
        else:
            print("¡La computadora gana esta ronda!")
            victorias_computadora += 1
        
        print(f"Marcador - Tú: {victorias_jugador}, Computadora: {victorias_computadora}, Empates: {empates}\n")
    
    # Mostrar resultados finales
    print("\n" + "="*40)
    print("RESULTADOS FINALES:")
    print(f"Victorias tuyas: {victorias_jugador}")
    print(f"Victorias de la computadora: {victorias_computadora}")
    print(f"Empates: {empates}")
    
    if victorias_jugador > victorias_computadora:
        print("¡Felicidades, ganaste el juego!")
    elif victorias_computadora > victorias_jugador:
        print("La computadora ganó el juego.")
    else:
        print("El juego terminó en empate.")
    print("="*40)

# Versión alternativa más simple (una sola ronda)
def jugar_una_ronda():
    """
    Versión simplificada para una sola ronda
    """
    opciones = ["piedra", "papel", "tijera"]
    
    eleccion_computadora = random.choice(opciones)
    eleccion_jugador = input("Elige piedra, papel o tijera: ").lower().strip()
    
    if eleccion_jugador not in opciones:
        return "Elección no válida"
    
    print(f"Computadora eligió: {eleccion_computadora}")
    
    if eleccion_jugador == eleccion_computadora:
        return "¡Empate!"
    elif (
        (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or
        (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
        (eleccion_jugador == "tijera" and eleccion_computadora == "papel")
    ):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

# Ejecutar el juego completo
if __name__ == "__main__":
    jugar_piedra_papel_tijera()
    
    # Para jugar solo una ronda, descomenta la línea siguiente:
    # print(jugar_una_ronda())