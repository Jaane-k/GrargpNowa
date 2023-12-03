from random import randint, choice, random


# ---------------------------------
class Player:
    def __init__(self, name, life=100, mana=100, gold=50, experience=0, level=1):
        self.name = name
        self.life = life
        self.mana = mana
        self.gold = gold
        self.experience = experience
        self.level = level
        self.inventory = []

    def display_inventory(self):
        print("Twój ekwipunek:")
        if not self.inventory:
            print("Ekwipunek jest pusty.")
        else:
            for item in self.inventory:
                print(f"- {item['name']}")

    def gain_experience(self, experience_points):
        self.experience += experience_points
        print(f"Zdobywasz {experience_points} punktów doświadczenia!")

        if self.experience >= 30:
            self.level += 1
            self.experience = 0
            print(f"Awansowałeś na poziom {self.level}!")

            if self.level == 2:
                print("Odblokowano nowy atak: Mocny Atak!")
            elif self.level == 3:
                print("Odblokowano nowy atak: Błyskawiczny Atak!")

    def display_stats(self):
        print(f"Masz {self.life} HP, {self.mana} many, {self.gold} złota, Poziom {self.level}, Doświadczenie {self.experience}")
        
# ---------------------------------
def zwykly_atak():
    return randint(3, 10)


def fire_ball():
    global player
    if player.mana < 10:
        print("-" * 40)
        print("Nie masz wystarczającej ilości many!")
        return 0
    player.mana -= 10
    return randint(13, 20)


def mocny_atak():
    return randint(8, 15)


def blyskawiczny_atak():
    global player
    if player.mana < 15:
        print("-" * 40)
        print("Nie masz wystarczającej ilości many!")
        return 0
    player.mana -= 15
    return randint(10, 25)


def mikstura_zdrowia():
    global player
    max_health = 100
    healing_value = randint(15, 30)
    if player.life + healing_value > max_health:
        player.life = max_health
    else:
        player.life += healing_value
    return healing_value


def mikstura_many():
    global player
    max_mana = 100
    mana_value = randint(15, 30)
    if player.mana + mana_value > max_mana:
        player.mana = max_mana
    else:
        player.mana += mana_value
    return mana_value


def wybierz_atak():
    print('a/A - Wykonaj Normalny Atak')
    print('b/B - Fire ball!')
    print('c/C - Mocny Atak')
    print('d/D - Błyskawiczny Atak')
    co = input().upper()
    if co == 'A':
        return zwykly_atak()
    elif co == 'B':
        return fire_ball()
    elif co == 'C':
        return mocny_atak()
    elif co == 'D':
        return blyskawiczny_atak()
    else:
        print("Nie wybrano akcji")
        return 0


# ---------------------------------
def random_opponent():
    opponents = [
        ["Mały Goblin", 15, 3, 0, 10],
        ["Nimfa Wodna", 10, 3, 0, 8],
        ["Duży Troll", 20, 5, 0, 15],
        ["Zmutowany Szczur", 12, 4, 0, 12],
        ["Cienisty Duch", 18, 3, 0, 10],
        ["Wampir", 25, 7, 0, 20],
        ["Ogr", 30, 8, 0, 25],
        ["Szalony Alchemik", 15, 6, 0, 18],
        ["Zjawy", 18, 4, 0, 15],
        ["Mroczny Czarownik", 22, 6, 0, 22]
    ]
    return choice(opponents)


# ---------------------------------
class Shop:
    def __init__(self, items, player_level):
        self.items = items
        self.player_level = player_level

    def display_items(self):
        print(f"Witaj w sklepie! Masz dostępne przedmioty:")
        print(f"Aktualna ilość złota: {player.gold}")
        
        for i, item in enumerate(self.items, 1):
            if item['level'] <= self.player_level:
                print(f"{i}. {item['name']} - {item['price']} złota")
            else:
                print(f"{i}. {item['name']} - Poziom {item['level']} (wymaga poziomu {item['level']})")

    def buy_item(self, player_gold, category_choice):
        valid_categories = ["health_potion", "weapon", "mana_potion", "armor"]
        category_index = category_choice - 1

        if 0 <= category_index < len(valid_categories):
            category_items = [item for item in self.items if item["type"] == valid_categories[category_index]]
            if category_items and category_items[0]["level"] <= player.level:  
                item = category_items[0]
                if player_gold >= item["price"]:
                    print(f"Transakcja udana! Kupiłeś przedmiot: {item['name']}.")
                    player.inventory.append(item)
                    return player_gold - item["price"], category_choice
                else:
                    print("Masz za mało złota. Nie stać cię na ten przedmiot.")
                    return player_gold, 0
            else:
                print("Brak dostępnych przedmiotów w danej kategorii lub masz za niski level.")
                return player_gold, 0
        else:
            print("Niepoprawny wybór kategorii.")
            return player_gold, 0

# ---------------------------------
def casino():
    global player
    print("-" * 40)
    print("Witaj w kasynie! Zaraz zacznie się gra.")
    print("Możesz wygrać lub stracić swoje złoto.")


    chance = random()
    if chance < 0.5:
        print("Wygrać podwójną ilość złota.")
        print("Stracić połowę złota.")
        choice = input("Wybierz 1 lub 2: ")
        if choice == "1":
            print("Gratulacje! Wygrałeś podwójną ilość złota!")
            player.gold *= 2
        elif choice == "2":
            print("Niestety, straciłeś połowę złota.")
            player.gold //= 2
        else:
            print("Niepoprawny wybór. Gra kończy się bez zmian.")
    else:
        print("Wygrać pięciokrotność złota.")
        print("Stracić całe złoto.")
        choice = input("Wybierz 3 lub 4: ")
        if choice == "3":
            print("Gratulacje! Wygrałeś pięciokrotność złota!")
            player.gold *= 5
        elif choice == "4":
            print("Niestety, straciłeś całe złoto.")
            player.gold = 0
        else:
            print("Niepoprawny wybór. Gra kończy się bez zmian.")

# ---------------------------------
shop_items = [
    {"name": "Mikstura zdrowia", "price": 10, "level": 1, "type": "health_potion"},
    {"name": "Miecz", "price": 50, "level": 2, "type": "weapon"},
    {"name": "Eliksir many", "price": 30, "level": 3, "type": "mana_potion"},
    {"name": "Zbroja", "price": 60, "level": 4, "type": "armor"},
]

# ---------------------------------
def gain_experience(experience_points):
    global player
    player.experience += experience_points
    print(f"Zdobywasz {experience_points} punktów doświadczenia!")

    if player.experience >= 30:  
        player.level += 1
        player.experience = 0
        print(f"Awansowałeś na poziom {player.level}!")

        if player.level == 2:
            print("Odblokowano nowy atak: Mocny Atak!")
        elif player.level == 3:
            print("Odblokowano nowy atak: Błyskawiczny Atak!")

# ---------------------------------
player_name = input('Podaj imię twojego bohatera: ')
player = Player(player_name, 100, 100, 50, 0, 1)
player_level = player.level

shop = Shop(shop_items, player_level)

# ---------------------------------
def play_game():
    global player
    number_of_defeated_opponents = 0

    while player.life > 0:
        opponent = random_opponent()
        print("-" * 40)

        while opponent[1] > 0 and player.life > 0:
            print(f"{player.name} walczy teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")

            player.life -= opponent[2]
            if player.life <= 0:
                break

            player.display_stats()
            atak = wybierz_atak()
            opponent[1] -= atak
            print(f"Zadałeś {atak} obrażeń")

        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            number_of_defeated_opponents += 1
            player.gold += randint(5, 15)
            gain_experience(opponent[4])

        print(f"Aktualna ilość złota: {player.gold}")

        print("\nWchodzisz do kasyna:")
        casino()

        print("\nWchodzisz do sklepu:")
        shop.display_items()
        try:
            item_choice = int(input("Wybierz numer przedmiotu do zakupu (lub 0, aby zakończyć zakupy): "))
            if item_choice == 0:
                break

            player.gold, bought_item = shop.buy_item(player.gold, item_choice)
            if bought_item:
                player.display_inventory()
                if shop_items[bought_item - 1]["type"] == "health_potion":
                    healing_value = mikstura_zdrowia()
                    print(f"Wypijasz Miksturę Zdrowia i odzyskujesz {healing_value} punktów życia.")
                elif shop_items[bought_item - 1]["type"] == "mana_potion":
                    mana_value = mikstura_many()
                    print(f"Wypijasz Miksturę Many i odzyskujesz {mana_value} many.")
        except ValueError:
            print("Wprowadzono niepoprawną wartość. Spróbuj jeszcze raz.")

    print("-" * 40)
    print("KONIEC GRY!")
    print(f"Zabiłeś {number_of_defeated_opponents} przeciwników i masz {player.gold} złota, Poziom {player.level}.")

# ---------------------------------
print("Witaj w grze RPG!")
print("Czy chcesz grać samemu czy z kolegami?")
print("1. Samemu")
print("2. Z kolegami")

choice2 = input()
if choice2 == "1":
    play_game()
elif choice2 == "2":
    print("Gra z kolegami jest obecnie niedostępna.")
else:
    print("Niepoprawny wybór.")