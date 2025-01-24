import random
from clases import enemigo
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("Ingresa el nombre de tu jugador ")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15),
    ]

    enemigos_derrotados = []

    print("Comienza la aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        print(f"Te encuentrtas con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("Que de deseas hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"Has atacado al  {enemigo_actual.nombre} y le has causado {dano_jugador} de dano"
                )
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"{enemigo_actual.nombre} ta ataco y te causo {dano_enemigo} de dano"
                    )
                    jugador.recibir_dano(dano_enemigo)
            elif accion == "huir":
                print("Has decicido huir del combate")
                break
        
        if jugador.salud <= 0:
            print("Has perdido la partida!")
            break
        
        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input("Quieres seguir explorando (s/n)").lower()

        if continuar != "s":
            print("Gracias por haber jugado Batallas Galacticas")
            break
    if not enemigos:
        print("Felicidadez has derrotado a todos los enmigos")

if __name__ == "__main__":
    main()