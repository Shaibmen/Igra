import json
import random
import csv
import os

#создать классы
class_personaz = {
    "Крестьянин": {"Здоровье": 522, "Урон": 112, "Защита": 15},
    "Заключённый": {"Здоровье": 455, "Урон": 109, "Защита": 10},
    "Пророк": {"Здоровье": 500, "Урон": 20, "Защита": 5},
    "Наёмник": {"Здоровье": 490, "Урон": 130, "Защита": 12},
}

player = {
    "Имя": "",
    "Класс": "",
    "Здоровье": "",
    "Урон": "",
    "Защита": "",
    "Кошелёк": 1500,
}
player_Inventory = []
global mobs_kill
mobs_kill = 0

#создать енеми и боссов и их генерацию
enemy = {
    "Страж леса": {"Здоровье": 200, "Урон": 50, "Защита": 65}
}

boss = {
    "Столп Мироздания": {"Здоровье": 600, "Урон": 200, "Защита": 50},
    "Малликет - бог смерти": {"Здоровье": 500, "Урон": 350, "Защита": 12},
    "Секиро": {"Здоровье": 400, "Урон": 400, "Защита": 10},
}

#создать разброс урона
def damage():
    damage_min_player = player["Урон"] - 10
    damage_max_player = player["Урон"] + 10
    player["Урон"] = random.randint(damage_min_player, damage_max_player)
    return player["Урон"]

#создать награду
def reward():
    money = random.randint(145, 200)
    return money

#уклонение
def yklon():
    itog = random.randint(1,2)
    return itog

#создать режим боя
def fight_enemy():
    print("Вы слышите в кустах какой то звук, на вас накидывается какое - то существо, похоже сейчас будет бой!")
    if mobs_kill == 3:
        enemy_unit = boss["Секиро"]
    else:
       enemy_unit = enemy["Страж леса"]
    if mobs_kill == 6:
        enemy_unit = boss["Малликет - бог смерти"]
    else:
        enemy_unit = enemy["Страж леса"]
    if mobs_kill == 9:
        enemy_unit = boss["Столп Мироздания"]
    else:
       enemy_unit = enemy["Страж леса"]
    if mobs_kill < 3:
        enemy_unit = enemy["Страж леса"]
    
    enemy_unit["Здоровье"] = 200

    while player["Здоровье"] > 0 and enemy_unit["Здоровье"] > 0:
        reward_enemy = reward()
        player_damage = damage()
        print("Ваше здоровье:", player["Здоровье"])
        print("Здоровье врага:", enemy_unit["Здоровье"])
        print("Выбирите действие:\n1.Атаковать\n2.Уклониться\n3.Сбежать")
        
        choise_fight = int(input())
        if choise_fight == 1:
            enemy_unit["Здоровье"] = enemy_unit["Здоровье"] - player_damage
            player["Здоровье"] = player["Здоровье"] - enemy_unit["Урон"]
            if enemy_unit["Здоровье"] < 0:
                print("Монстр повержен!\nВы получили:", reward_enemy,"золотых")
                player["Кошелёк"] = player["Кошелёк"] + reward_enemy
                market()

        if choise_fight == 2:
            ykloniksa = yklon()
            if ykloniksa == 1:
                print("Вы успешно уклонились!")
            else:
                print("произошёл анлак...))")
                player["Здоровье"] = player["Здоровье"] - enemy_unit["Урон"]

        if choise_fight == 3:
            print("Вы сбежали с поля брани, вы поступили как трус, хоть того и требовала ситуация")
            market()       

#присваивание выбранных атрибутов игроку
# damage_player = class_personaz["..."]["Урон"] ----- обрашение к атрибутам словаря

def startStats_player():

    name_player = str(input())

    print("Выберите желаемый класс:")
    print("1. Крестьянин: Здоровье - 522, Урон - 112, Защита - 15, Выносливость - 100\n2. Заключённый: Здоровье - 455, Урон - 109, Защита - 10")
    print("3. Пророк: Здоровье - 500, Урон - 20, Защита - 5, Выносливость - 70\n4. Наёмник: Здоровье - 490, Урон - 130, Защита - 12")
    choise_class = int(input())

    if choise_class == 1:
        player["Имя"] = name_player
        player["Класс"] = "Крестьянин"
        player["Здоровье"] = class_personaz["Крестьянин"]["Здоровье"]
        player["Урон"] = class_personaz["Крестьянин"]["Урон"]
        player["Защита"] = class_personaz["Крестьянин"]["Защита"]
        

    if choise_class == 2:
        player["Имя"] = name_player
        player["Класс"] = "Заключённый"
        player["Здоровье"] = class_personaz["Заключённый"]["Здоровье"]
        player["Урон"] = class_personaz["Заключённый"]["Урон"]
        player["Защита"] = class_personaz["Заключённый"]["Защита"]
    if choise_class == 3:
        player["Имя"] = name_player
        player["Класс"] = "Пророк"
        player["Здоровье"] = class_personaz["Пророк"]["Здоровье"]
        player["Урон"] = class_personaz["Пророк"]["Урон"]
        player["Защита"] = class_personaz["Пророк"]["Защита"]

    if choise_class == 4:
        player["Имя"] = name_player
        player["Класс"] = "Наёмник"
        player["Здоровье"] = class_personaz["Наёмник"]["Здоровье"]
        player["Урон"] = class_personaz["Наёмник"]["Урон"]
        player["Защита"] = class_personaz["Наёмник"]["Защита"]

    if choise_class > 4 or choise_class < 1:
        print("неверное число! Попробуйте ещё раз")
        print("Введите имя:")
        startStats_player()

#создать меню с отображением характеристик
def stats():
    print("Статы:")
    print(player)
    print("Ваш инвентарь:")
    print(player_Inventory)
    print(f"Убито монстров: {mobs_kill}")
    # print(mobs_kill)
    print("Для выхода введите \"0\"")
    exit_stats = int(input())
    if exit_stats == 0:
        market()

#сохранение в json
def tojson():
    playertosave = {
        "Name": player["Имя"],
        "Class": player["Класс"],
        "Zdorovie": player["Здоровье"],
        "Damage": player["Урон"],
        "Defence": player["Защита"],
        "Money": player["Кошелёк"],
        "Inventory": player_Inventory,
    }   
    with open('output.json', 'w') as file:
        json.dump(playertosave, file, indent=4)
    print("Сохранение завершено!")

def zarguzkaFromJson():
    with open('output.json', 'r') as file:
        data = json.load(file)

    player["Имя"] = data["Name"]
    player["Класс"] = data["Class"]
    player["Здоровье"] = data["Zdorovie"]
    player["Урон"] =  data["Damage"]
    player["Защита"] = data["Defence"]
    player["Кошелёк"] = data["Money"]
    

#создание рынка
def market():
    print("Вы приходите на рынок, тут достаточно оживлёно, впрочем как и всегда.\nЧто вы желаете сделать?:")
    print("1.Купить оружие\n2.Купить броню\n3.Взять задание\n4.Посмотреть характеристики\n5.Сходить к лекарю\n6.Сохранить игру\n7.Завершить игру")
    choise_market = int(input())
    if choise_market == 1:
        print("Вы приходите в оружейную лавку, перед вами стоит кузнец и предлагает свой арсенал:")
        # dictionary = {1:"1.Двухперстная печать - 500 золотых.", 2:"2.Клинок алой крови - 1200 золотых.", 3:"3.Воровские клинки - 850 золотых.", 4:"4.Копьё - 450 золотых.", 5:"Цвайхандер - 1500 золотых"}
        print("1.Двухперстная печать - 500 золотых.\n2.Клинок алой крови - 1200 золотых.\n3.Воровские клинки - 850 золотых.\n4.Копьё - 450 золотых.\n5.Цвайхандер - 1500 золотых")
        print("Для выхода введите \"0\"")
        IsDone = True
        while (IsDone != False):
            choise_weapon = int(input())
            if choise_weapon == 1:
                if player["Кошелёк"] > 500:
                    player["Кошелёк"] = player["Кошелёк"] - 500
                    player_Inventory.append("Двухперстная печать")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 2:
                if player["Кошелёк"] > 1200:
                    player["Кошелёк"] = player["Кошелёк"] - 1200
                    player_Inventory.append("Клинок алой крови")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 3:
                if player["Кошелёк"] > 850:
                    player["Кошелёк"] = player["Кошелёк"] - 850
                    player_Inventory.append("Воровские клинки")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 4:
                if player["Кошелёк"] > 450:
                    player["Кошелёк"] = player["Кошелёк"] - 450
                    player_Inventory.append("Копьё")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 5:
                if player["Кошелёк"] > 1500:
                    player["Кошелёк"] = player["Кошелёк"] - 1500
                    player_Inventory.append("Цвайхандер")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 0:
                IsDone = False
                market()

    if choise_market == 2:
        bronya = ["1.Кожанка - 1500 золотых.", "2.Латные доспехи - 2000 золотых.", "3.Мантия чудотворца - 800 золотых.", "4.Снаряжение рыбака - 600 золотых.", "5.Доспех Легионера - 2500 золотых."]
        print("Вы приходите на рынок, перед вами раскинулись многочисленные палатки, сдешние торговцы уже заждались покупателей. Вы подходите к первому торговцу с бронёй:")
        bronya_redach = " | ".join(bronya)
        print(bronya_redach)
        # print("1.Кожанка - 1500 золотых.\n2.Латные доспехи - 2000 золотых.\n3.Мантия чудотворца - 800 золотых.\n4.Снаряжение рыбака - 600 золотых.\n5.Доспех Легионера - 2500 золотых")
        print("Для выхода введите \"0\"")
        IsDone = True
        while (IsDone != False):
            choise_weapon = int(input())
            if choise_weapon == 1:
                if player["Кошелёк"] > 1500:
                    player["Кошелёк"] = player["Кошелёк"] - 500
                    player_Inventory.append("Кожанка")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 2:
                if player["Кошелёк"] > 2000:
                    player["Кошелёк"] = player["Кошелёк"] - 2000
                    player_Inventory.append("Латные доспехи")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 3:
                if player["Кошелёк"] > 800:
                    player["Кошелёк"] = player["Кошелёк"] - 800
                    player_Inventory.append("Мантия чудотворца")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 4:
                if player["Кошелёк"] > 600:
                    player["Кошелёк"] = player["Кошелёк"] - 450
                    player_Inventory.append("Снаряжение рыбака")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 5:
                if player["Кошелёк"] > 2500:
                    player["Кошелёк"] = player["Кошелёк"] - 2500
                    player_Inventory.append("Доспех Легионера")
                    IsDone = False
                else:
                    print("У вас не хватает золотых!")

            if choise_weapon == 0:
                IsDone = False
                market()    

    if choise_market == 3:
        print("В лесу стали пропадать люди из нашего города, пойди туда и разберись")   
        fight_enemy()  

    if choise_market == 4:
        stats()

    if choise_market == 5:
        print("Вы пришли к лекарю, он готов осмотреть ваши раны, однако за это придётся заплатить 200 золотых")
        print("1.Полечиться\n2.Уйти")
        choise_lekar = int(input())
        
        if choise_lekar == 1:
            if player["Кошелёк"] > 200:
                player["Кошелёк"] = player["Кошелёк"] - 200
                player["Здоровье"] = player["Здоровье"] + 100
            else:
                print("У вас не хватает золотых!")
        if choise_lekar == 2:
            IsDone = False
            market()

    if choise_market == 6:
        tojson()

    if choise_market == 7:
        data = [
            [player["Имя"], player["Здоровье"], player["Защита"], player["Класс"], player["Кошелёк"], player["Урон"]]
        ]

        with open("output.csv", 'w', newline='') as file:
            writer = csv.writer(file)

            for row in data:
                writer.writerow(row)
        exit()
        
#История.
def start():
    print("1.Загрузить игру\n2.Начать новую\n3.Удалить сохранение")
    choise_satrt = int(input())
    if choise_satrt == 1:
        zarguzkaFromJson()
        market()
    if choise_satrt == 2:
        print("Был вечер и было утро, день ото дня, и так неизменно. Существовали народы и королевства. \nВсе они подчинялсь единой власти, бессмертный правитель, ужаснейший в своём роде - Гёбу Онива! ")
        print(" ")
        print("Он правит вот уже тысячу лет и никто не знает секрет его долголетия. Правил он жестоко и никто не мог ему возразить, ведь на его стороне Легионы.")
        print("Но однажды с тверди небесной сошла комета. Ужасный знак! В ту же ночь умер и Гёбу, в руках своих он держал руну не от мира сего.\nСошли на землю силы нечистые и погрузилась земля во мрак!")
        print(" ")
        print("Сошли 3 великих бедствия: на юге - неизлечимая хворь погрузившая регион в багровую пустошь, на востоке разошлись тверди земные и повыходила нечисть оттуда как из сказаний.\nНа севере опустели княжества и сёла, что случилось с людьми никто до сих пор не знает.")
        print("Запад же остался нетронутым, но жителей тех регионов постигла ещё более страшная участь - война.")
        print(" ")
        print("\"Долой императора! Долой деспота!\", воскликнули князья и взяли под свой контроль территорию умирающей империи.")
        print("Разразилась страшная война за территорию и погибло в ней столько народу, что вооброзить было невозможно.\nСотни тысяч погибших и упадок империи привели к временному перемирию, но сколько будет длиться этот хрупкий мир?")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" "), print("")
        print("Это была краткая предыстория игрового мира. (Если будет время доведу до ума)")
        print(" "), print("")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #начало игры

        print("Приветсвую, путник! Я страж городских ворот Эворт! Представься, а то не пропущу!")
        startStats_player()
        print("Ну здравствуй", player["Имя"],", говоришь ты", player["Класс"],"?")
        print(" ")
        print("Говорят можно найти работёнку на рынке. Твои способности там оценят по достоинству")
        print(" ")
        while True:
            try:
                market()
            except:
                print("Введённое значение не верно, будь внимательней!")

    if choise_satrt == 3:
        print("Введите путь до сохранения")
        path = str(input())
        os.remove(path)
        print("Удаление завершено!")



#старт всего безумия
start()