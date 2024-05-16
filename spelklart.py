

import random # Import the random module for generating random values

def health(a, b): # Define a function to generate random health points within a specified range
    health = []
    for i in range(a, b+1):
        health.append(i)
    return (random.choice(health))  # Return a random value from the health list

def damage(a, b):  # Define a function to generate random damage points within a specified range
    damage = []
    for i in range(a, b+1):
        damage.append(i)
    return (random.choice(damage))

class Vapen(): # Define a class for weapons
    def __init__(self, v_hp, v_str, v_namn):
        self.v_namn = v_namn
        self.v_hp = v_hp
        self.v_str = v_str

# Define a class for characters
class Karaktärer():
    def __init__(self, p_hp, p_str, p_lvl, p_lvlpoäng, p_namn, vapen):
        self.p_hp = p_hp
        self.p_str = p_str
        self.p_lvl = p_lvl
        self.p_lvlpoäng = p_lvlpoäng
        self.p_namn = p_namn
        self.vapen = vapen
# Define a class for monsters
class Drake():
    def __init__(self, m_hp, m_str, m_namn):
        self.m_namn = m_namn
        self.m_hp = m_hp
        self.m_str = m_str
# String representation of a monster
    def __str__(self):
        return f"Du stöter på en {self.m_namn}, den har {self.m_hp} hp och {self.m_str} styrka"
# Define a function to generate monsters for phase 1
def drakegenerator_fas1():
    drake = random.randint(1, 2)
    Fire = Drake(health(4, 11), damage(2, 6), "Fire")
    Golum = Drake(health(3, 7), damage(3, 8), "Golum")
    if drake == 1:
        drake_stats = (Fire)
        return (drake_stats)
    elif drake == 2:
        drake_stats = (Golum)
        return (drake_stats)
# Define a function to generate monsters for phase 2
def drakegenerator_fas2():
    drake = random.randint(1, 2)
    Lycan = Drake(health(6, 12), damage(4, 9), "Lycan")
    Golem = Drake(health(12, 17), damage(3,3), "Golem")
    if drake == 1:
        drake_stats = (Lycan)
        return (drake_stats)
    elif drake == 2:
        drake_stats = (Golem)
        return (drake_stats)
# Define a function to generate monsters for phase 3
def drakegenerator_fas3():
    drake = random.randint(1, 2)
    Undead = Drake(health(15, 22), damage(4, 5), "Undead")
    Orc = Drake(health(9, 15), damage(6, 10), "Orc")
    if drake == 1:
        drake_stats = (Undead)
        return (drake_stats)
    elif drake == 2:
        drake_stats = (Orc)
        return (drake_stats)
# Initialize weapons for players
Start = Vapen(0, 0, "en rutten pinne")
# Initialize characters with their respective weapons
Legolas = Karaktärer(8, 10, 0, 0, "Legolas", Start)
Gandalf = Karaktärer(11, 7, 0, 0, "Gandalf", Start)
Frodo = Karaktärer(13, 5, 0, 0, "Frodo", Start)
# Define a function to end the game
def slut():
    print("Game Over")
    quit()
# Define a function to increase player's stats
def lvl_poäng(spelar_stats):

    val = input("Vilken vill du höja\n H = hp\n S = str\n")
    if val in ["H", "h", "hp"]:
        spelar_stats.p_hp += 1
        print(f"Din hp är nu {spelar_stats.p_hp}\n")
        spelar_stats.p_lvlpoäng = 0
        return spelar_stats
    elif val in ["S", "s", "str"]:
        spelar_stats.p_str += 1
        print(f"Din str är nu {spelar_stats.p_str}\n")
        spelar_stats.p_lvlpoäng = 0
        return spelar_stats
# Define a function to initiate a fight between player and monster
def fight(spelar_stats, drake_stats):
    print(
        f"och du stöter på en {drake_stats.m_namn} med {drake_stats.m_hp} hp och {drake_stats.m_str} str\n")
    while drake_stats.m_hp > 0:  # Combat function for regular monsters
        if spelar_stats.p_str + spelar_stats.vapen.v_str >= drake_stats.m_hp:
            print("Du besegrade drake\n")
            print(f"Du har {spelar_stats.p_hp} hp kvar\n")
            spelar_stats.p_lvl += 1
            print(f"Du är är nu lvl {spelar_stats.p_lvl}\n")
            spelar_stats.p_lvlpoäng += 1
            return (spelar_stats)  # Return player's stats after defeating the monster

        elif spelar_stats.p_str + spelar_stats.vapen.v_str < drake_stats.m_hp and drake_stats.m_str >= spelar_stats.p_hp + spelar_stats.vapen.v_hp:
            print(
                f"Du dog\nDu nådde lvl {spelar_stats.p_lvl}\nMåste vara skill issue\n")
            slut() # Call function to end the game if player dies
        elif spelar_stats.p_str + spelar_stats.vapen.v_str < drake_stats.m_hp and drake_stats.m_str < spelar_stats.p_hp + spelar_stats.vapen.v_hp:
            drake_stats.m_hp = drake_stats.m_hp - \
                spelar_stats.p_str - spelar_stats.vapen.v_str
            spelar_stats.p_hp = spelar_stats.p_hp - \
                drake_stats.m_str + spelar_stats.vapen.v_hp

def boss_fight(spelar_stats): # Function for boss fight
    print("Nu har du nått sista kammaren men där väntar Drakmästaren\n Hans massiva firekapacitet har gett honom en hp på 30 och en styrka på 10\n")
    m_hp = 30
    m_str = 10
    val = input("S = sloss mot Drakmäsaren\nL = ge upp\n")
    while m_hp == 30:
        if val in ["S", "s", "sloss", "sloss mot Drakmästaren"]:
            while m_hp > 0:
                if spelar_stats.p_str + spelar_stats.vapen.v_str >= m_hp:
                    print(
                        "Du besegrade tarus och kan änligen lämna labyrinten\n")
                    return (spelar_stats)  # Return player's stats after defeating the boss

                elif spelar_stats.p_str + spelar_stats.vapen.v_str < m_hp and m_str >= spelar_stats.p_hp + spelar_stats.vapen.v_hp:
                    print(
                        f"Drakmästaren dödade dig\n Måste vara skill issue\n")
                    slut()
                elif spelar_stats.p_str + spelar_stats.vapen.v_str < m_hp and m_str < spelar_stats.p_hp + spelar_stats.vapen.v_hp:
                    m_hp = m_hp - \
                        spelar_stats.p_str - spelar_stats.vapen.v_str
                    spelar_stats.p_hp = spelar_stats.p_hp - \
                        m_str + spelar_stats.vapen.v_hp
        elif val in ["L", "l", "ge upp"]:
            print(
                "Du gav upp och dog på lvl 15\n Måste vara skill issue\n")
            slut()  # Call function to end the game if player dies

def kista_fas1(spelar_stats):
    # Define weapons available in phase 1
    Svärd = Vapen(health(1, 3), damage(1, 2), "ett Svärd")
    Sköld = Vapen(health(2, 3), damage(0, 0), "en Sköld")
    Yxa = Vapen(health(1, 2), damage(1, 4), "en Yxa")
    Pilbåge = Vapen(health(1, 2), damage(1, 3), "en Pilbåge")
    Spjut = Vapen(health(0, 3), damage(2, 3), "ett Spjut")
   # Randomly choose a weapon from the available options
    vapen = random.choice([Svärd, Sköld, Yxa, Pilbåge, Spjut])
  # Display information about the chosen weapon
    print(
        f"{vapen.v_namn}.\n det har en hp på {vapen.v_hp} och en styrka på {vapen.v_str}\n")
    # Prompt the player to decide whether to exchange the current weapon with the new one
    print(
        "Du måste ta bort ditt nuvarande vapen för att ta det nya\n")

    print(
        f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp och {spelar_stats.vapen.v_str} str\n ")
    while True:
        svar = input(
            "Om du vill byta det nya vapnet mot det gammla vapnet skriv in byt annars skriv något annat \n")
        if svar == "byt" or "Byt":     # Exchanges the weapons
            print("Du har nu ett nytt vapen i din ryggsäck\n")
            spelar_stats.vapen = vapen
            return spelar_stats
        else:
            print(
                "Du lämnade det nya fräsha vapnet i kistan för du kan inte överge ditt gamla vapen efter allt ni gjort tilsammans\n")
            return spelar_stats

def kista_fas2(spelar_stats):
  # Define weapons available in phase 2
    Svärd = Vapen(health(1, 3), damage(2, 4), "ett Svärd")
    Sköld = Vapen(health(2, 4), damage(0, 0), "en Sköld")
    Yxa = Vapen(health(1, 3), damage(1, 6), "en Yxa")
    Pilbåge = Vapen(health(1, 3), damage(2, 5), "en Pilbåge")
    Spjut = Vapen(health(2, 4), damage(3, 4), "ett Spjut")

    vapen = random.choice([Svärd, Sköld, Yxa, Pilbåge, Spjut])
    print(
        f"{vapen.v_namn}.\n det har en hp på {vapen.v_hp} och en styrka på {vapen.v_str}\n")

    print(
        "Du måste ta bort ditt nuvarande vapen för att ta det nya\n")

    print(
        f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp och {spelar_stats.vapen.v_str} str\n ")
# Ask the player for input to decide whether to keep the new weapon or not
    while True:
        svar = input(
            "Om du vill byta det nya vapnet mot det gammla vapnet skriv in 1 annars skriv något annat \n")
        if svar == "1":
            print("Du har nu ett nytt vapen i din ryggsäck\n")
            spelar_stats.vapen = vapen
            return spelar_stats
        else:
            print(
                "Du lämnade det nya fräsha vapnet i kistan för du kan inte överge ditt gamla vapen efter allt ni gjort tilsammans\n")
            return spelar_stats

def kista_fas3(spelar_stats):
   # Define different weapons available in the chest
    Svärd = Vapen(health(2, 4), damage(4, 5), "ett Svärd")
    Sköld = Vapen(health(3, 5), damage(0, 0), "en Sköld")
    Yxa = Vapen(health(2, 3), damage(3, 8), "en Yxa")
    Pilbåge = Vapen(health(2, 4), damage(4, 7), "en Pilbåge")
    Spjut = Vapen(health(3, 4), damage(5, 6), "ett Spjut")

    vapen = random.choice([Svärd, Sköld, Yxa, Pilbåge, Spjut])
    print(
        f"{vapen.v_namn}.\n det har en hp på {vapen.v_hp} och en styrka på {vapen.v_str}\n")
    # Print instructions for the player
    print(
        "Du måste ta bort ditt nuvarande vapen för att ta det nya\n")

    print(
        f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp och {spelar_stats.vapen.v_str} str\n ")
    # Ask the player for input to decide whether to keep the new weapon or not
    while True:
        svar = input(
            "Om du vill byta det nya vapnet mot det gammla vapnet skriv in 1 annars skriv något annat \n")
        if svar == "1":
            print("Du har nu ett nytt vapen i din ryggsäck\n")
            spelar_stats.vapen = vapen
            return spelar_stats
        else:
            print(
                "Du lämnade det nya fräsha vapnet i kistan för du kan inte överge ditt gamla vapen efter allt ni gjort tilsammans\n")
            return spelar_stats
    # Define a function to determine room type in phase 1
def rum_typ_fas1(spelar_stats):
    typ = random.randint(1, 10)
    if typ in [1, 2, 3, 4, 10]: # If the room contains a monster
        drake_stats = drakegenerator_fas1() 
        spelar_stats = fight(spelar_stats, drake_stats) # Initiate a fight with the monster

        if spelar_stats.p_lvlpoäng == 3:  # If player gains enough level points for a level-up
            print(
                "Du har nu fått en lvl uppgradering som du kan använda för att höja en valfri stat med 1. \n")
            print(
                f"Dina nuvarande stats är {spelar_stats.p_hp} hp och {spelar_stats.p_str} str \n")
            spelar_stats = lvl_poäng(spelar_stats) # Upgrade player's stats
            return (spelar_stats)
        else:
            return spelar_stats  # Return player's stats
    elif typ in [5, 6]:  # If the room is empty
        print("och kommer till ett tomt rum\n")
        return spelar_stats  # Return player's stats
    elif typ in [7, 8]:  # If the room contains a chest
        val_kista_fas2(spelar_stats)  # Activate chest event
        return spelar_stats  # Return player's stats
    elif typ in [9, 10]:  # If the room contains a trap
        fälla(spelar_stats)  # Trigger trap event
        return spelar_stats  # Return player's stats
    # Define a function to determine room type in phase 2
def rum_typ_fas2(spelar_stats):
    typ = random.randint(1, 10)
    if typ in [1, 2, 3, 4]:
        drake_stats = drakegenerator_fas2()
        spelar_stats = fight(spelar_stats, drake_stats)
        if spelar_stats.p_lvlpoäng == 3:
            print(
                "Du har nu fått en lvl uppgradering som du kan använda för att höja en valfri stat med 1. \n")
            print(
                f"Dina nuvarande stats är {spelar_stats.p_hp} hp och {spelar_stats.p_str} str \n")
            spelar_stats = lvl_poäng(spelar_stats)
            return (spelar_stats)
        else:
            return spelar_stats
    elif typ in [5, 6]:
        print("och kommer till ett tomt rum\n")
        return (spelar_stats)
    elif typ in [7, 8]:
        val_kista_fas2(spelar_stats)
        return (spelar_stats)
    elif typ in [9, 10]:
        fälla(spelar_stats)
        return (spelar_stats)

def rum_typ_fas3(spelar_stats):
    typ = random.randint(1, 10)
    if typ in [1, 2, 3, 4]:
        drake_stats = drakegenerator_fas3()
        spelar_stats = fight(spelar_stats, drake_stats)
        if spelar_stats.p_lvlpoäng == 3:
            print(
                "Du har nu fått en lvl uppgradering som du kan använda för att höja en valfri stat med 1. \n")
            print(
                f"Dina nuvarande stats är {spelar_stats.p_hp} hp och {spelar_stats.p_str} str \n")
            spelar_stats = lvl_poäng(spelar_stats)
            return (spelar_stats)
        else:
            return spelar_stats
        return (spelar_stats)
    elif typ in [5, 6]:
        print("och kommer till ett tomt rum\n")
        return (spelar_stats)
    elif typ in [7, 8]:
        val_kista_fas3(spelar_stats)
        return (spelar_stats)
    elif typ in [9, 10]:
        fälla(spelar_stats)
        return (spelar_stats)
# Define a function for triggering a trap
def fälla(spelar_stats):
    if spelar_stats.p_hp > 1:
        spelar_stats.p_hp -= 1
        print(
            f"där du klev i en fälla, du har nu {spelar_stats.p_hp} hp kvar\n")
        return spelar_stats
    else:
        print(
            f"där du dör i en fälla\n Du nådde lvl {spelar_stats.p_lvl}\n Måste vara skill issue\n")
        slut()  #call function to end the game if the player dies in the trap


def val_vanlig_fas1(spelar_stats):

    while spelar_stats.p_lvl <= 8:
        val = input(
            "vad vill du göra?\n S = se stats\n V = gå vänster\n F = gå fram\n H = gå höger\n R = öppna ryggsäck\n")
        if val in ["S", "stats", "s", "se stats"]:
            print(
                f"Du har {spelar_stats.p_hp} hp, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")

        elif val in ["V", "vänster", "v", "gå vänster"]:
            print("Du går igenom dörren till vänster ")
            rum_typ_fas1(spelar_stats)
        elif val in ["H", "höger", "h", "gå höger"]:
            print("Du går igenom dörren till höger ")
            rum_typ_fas1(spelar_stats)
        elif val in ["R", "ryggsäck", "r", "öppna ryggsäck"]:
            print(
                f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp {spelar_stats.vapen.v_str} str \n")
        elif val in ["F", "fram", "f", "fram"]:
            print("Du går igenom dörren framför dig ")
            rum_typ_fas1(spelar_stats)
    
    return (spelar_stats)

def val_vanlig_fas2(spelar_stats):
    spelar_stats.p_hp += 3
    print(
        "Du har nu nått fas två som betyder att draken kommer vara starkare och vapnen bättre\n Men du får 3 extra hp\n")
    while spelar_stats.p_lvl <= 15:
        val = input(
            "vad vill du göra?\n S = se stats\n V = gå vänster\n F = gå fram\n H = gå höger\n R = öppna ryggsäck\n")
        if val in ["S", "stats", "s", "se stats"]:
            print(
                f"Du har {spelar_stats.p_hp} hp, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")

        elif val in ["V", "vänster", "v", "gå vänster"]:
            print("Du går igenom dörren till vänster ")
            rum_typ_fas2(spelar_stats)
        elif val in ["H", "höger", "h", "gå höger"]:
            print("Du går igenom dörren till höger ")
            rum_typ_fas2(spelar_stats)
        elif val in ["R", "ryggsäck", "r", "öppna ryggsäck"]:
            print(
                f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp {spelar_stats.vapen.v_str} str \n")
        elif val in ["F", "fram", "f", "gå fram"]:
            print("Du går igenom dörren framför dig ")
            rum_typ_fas2(spelar_stats)
        else:
            print("Din sopa välj ett av alternativen\n")

    return (spelar_stats)

def val_vanlig_fas3(spelar_stats):
    spelar_stats.p_hp += 3
    print(
        "Du har nu nått fas tre som betyder att draken kommer vara starkare och vapnen bättre\n Men du får 3 extra hp\n")
    while spelar_stats.p_lvl <= 18:
        val = input(
            "vad vill du göra?\n S = se stats\n V = gå vänster\n F = gå fram\n H = gå höger\n R = öppna ryggsäck\n")
        if val in ["S", "stats", "s", "se stats"]:
            print(
                f"Du har {spelar_stats.p_hp} hp, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")

        elif val in ["V", "vänster", "v", "gå vänster"]:
            print("Du går igenom dörren till vänster ")
            rum_typ_fas3(spelar_stats)
        elif val in ["H", "höger", "h", "gå höger"]:
            print("Du går igenom dörren till höger ")
            rum_typ_fas3(spelar_stats)
        elif val in ["R", "ryggsäck", "r", "öppna ryggsäck"]:
            print(
                f"Du har {spelar_stats.vapen.v_namn} med {spelar_stats.vapen.v_hp} hp {spelar_stats.vapen.v_str} str \n")
        elif val in ["F", "fram", "f", "gå fram"]:
            print("Du går igenom dörren framför dig ")
            rum_typ_fas3(spelar_stats)

    return (spelar_stats)

def val_kista_fas1(spelar_stats):
    val = input(
        "och hittar en kista. Vad vill du göra?\n S = se stats\n Ö = öppna kista\n L = lämna kistan\n")
    if val in ["S", "stats", "s", "se stats"]:
        print(
            f"Du har hp {spelar_stats.p_hp}, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")
        return val_kista_fas1(spelar_stats)
    elif val in ["Ö", "öppna", "ö", "öppna kista"]:
        print(
            "du öppnar kistan och i den hittar du ")
        kista_fas1(spelar_stats)
        return spelar_stats
    elif val in ["L", "lämna kistan", "lämna", "l"]:
        print("du lämnar kistan där för att rutna, utan att någonsinn få veta vad som finns i den.\nKistans inehåll kommer att förbli ett mysterium för alltid.\n")
        return spelar_stats
    else:
        print("din sopa välj ett av alternativen")
        return val_kista_fas1(spelar_stats)
# Function to handle player's choice when encountering a chest in phase 2
def val_kista_fas2(spelar_stats):
    val = input(
        "och hittar en kista. Vad vill du göra?\n S = se stats\n Ö = öppna kista\n L = lämna kistan\n")
    if val in ["S", "stats", "s", "se stats"]:
        print(
            f"Du har hp {spelar_stats.p_hp}, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")
        return val_kista_fas2(spelar_stats)
    elif val in ["Ö", "öppna", "ö", "öppna kista"]:
        print(
            "du öppnar kistan och i den hittar du ")
        kista_fas2(spelar_stats)
        return spelar_stats
    elif val in ["L", "lämna kistan", "lämna", "l"]:
        print("du lämnar kistan där för att rutna, utan att någonsinn få veta vad som finns i den.\nKistans inehåll kommer att förbli ett mysterium för alltid.\n")
        return spelar_stats
  # Funktion för att hantera spelarens val i fas 3 av kistevenemanget
def val_kista_fas3(spelar_stats):
    val = input(
        "och hittar en kista. Vad vill du göra?\n S = se stats\n Ö = öppna kista\n L = lämna kistan\n")
    if val in ["S", "stats", "s", "se stats"]:
        print(
            f"Du har hp {spelar_stats.p_hp}, din str är {spelar_stats.p_str} och din lvl är {spelar_stats.p_lvl}\n")
        return val_kista_fas3(spelar_stats)
    elif val in ["Ö", "öppna", "ö", "öppna kista"]:
        print(
            "du öppnar kistan och i den hittar du ")
        kista_fas3(spelar_stats)
        return spelar_stats
    elif val in ["L", "lämna kistan", "lämna", "l"]:
        print("du lämnar kistan där för att rutna, utan att någonsinn få veta vad som finns i den.\nKistans inehåll kommer att förbli ett mysterium för alltid.\n")
        return spelar_stats
   # Funktion för att låta spelaren välja en karaktär
def karaktärsval():
    namn = (input("""
    Välj din karaktär.
    svara med 1, 2 eller 3.

    1. Legolas       2. Gandalf       3. Frodo
    hp = 8           hp = 11             hp = 13 
    str = 10         str = 7            str = 5 
    """))

    if namn == "1":
        Spelar_stats = (Legolas)
        print(" Du är nu en Legolas med 5 hp och 10 str \n")
        return (Spelar_stats)

    elif namn == "2":
        Spelar_stats = (Gandalf)
        print(" Du är nu en Gandalf med 8 hp och 7 str \n")
        return (Spelar_stats)

    elif namn == "3":
        Spelar_stats = (Frodo)
        print(" Du är nu en Frodo med 10 hp och 5 str \n")
        return (Spelar_stats)

    else:
        print("svara 1, 2 eller 3 din sopa\n")
        return karaktärsval()
# Funktion för att starta spelet
def main():
    print("""
    Välkommen till Sagornas värld

    Ditt mål är att nå lvl 20 men se upp för Drakmästaren.
    Han har en firekapacitet på 100%.
    """)

# Run the game functions
    spelar_stats = karaktärsval()

    val_vanlig_fas1(spelar_stats)

    val_vanlig_fas2(spelar_stats)

    val_vanlig_fas3(spelar_stats)

    boss_fight(spelar_stats)

    print("Grattis du vann\n")
    slut()   # End the game

main() 

# Define a function for typing text effect
def typingInput(text):
    for character in text:
        print(character, end='', flush=True)
        # Simulera en paus mellan varje tecken
        __import__('builtins').__dict__['input']('')  # Vänta på en "Enter" från användaren
    value = input()
    return value


