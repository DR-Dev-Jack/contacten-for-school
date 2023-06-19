# ________________________________IMPORTS________________________________
# ________________________________VARIABLES______________________________
going_until_i_stop = True
nummer = {"Hakan Akkas": "0643825338", "Djek Ladder": "06", "Gerat-jan willem": "06", "John": "06", "Joe": "06"}


# ________________________________definitions____________________________
def start_menu():
    print("---------------START-MENU-------------------")
    print("|    option 1:   bekijk contacten          |")
    print("|    option 2:   voeg contacten toe        |")
    print("|    option 3:   pas contact aan           |")
    print("|    option 4:   verwijder contact         |")
    print("|    option 5:   stop contact app          |")
    print("--------------------------------------------")
    welke_optie = input("welke option? : ")
    print()
    print()
    return welke_optie


def bekijk_contact(nummer_lijst):
    print("----------------BEKIJK-MENU-----------------")
    for key, value in nummer_lijst.items():
        lengte = len(key) + len(value) + 5
        plus = 41 - lengte
        extra = ""
        for i in range(plus):
            extra += " "
        print("|", key, ":", value, extra, "|")
    print("--------------------------------------------")
    print()
    print()


def voeg_contact(nummer):
    print("-------------TOEVOEGEND-MENU----------------")
    print("|     stap 1:     voeg naam toe            |")
    print("|     stap 2:     bevestig naam            |")
    print("|     stap 3:     voeg nummer toe          |")
    print("|     stap 4:     bevestig nummer          |")
    print("--------------------------------------------")
    nieuw_contact_naam = input("wat is de naam van uw nieuwe contact? : ")
    nieuw_contact_nummer = input("wat is het nummer van uw nieuwe contact? : ")
    nummer[nieuw_contact_naam] = nieuw_contact_nummer
    print()
    print()
    return nummer


def pas_contact(nummer):
    print("---------------VERANDER-MENU---------------|")
    print("|   stap 1:   naam of nummer veranderen    |")
    print("|   stap 2:   wie zijn naam of nummer      |")
    print("|   stap 3:   naar wat voor naam/nummer    |")
    print("|   stap 4:   oude nummer word verwijdert  |")
    print("--------------------------------------------")
    naam_of_nummer = input("wilt u een naam of een nummer veranderen? : ")
    if naam_of_nummer == "een naam" or naam_of_nummer == "naam":
        wie_veranderen = input("wie zijn naam wil je veranderen? : ")
        naar_wat_veranderen = input("naar wat wil je de naam veranderen? :")
        nummer[naar_wat_veranderen] = nummer[wie_veranderen]
        del nummer[wie_veranderen]
    if naam_of_nummer == "een nummer" or naam_of_nummer == "nummer":
        wie_veranderen = input("wie zijn nummer wil je veranderen? : ")
        naar_wat_veranderen = input("naar wat wil je het nummer veranderen? :")
        nummer[wie_veranderen] = naar_wat_veranderen
    print()
    print()
    return nummer


def verwijder_contact(nummer_lijst):
    print("--------------VERWIJDER-MENU---------------|")
    print("|   stap 1:   wie verwijderen              |")
    print("|   stap 2:   waarom verwijderen, grapje   |")
    print("|   stap 3:   bevestiging verwijderen      |")
    print("--------------------------------------------")
    wie_doet_stom = input("wie wil je verwijder? : ")
    del nummer_lijst[wie_doet_stom]
    print("je gaat", wie_doet_stom, "voorlopig niet meer zien")
    print()
    print()
    return nummer_lijst


# ________________________________CODE___________________________________
def main():
    nummer_lijst = {"Hakan Akkas": "0643825338", "Djek Ladder": "06", "Gerat-jan willem": "06", "John": "06", "Joe": "06"}

    while (optie := start_menu()) != "5":
        # optie = start_menu()
        if optie == "1":
            print("option 1:")
            bekijk_contact(nummer_lijst)
        elif optie == "2":
            print("option 2")
            nummer_lijst = voeg_contact(nummer_lijst)
        elif optie == "3":
            print("option 3")
            pas_contact(nummer_lijst)
        elif optie == "4":
            print("option 4")
            nummer_lijst = verwijder_contact(nummer_lijst)

        else:
            print("alleen het nummer typen alsjeblieft")

main()