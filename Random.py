#imports
import random;
import time;

#variables
vidas = 8;
altnum = random.randint(1, 100);
while(vidas > 0):
        preguntar = input("What number from 1 to 100 do you think I am thinking of?: ");
        if preguntar.isdigit():
            preguntar = int(preguntar)
            # Win
            if(preguntar == altnum):
                print("Congratulations, you win.");
                break
            # Less
            elif(preguntar > altnum):
                time.sleep(0.3);
                print("Less");
                time.sleep(0.3);
            # More
            elif(preguntar < altnum):
                time.sleep(0.3);
                print("More");
                time.sleep(0.3);

            vidas -= 1;
            time.sleep(0.3);

            print("you have", (vidas), "lives left");
            time.sleep(0.3);

            if(vidas == 0):
                print("You have lost all your lives, the number I was thinking of was:", (altnum));
                break;
        else:
            print("You need to enter a number to continue")