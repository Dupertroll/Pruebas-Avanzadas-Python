#piedra = 1
#papel = 2
#tijera = 3
# Imports
import time
import random
# Inicio

comostas = input("Hola, ¿cómo estás?: ")
time.sleep(0.4)

print("Tampoco me importa, vamos a jugar piedra papel o tijera.")
time.sleep(1)

def game():
    altnum = random.randint(1, 3)
    eleccion = input("(Piedra, Papel o Tijera): ")

    # Juego

    # Piedra

    if(eleccion == "Piedra" or eleccion == "piedra"):
        if(altnum == 2):
            time.sleep(0.4)
            print("Yo elijo papel.")
            time.sleep(0.8)
            print("Perdiste")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()

        elif(altnum == 1):
            time.sleep(0.4)
            print("Yo elijo piedra.")
            time.sleep(0.8)
            print("Empate")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()
            
        
        elif(altnum == 3):
            time.sleep(0.4)
            print("Yo elijo tijera")
            time.sleep(0.8)
            print("Ganaste")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()

    # Papel  
        
    elif(eleccion == "papel" or eleccion == "Papel"):
        if(altnum == 2):
            time.sleep(0.4)
            print("Yo elijo papel.")
            time.sleep(0.8)
            print("Empate")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()
        
        elif(altnum == 1):
            time.sleep(0.4)
            print("Yo elijo piedra.")
            time.sleep(0.8)
            print("Ganaste")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()
        
        elif(altnum == 3):
            time.sleep(0.4)
            print("Yo elijo tijera.")
            time.sleep(0.8)
            print("Perdiste")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()

    # Tijera

    elif(eleccion == "tijera" or eleccion == " Tijera"):
        
        if(altnum == 2):
            time.sleep(0.4)
            print("Yo elijo papel.")
            time.sleep(0.8)
            print("Ganaste")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()
        
        elif(altnum == 1):
            time.sleep(0.4)
            print("Yo elijo piedra.")
            time.sleep(0.8)
            print("Perdiste")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()
        
        elif(altnum == 3):
            time.sleep(0.4)
            print("Yo elijo tijera.")
            time.sleep(0.8)
            print("Empate")
            again = input("¿Quíeres volver a jugar?: ")
            if(again == "si" or again == "sí" or again == "sÍ" or again == "Sí" or again == "Si" or again == "SÍ" or again == "SI" or again == "1"):
                game()

    # Huevos de pascua 🤑🤑🤑🤑

    elif eleccion.isdigit():
        print("Eres muy inteligente poniendo un número 🤑🤑🤑")

    else:
        print("Me pregunto que pusiste para llegar a este lugar 🤔🤔.")

if comostas.isdigit():
    print("Espera, es enserio?, te pregunto cómo estas y me respondes con un número, que poca humildad")
    time.sleep(1.3)
game()