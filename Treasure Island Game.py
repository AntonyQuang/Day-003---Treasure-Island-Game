print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice_1 = input("You reach a fork on the road. Which way do you go? Type \"left\" or \"right\". \n").lower()

if choice_1 == "left": 
    choice_2 = input("You eventually reach a river, the water looks calm and a sign says that a boat will arrive in 1 hour.\nWhat will you do? Tpye \"swim\" or \"wait?\" \n").lower()
    if choice_2 == "wait":
        choice_3 = input("You safely take the boat across.\nYou now stand before three doors: red, blue, and yellow.\nWhich do you open? Type \"blue\", \"red\" or \"yellow\" \n").lower()
        if choice_3 == "red":
            print("The red door opens to a room of fire that engulfs you, reducing you to ashes. \n GAME OVER.")
        elif choice_3 == "blue":
            print("Behind the blue door is a horde of beasts that tear you limb from limb. \nGAME OVER.")
        elif choice_3 == "yellow":
            print("Behind the yellow door lies...a Nintendo 64! What a treasure!\nThank you for playing!")
        else:
            print("A trap suddenly activates and you are skewered by spikes. \nGAME OVER.")
    else:
        print("You get attacked by a trout. With a knife. It hurts...\nGAME OVER.")
else:
    print("Your sense of direction has failed you as you fall into a hole. All that is heard from you is a splat.\nGAME OVER")
