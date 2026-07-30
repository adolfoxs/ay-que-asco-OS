import random
import os
import time as tm
import sys
# alias para el código provisto
rm = random
# Moneda del sistema (comienzas con 1 al prender el OS)
ascoins = 1.0
secret_unlocked = False
bono_secreto_activo = False

def check_unlock():
    global secret_unlocked, ascoins, bono_secreto_activo
    # umbral reducido a 30 ascoins
    if not secret_unlocked and ascoins >= 30:
        secret_unlocked = True
        bono_secreto_activo = True
        print("¡Has desbloqueado el Bono Secreto! Cada victoria futura te dará +3 ascoins extra.")


def otorgar_recompensa(base_reward):
    global ascoins, bono_secreto_activo
    ascoins += base_reward
    if bono_secreto_activo:
        ascoins += 3
        print("Bono secreto activado: +3 ascoins extra.")
    print(f"Has ganado {base_reward + (3 if bono_secreto_activo else 0)} ascoins. Saldo: {ascoins}")

def initial():
    print("hola bienvenido a ay que asco OS")
    print("porfavor ingrese su su contraseña para continuar o escriba 'apagar' para apagar ay que asco OS")
    contraseña = "ay que asco"
    contraseña_ingresada = input("Ingrese su contraseña: ")
    if contraseña_ingresada.strip().lower() == "apagar":
        print("apagando ay que asco OS")
        sys.exit()
    # Comprobar contraseña principal o contraseña especial para GatutusOS
    if contraseña_ingresada == contraseña:
        print("contraseña correcta")
        print("bienvenido a ay que asco OS")
        return menu()
    if contraseña_ingresada.strip().lower() == "ay que gatutus":
        print("Abriendo GatutusOS...")
        tm.sleep(0.5)
        try:
            import runpy, os as _os
            path = _os.path.join(_os.path.dirname(__file__), "gatututsOS.PY")
            runpy.run_path(path, run_name="__main__")
        except Exception as e:
            print("Error al abrir GatutusOS:", e)
        # Volver al inicio de sesión
        return initial()
    else:
        print("contraseña incorrecta")
        print("reiniciando ay que asco OS")
        return initial()


def jugar_adivinanza():
    numero_secreto = random.randint(1, 20)
    intentos = 0

    print("Estoy pensando en un número entre 1 y 20.")
    print("Intenta adivinarlo.")

    while True:
        intento_raw = input("Tu número (o escribe 'salir' para volver): ").strip()
        if intento_raw.lower() == 'salir':
            print(f"El número secreto era: {numero_secreto}")
            print("Volviendo al menú principal")
            return
        if not intento_raw.isdigit():
            print("Por favor escribe un número válido o 'salir'.")
            continue

        intentos += 1
        intento = int(intento_raw)

        if intento < numero_secreto:
            print("Muy bajo. Intenta otra vez.")
        elif intento > numero_secreto:
            print("Muy alto. Intenta otra vez.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            try:
                otorgar_recompensa(5)
                check_unlock()
            except Exception:
                pass
            break


def jugar_cachipun():
    opciones = ["piedra", "papel", "tijera"]
    print("Juego: Piedra, Papel o Tijera. Escribe 'salir' para volver al menú.")
    def normalizar(s):
        s = s.replace('\u00A0', ' ')
        s = ''.join(ch for ch in s if ch.isalpha() or ch.isspace())
        return s.strip().lower()

    while True:
        eleccion = normalizar(input("Tu elección: "))
        if eleccion == "salir":
            print("Volviendo al menú principal")
            return
        if eleccion not in opciones:
            print("Opción no válida. Elige piedra/papel/tijera o 'salir'.")
            continue
        oponente = random.choice(opciones)
        print(f"oponente eligió: {oponente}")
        if eleccion == oponente:
            print("Empate.")
        elif (eleccion == "piedra" and oponente == "tijera") or \
             (eleccion == "papel" and oponente == "piedra") or \
             (eleccion == "tijera" and oponente == "papel"):
            print("¡Ganaste!")
            try:
                otorgar_recompensa(2)
                check_unlock()
            except Exception:
                pass
        else:
            print("Perdiste.") 
            try:
                ascoins -= 1
            except Exception:
                pass
            try:
                check_unlock()
            except Exception:
                pass

def jugar_ahorcado():
    palabras = ["gato", "perro", "python", "programa", "computadora", "raton", "teclado", "pantalla", "desarrollo", "juego"]
    palabra = rm.choice(palabras).lower()
    letras_adivinadas = set()
    intentos = 10

    print("Juego: Ahorcado. Escribe 'salir' para volver al menú.")
    while True:
        display = ' '.join([c if c in letras_adivinadas else '_' for c in palabra])
        print("Palabra:", display)
        if '_' not in display:
            print("¡Felicidades! Adivinaste la palabra:", palabra)
            return
        print("Intentos restantes:", intentos)
        entrada = input("Adivina una letra o la palabra completa: ").strip().lower()
        if entrada == 'salir':
            print("Volviendo al menú principal")
            return
        if entrada == '':
            continue
        if len(entrada) == 1:
            if not entrada.isalpha():
                print("Introduce una letra válida.")
                continue
            if entrada in letras_adivinadas:
                print("Ya intentaste esa letra.")
                continue
            if entrada in palabra:
                letras_adivinadas.add(entrada)
                print("¡Bien! Letra correcta.")
            else:
                intentos -= 1
                print("Letra incorrecta.")
        else:
            if entrada == palabra:
                print("¡Correcto! Has adivinado la palabra:", palabra)
                try:
                    otorgar_recompensa(10)
                    check_unlock()
                except Exception:
                    pass
                return
            else:
                intentos -= 1
                print("Palabra incorrecta.")

        if intentos <= 0:
            print("Te quedaste sin intentos. La palabra era:", palabra)
            try:
                ascoins -= 5
            except Exception:
                pass
            print(f"Perdiste 5 ascoins. Saldo: {ascoins}")
            return

def jugar_gatutu():
    print("Bienvenido a Gatutu-Domination!")
    tm.sleep(1)
    print("Tienes que crear un virus para que los humanos se extingan y los gatos tomen lugar.")
    tm.sleep(1)
    print("[#Pon enter para continuar#]")
    input()
    # Limpiar pantalla (compatible con Windows y Unix)
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

    print("Nombra tu virus:")
    name = input()
    while len(name) > 16:
        print("No puedes superar los 16 caracteres, trata de reducir las letras!")
        name = input()

    # Reducir la población inicial para que la partida sea jugable
    personas = 100000
    infectados = 0
    gatutumonedas = 10.0
    arg = ""
    gravedad = 1
    infectividad = 1
    cura = 0
    estado_desc = ""
    descubierto = False

    while True:
        print("Descubierto:", estado_desc)
        print("Personas:", int(personas))
        print("Infectados:", int(infectados))
        print("Gravedad:", gravedad)
        print("Gatutu Monedas *:", gatutumonedas)
        print("Opciones: 1 = Mejorar a", name, "2 = Info detallada 3 = Salir al menú")
        print("Actualiza esta informacion poniendo enter (o escribe 'salir')")
        op = input()
        if op == "1":
            print("¿Que quieres mejorar? 1. Gravedad, cuesta 50 Gatutu Monedas 2. Infectividad, cuesta 10 Gatutu Monedas")
            op2 = input()
            if op2 == "2":
                print("Seguro? S/n")
                arg = input().lower()
                if arg == "s":
                    if gatutumonedas >= 10:
                        print("Comprado!")
                        infectividad = infectividad + 1
                        gatutumonedas = gatutumonedas - 10
                    else:
                        print("Insuficientes Gatutu Monedas.")
                else:
                    print("Abortado")
            elif op2 == "1":
                if gatutumonedas >= 50:
                    print("Seguro? S/n")
                    arg = input().lower()
                    if arg == "s":
                        print("Comprado!")
                        gatutumonedas = gatutumonedas - 50
                        gravedad = gravedad + 1
                    else:
                        print("Abortado")
                else:
                    print("insuficientes Gatutu Monedas.")
        if op == "2":
            print(name)
            print("Bacteria")
            print("Infectividad:", infectividad)
            print("Gravedad:", gravedad)
            print("[-|---------|-]")
            print("Infectados")
            print("[#", int(infectados), "#]")

        # Opción para salir al menú principal
        if isinstance(op, str) and (op.strip().lower() == "3" or op.strip().lower() == "salir" or op.strip().lower() == "exit" or op.strip().lower() == "q"):
            print("Saliendo al menú principal...")
            return

        # Lógica de infectados y ganancias
        if gravedad >= 1:
            personas = personas - 0
        if infectividad == 1:
            infectados = infectados + rm.randrange(1, 14)
            gatutumonedas = gatutumonedas + 0.2
        if infectividad >= 2:
            infectados = infectados + rm.randrange(14, 50)
            gatutumonedas = gatutumonedas + 0.5
        if infectividad >= 4:
            infectados = infectados + rm.randrange(50, 1000)
            gatutumonedas = gatutumonedas + 3
        if infectividad >= 7:
            infectados = infectados + rm.randrange(1000, 1000000)
            gatutumonedas = gatutumonedas + 13

        # Evitar que infectados supere al total de personas
        if infectados > personas:
            infectados = int(personas)

        # Efecto de la gravedad sobre personas y posibilidad de cura
        if gravedad == 2:
            personas = personas - infectados / 20
            probabilidad_desc = rm.randrange(1, 1050)
            if probabilidad_desc == 1:
                cura = 1
        if gravedad >= 3:
            personas = personas - infectados / 15
            probabilidad_desc = rm.randrange(1, 100)
            if probabilidad_desc == 1:
                cura = 2
        if gravedad >= 5:
            personas = personas - infectados / 10
            probabilidad_desc = rm.randrange(1, 150)
            if probabilidad_desc == 1:
                cura = 3
        if gravedad >= 10:
            personas = personas - infectados / 2
            probabilidad_desc = rm.randrange(1, 15)
            if probabilidad_desc == 1:
                cura = 4

        # Aplicar efecto de una cura si ocurre
        if cura == 1:
            infectados = infectados - rm.randrange(100, 1000)
        elif cura == 2:
            infectados = infectados - rm.randrange(1000, 10000)
        elif cura == 3:
            infectados = infectados - rm.randrange(10000, 100000)
        elif cura == 4:
            infectados = infectados - rm.randrange(500000, 930000)

        # Si hubo cura, marcar descubierto y luego resetear cura (aplicar una vez)
        if cura > 0:
            descubierto = True
            cura = 0

        # Evitar valores negativos y límites lógicos
        if infectados < 0:
            infectados = 0
        if personas < 0:
            personas = 0

        estado_desc = "Si" if descubierto else "No"

        # Comprobar condición de victoria: si no quedan personas o los infectados alcanzan la población
        if personas <= 0 or (personas > 0 and infectados >= personas):
            personas = 0
            # Recompensa por victoria
            try:
                otorgar_recompensa(20)
                check_unlock()
            except Exception:
                pass
            print("Felicidades! Has exterminado a la humanidad y los gatos han tomado el control del mundo!")
            print("Has recibido 20 ascoins por la victoria. Saldo actual:", ascoins)
            print("--- Resumen final ---")
            print("Personas:", int(personas))
            print("Infectados:", int(infectados))
            print("Gatutu Monedas:", gatutumonedas)
            print("Gracias por jugar Gatutu-Domination!")
            # Pedir la frase mágica para continuar
            while True:
                entrada_final = input("Escribe 'ay que asco' para volver al menú: ").strip()
                if entrada_final.lower() == "ay que asco":
                    print("Frase correcta. Volviendo al menú principal...")
                    break
                else:
                    print("Frase incorrecta. Intenta de nuevo.")
            return

        # Si te descubren, mostrar mensaje de derrota y submenú de opciones
        if descubierto:
            print("Has perdido! Te han descubierto.")
            while True:
                print("que desea hacer ahora?")
                print("1. volver a jugar")
                print("2. salir del juego y apagar ay que asco OS")
                print("3. salir al menu principal")
                selection = input()
                if selection == "1":
                    jugar_gatutu()
                    return
                elif selection == "2":
                    print("saliendo del juego y apagando ay que asco OS")
                    sys.exit()
                elif selection == "3":
                    print("saliendo al menu principal")
                    return
                else:
                    print("Opción no válida.")


def jugar_carreras_gatos():
    print("Bienvenido a Carreras de Gatos!")
    print("Escribe 'salir' en cualquier momento para volver al menú.")
    global ascoins
    print(f"Saldo actual de ascoins: {ascoins}")
    # Número de corredores
    while True:
        num_raw = input("¿Cuántos gatos correrán? (3-8, defecto 5): ").strip()
        if num_raw.lower() == 'salir':
            print("Volviendo al menú principal")
            return
        if num_raw == '':
            num = 5
            break
        if not num_raw.isdigit():
            print("Por favor introduce un número válido.")
            continue
        num = int(num_raw)
        if 3 <= num <= 8:
            break
        print("Elige un número entre 3 y 8.")

    gatos = [f"Gato{ i+1 }" for i in range(num)]
    print("Gatos participantes:", ', '.join(gatos))

    # Apuesta del usuario
    while True:
        apuesta = input(f"A qué gato apuestas? (1-{num}) o nombre: ").strip().lower()
        if apuesta == 'salir':
            print("Volviendo al menú principal")
            return
        if apuesta.isdigit():
            idx = int(apuesta) - 1
            if 0 <= idx < num:
                apuesta_idx = idx
                break
        else:
            # intentar emparejar por nombre
            for i, g in enumerate(gatos):
                if apuesta == g.lower():
                    apuesta_idx = i
                    break
            else:
                print("Gato no válido. Intenta de nuevo.")
                continue
            break

    print(f"Has apostado a: {gatos[apuesta_idx]}")
    # Apuesta del usuario
    while True:
        bet_raw = input(f"Cuántos ascoins quieres apostar? (saldo {ascoins}): ").strip()
        if bet_raw.lower() == 'salir':
            print("Volviendo al menú principal")
            return
        try:
            bet = float(bet_raw)
        except Exception:
            print("Introduce una cantidad válida.")
            continue
        if bet <= 0:
            print("La apuesta debe ser mayor que 0.")
            continue
        if bet > ascoins:
            print("No tienes suficientes ascoins.")
            continue
        break

    print("Preparando carrera...")
    tm.sleep(0.8)

    # Estado de la carrera: posiciones (distancia)
    posiciones = [0] * num
    meta = 50
    ganador = None
    while ganador is None:
        for i in range(num):
            posiciones[i] += rm.randint(1, 6)
            if posiciones[i] >= meta:
                ganador = i
                break
        # Mostrar progreso simple
        line = ' | '.join(f"{g}: {min(p, meta)}/{meta}" for g, p in zip(gatos, posiciones))
        print(line)
        tm.sleep(0.2)

    print(f"¡El ganador es {gatos[ganador]}!")
    if ganador == apuesta_idx:
        # Ganancia simple: recuperas la apuesta y ganas la misma cantidad
        ascoins += bet
        if bono_secreto_activo:
            ascoins += 3
            print("Bono secreto activado: +3 ascoins extra.")
        print("¡Felicidades, ganaste la apuesta!")
        try:
            check_unlock()
        except Exception:
            pass
    else:
        ascoins -= bet
        print("Perdiste la apuesta. Mejor suerte la próxima.")
        try:
            check_unlock()
        except Exception:
            pass
    print(f"Saldo actualizado de ascoins: {ascoins}")
    return


def funcion_secreta():
    global secret_unlocked
    if not secret_unlocked:
        print("La función secreta está bloqueada. Consigue 30 ascoins para desbloquearla.")
        return
    print("Función secreta desbloqueada. Escribe la cadena que quieres que repita:")
    texto = input("Texto: ")
    if texto.strip().lower() == 'salir':
        print("Volviendo al menú principal")
        return
    while True:
        veces_raw = input("Cuántas veces repetir? (número, 'salir' para cancelar): ").strip()
        if veces_raw.lower() == 'salir':
            print("Cancelado. Volviendo al menú principal")
            return
        if not veces_raw.isdigit():
            print("Introduce un número válido.")
            continue
        veces = int(veces_raw)
        break
    for _ in range(veces):
        print(texto)
    return


def menu():
    while True:
        # Construir menú dinámico
        opciones = [
            ("jugar ay que asco game", jugar_adivinanza),
            ("jugar cachipun", jugar_cachipun),
            ("jugar ahorcado", jugar_ahorcado),
            ("jugar Gatutu-Domination", jugar_gatutu),
            ("jugar Carreras de Gatos", jugar_carreras_gatos),
        ]
        if secret_unlocked:
            opciones.append(("Función secreta", funcion_secreta))
        opciones.append(("apagar ay que asco OS", None))

        print("que desea hacer?")
        print(f"Saldo ascoins: {ascoins}")
        for i, (label, _) in enumerate(opciones, start=1):
            print(f"{i}. {label}")

        choice = input().strip()
        if not choice.isdigit():
            print("Opción no válida.")
            continue
        idx = int(choice) - 1
        if idx < 0 or idx >= len(opciones):
            print("Opción no válida.")
            continue

        label, action = opciones[idx]
        if action is None:
            print("apagando ay que asco OS")
            return

        # Llamar a la acción seleccionada
        if action == jugar_adivinanza:
            print("abriendo ay que asco game")
            jugar_adivinanza()
            # Submenú tras adivinanza
            while True:
                print("que desea hacer ahora?")
                print("1. volver a jugar")
                print("2. salir del juego y apagar ay que asco OS")
                print("3. salir al menu principal")
                selection = input()
                if selection == "1":
                    jugar_adivinanza()
                elif selection == "2":
                    print("saliendo del juego y apagando ay que asco OS")
                    return
                elif selection == "3":
                    print("saliendo al menu principal")
                    break
                else:
                    print("Opción no válida.")
        else:
            # otras acciones
            action()
if __name__ == "__main__":
    initial()
