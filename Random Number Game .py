#imports
import random;
import time;

#variables
vidas = 5;
altnum = random.randint(0, 100);
while(vidas > 0):
        preguntar = input("¿En que número del 1 al 100 crees que estoy pensando?: ");
        if preguntar.isdigit():
            preguntar = int()
            if(preguntar == altnum):
                print("Ganaste, felicidades");
                break
            elif(preguntar > altnum):
                time.sleep(0.3);
                print("menos");
                time.sleep(0.3);
            elif(preguntar < altnum):
                time.sleep(0.3);
                print("mas");
                time.sleep(0.3);
            vidas -= 1;
            time.sleep(0.3);
            print("te quedan", (vidas));
            time.sleep(0.3);
            if(vidas == 0):
                print("Has perdido todas tus vidas, el número en el que estaba pensando era:", (altnum));
                break;
        else:
            print("Es necesario que coloques un número para continuar")