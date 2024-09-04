import random

tablero1=[]
tablero2=[]

def generar_tablero1(): # Función para crear el tablero
    row, col=5, 5
    for _ in range(row): 
        tablero1.append(["~"] * col)

def generar_tablero2(): # Función para crear el tablero 2
    row, col=5, 5
    for _ in range(row): 
        tablero2.append(["~"] * col) 

def mostrar_tablero1(): # Función para mostrar el tablero
    print("Datos del tablero 1:")
    print()
    for i in tablero1: 
        print(i)
    print()
    print()

def mostrar_tablero2(): # Función para mostrar el tablero 2
    print("Datos del tablero 2:")
    print()
    for i in tablero2: 
        print(i)
    print()
    print()

def poner_barcos_jugador1(): # Función para poner los barcos del jugador 1
    cantidad_barcos=5
    for i in range(1, cantidad_barcos + 1): 
        while True: 
            x, y = map(int, input(f"Por favor, jugador 1 ingrese las coordenadas X e Y del barco {i}, separadas por un espacio: ").split())
            if x < 5 and y < 5: 
                if tablero1[y][x] == "~": 
                    tablero1[y][x]="1" 
                    break 
                else:
                    print()
                    print("¡Ya se ha desplegado una unidad en esta posición!") 
                    print()
                    mostrar_tablero1()
                    print()
            else:
                print()
                print("¡La coordenada ingresada está por fuera del área!") 
                print()
                mostrar_tablero1()
                print()
    print("Así ha desplegado sus unidades JUGADOR 1:")
    print()
    mostrar_tablero1()

def poner_barcos_jugador2(): # Función para poner los barcos del jugador 2
    cantidad_barcos=5
    for i in range(1, cantidad_barcos + 1): 
        while True: 
            x, y = map(int, input(f"Por favor, jugador 2 ingrese las coordenadas X e Y del barco {i}, separadas por un espacio: ").split())
            if x < 5 and y < 5: 
                if tablero2[y][x] == "~": 
                    tablero2[y][x]="2" 
                    break 
                else:
                    print()
                    print("¡Ya se ha desplegado una unidad en esta posición!") 
                    print()
                    mostrar_tablero2()
                    print()
            else:
                print()
                print("¡La coordenada ingresada está por fuera del área!") 
                print()
                mostrar_tablero2()
                print()
    print("Así ha desplegado sus unidades JUGADOR 2:")
    print()
    mostrar_tablero2()

def poner_barcos_computadora(): # Función para poner los barcos de la computadora
    cantidad_barcos=5
    for i in range(cantidad_barcos):
        while True:
            x=random.randint(0, 4)
            y=random.randint(0, 4)
            if x < 5 and y < 5:
                if tablero2[y][x] != "2":
                    tablero2[y][x]="2"
                    break

def juego_contra_computadora(): # Función para iniciar el juego contra la computadora
    unidades_jugador1=0
    unidades_jugador2=0

    while True:
        unidades_jugador1=0
        unidades_jugador2=0
        for area in tablero1:
            for barco in area:
                if barco == "1":
                    unidades_jugador1+=1
        for area in tablero2:
            for barco in area:
                if barco == "2":
                    unidades_jugador2+=1
                
        if unidades_jugador1 == 0:
            print("Haz PERDIDO, la computadora ha hundido todos tus barcos")
            print()
            break
        elif unidades_jugador2 == 0:
            print("FELICIDADES, ¡Has ganado el juego!")
            print()
            break
        
        print("¡Turno computadora!")
        while True:
            x=random.randint(0, 4)
            y=random.randint(0, 4)
            if x < 5 and y < 5:
                if tablero1[y][x] == "1":
                    print()
                    print(f"¡La computadora ha elegido {x},{y} y ha ACERTADO en un objetivo!")
                    unidades_jugador1-=1
                    tablero1[y][x]="~"
                    break
                else:
                    print()
                    print(f"¡La computadora ha elegido {x},{y} y ha FALLADO!")
                    break
            else:
                print()
                print("¡Las coordenadas ingresadas están por fuera del área!")
                print()
        print()            
        print("¡Tu turno!")
        print()
        while True:
            x, y = map(int, input(f"Por favor ingrese las coordenadas X e Y del objetivo, separadas por un espacio: ").split())
            print()
            if x < 5 and y < 5:
                if tablero2[y][x] == "2":
                    print("¡Haz ACERTADO en un objetivo!")
                    print()
                    unidades_jugador2-=1
                    tablero2[y][x]="~"
                    break
                else:
                    print("¡Haz FALLADO!")
                    print()
                    break
            else:
                print("¡Las coordenadas ingresadas están por fuera del área!")
                print()

        print(f"Unidades Jugador: {unidades_jugador1} | Unidades Computadora: {unidades_jugador2}")
        print()

def juego_contra_jugador(): # Función para iniciar el juego contra otro jugador
    unidades_jugador1=0
    unidades_jugador2=0

    while True:
        unidades_jugador1=0
        unidades_jugador2=0
        
        for area in tablero1:
            for barco in area:
                if barco == "1":
                    unidades_jugador1+=1
        for area in tablero2:
            for barco in area:
                if barco == "2":
                    unidades_jugador2+=1

        if unidades_jugador2 == 0:
            print("FELICIDADES, ¡jugador 1 ha ganado!")
            print()
            break
        elif unidades_jugador1 == 0:
            print("FELICIDADES, ¡jugador 2 ha ganado!")
            print()
            break
        
        print()
        print("¡Turno Jugador 1!")
        print()
        while True:
            x, y = map(int, input(f"Por favor ingrese las coordenadas X e Y del objetivo, separadas por un espacio: ").split())
            if x < 5 and y < 5:
                if tablero2[y][x] == "2":
                    print()
                    print("¡Jugador 1 ha ACERTADO en un objetivo!")
                    unidades_jugador2-=1
                    tablero2[y][x]="~"
                    break
                else:
                    print()
                    print("¡Jugador 1 ha FALLADO!")
                    break
            else:
                print()
                print("¡Las coordenadas ingresadas están por fuera del área!")
                print()
        print()            
        print("¡Turno Jugador 2!")
        print()
        while True:
            x, y = map(int, input(f"Por favor ingrese las coordenadas X e Y del objetivo, separadas por un espacio: ").split())
            print()
            if x < 5 and y < 5:
                if tablero1[y][x] == "1":
                    print("¡Jugador 2 ha ACERTADO en un objetivo!")
                    print()
                    unidades_jugador1-=1
                    tablero1[y][x]="~"
                    break
                else:
                    print("¡Jugador 2 ha FALLADO!")
                    print()
                    break
            else:
                print("¡Las coordenadas ingresadas están por fuera del área!")
                print()

        print(f"Unidades Jugador 1: {unidades_jugador1} | Unidades Jugador 2: {unidades_jugador2}")
        print()

def menu_juego():
    while True:
        print()
        print("- - - - - ¡Bienvenido a Batalla Naval! - - - - -")
        print()
        print("1. Contra la Computadora\n2. Dos Jugadores\n3. Salir")
        print()
        opcion=int(input("Por favor seleccione un modo de juego: "))
        print()
        if opcion == 1:
            print("¡Juego contra la computadora!")
            print()
            generar_tablero1()
            poner_barcos_jugador1()
            print()
            generar_tablero2()
            poner_barcos_computadora()
            print()
            print("* * * Inicio del juego * * *")
            print()
            juego_contra_computadora()
            mostrar_tablero1()
            mostrar_tablero2()
        elif opcion == 2:
            print("¡Juego a dos jugadores!")
            print()
            tablero1.clear()
            tablero2.clear()
            generar_tablero1()
            generar_tablero2()
            poner_barcos_jugador1()
            poner_barcos_jugador2()
            print()
            print("* * * Inicio del juego * * *")
            print()
            juego_contra_jugador()
            print()
            mostrar_tablero1()
            mostrar_tablero2()
        elif opcion == 3:
            break
        else:
            print("¡La opción seleccionada es incorrecta!")

menu_juego()