import random
import time

purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
biriuz = '\033[96m'
gray = '\033[1;30m'

white = '\033[0m'
black = '\033[30m'


print(red+"Симулятор Нигера V 0.7.6\nРазработчик: MrBuenos(Аверкин Даниил)\nДля просмотра команд введите 0"+white)
time.sleep(3)

day = 0
money = 5679
avt = 1
rg = 0
gun = 1
car = 1
ask = 0
live = 100
band = 1
dayz = 0
unfun = 0
dayun = 0
dayv = -7
lic = 0 
sl1 = 0
sl2 = 0
sl3 = 0
sl4 = 0
sl5 = 0

while True:
    day = day+1
    money -= 235*band
    
    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )

    if (day-dayz == 3) and (ask > 0):
        ask -= 1
        dayz = day
    
    if ask > 5:
        ask = 5
    
    if day-dayun == 7:
        unfun = 0
    
    if band < 1:
        live = 0
    
    if live < 1:
        print("Вы умерли, вы проиграли")
        break
    
    if live > 100:
        live = 100
        
    if money < 0:
        live = live-20
    
    if unfun > 1:
        r = random.randint(3, 20)
        r1 = random.randint(1, 5)
        power1 = r*r1
        power = gun*band*1.5
        print("Жители подконтрольного района\nПодняли бунт\nИх силы:", r, "человек", "оружие", r1)
        print("Подавить бунт - 1\nОтказаться от района - 2")
        v = int(input()) 
        unfun = 0
        if v == 1:
            if power >= power1:
                avt += 20
                if power-power1 > 16:
                    print("Бунт подавлен. Это было просто")
                    input('Введите Enter')
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                if 8 < power-power1 < 17:
                    print("Бунт подавлен.\nНо ты получил легкое ранение.")
                    live = live-17
                    input('Введите Enter')
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                if 4 < power-power1 < 9:
                    print("Бунт подавлен.\nНо ты получил серьезное ранение.")                        
                    live = live-57
                    input('Введите Enter')
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                if 1 < power-power1 < 5:
                    if band > 1:
                        print("Бунт подавлен.\nНо вы потеряли одного нигера")
                        band = band-1
                        input('Введите Enter')
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                    if band < 2:
                        print("Бунт подавлен.\nНо ты очень сильно ранен")
                        live= live-86
                        input('Введите Enter')
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
            else:
                print("Бунт не подавлен, вы потеряли район.\nВы сильно ранены")
                live = live-86
                rg = 0
                input('Введите Enter')
                print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )

        if v == 2:
            print("Вы отказались, вы потеряли район")
            rg = 0
            input('Введите Enter')
            
    if ask == 1:
        rask = random.randint(1, 100)
        if rask < 17:
            print("\nВас нашла полиция!")
            print("Команды:\nЗащищаться оружием - 1\nСкрыться на транспорте - 2\nВызвать банду - 3\nОткупиться - 4\nСдаться - 5")
            ch = int(input())
            if ch == 1:
                r = random.randint(1, 10)
                zach = gun+r
                if zach > 6:
                    print("Вы защитились, но в перестрелке получилиранение. Авторитет +10")
                    avt = avt+10
                    live = live-26
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали, вы проиграли")
                    break
            if ch == 2:
                r = random.randint(1, 10)
                zuch = car+r
                if zuch > 6:
                    print("Вы скрылись. Авторитет +5")
                    avt = avt+5
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали вы проиграли")
                    break
            
            if ch == 3:
                r = random.randint(1, 10)
                zach = band*r
                if zach > 19:
                    print("Вы спасены. Авторитет +2")
                    avt = avt+2
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас не смогли спасти. Вы проиграли")
                    break
                
            if ch == 4:
                r = random.randint(500, 5000)
                print("Они хотят", r, "руб.\nЧтобы отдать введите 1\nЧтобы отказать введите 2")
                v = int(input())
                if v == 1:
                    if money >= r:
                        money = money-r
                        print("Вы откупились")
                        ask = 0
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                    else:
                        print("Вам не хватило денег.\nВас поймали, вы проиграли.")
                        break
                if v == 2:
                    print("Вас поймали, вы проиграли")
                    break
                    
            if ch == 5:
                print("Вас поймали, вы проиграли")
                break
                
    
    if ask == 2:
        rask = random.randint(1, 100)
        if rask < 25:
            print("\nВас нашла полиция!")
            print("Команды:\nЗащищаться оружием - 1\nСкрыться на транспорте - 2\nВызвать банду - 3\nОткупиться - 4\nСдаться - 5")
            ch = int(input())
            if ch == 1:
                r = random.randint(1, 10)
                zach = gun+r
                if zach > 9:
                    print("Вы защитились, но в перестрелке получилиранение. Авторитет +10")
                    avt = avt+15
                    live = live-29
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали, вы проиграли")
                    break
            if ch == 2:
                r = random.randint(1, 10)
                zuch = car+r
                if zuch > 9:
                    print("Вы скрылись. Авторитет +5")
                    avt = avt+10
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали вы проиграли")
                    break
            
            if ch == 3:
                r = random.randint(1, 10)
                zach = band*r
                if zach > 25:
                    print("Вы спасены. Авторитет +2")
                    avt = avt+5
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас не смогли спасти. Вы проиграли")
                    break
                
            if ch == 4:
                r = random.randint(2000, 8000)
                print("Они хотят", r, "руб.\nЧтобы отдать введите 1\nЧтобы отказать введите 2")
                v = int(input())
                if v == 1:
                    if money >= r:
                        money = money-r
                        print("Вы откупились")
                        ask = 0
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                    else:
                        print("Вам не хватило денег.\nВас поймали, вы проиграли.")
                        break
                if v == 2:
                    print("Вас поймали, вы проиграли")
                    break
                    
            if ch == 5:
                print("Вас поймали, вы проиграли")
                break
                                
    if ask == 3:
        rask = random.randint(1, 100)
        if rask < 40:
            print("\nВас нашла полиция!")
            print("Команды:\nЗащищаться оружием - 1\nСкрыться на транспорте - 2\nВызвать банду - 3\nОткупиться - 4\nСдаться - 5")
            ch = int(input())
            if ch == 1:
                r = random.randint(1, 10)
                zach = gun+r
                if zach > 12:
                    print("Вы защитились, но в перестрелке получилиранение. Авторитет +10")
                    avt = avt+10
                    live = live-26
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали, вы проиграли")
                    break
            if ch == 2:
                r = random.randint(1, 10)
                zuch = car+r
                if zuch > 12:
                    print("Вы скрылись. Авторитет +5")
                    avt = avt+5
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали вы проиграли")
                    break
            
            if ch == 3:
                r = random.randint(1, 10)
                zach = band*r
                if zach > 30:
                    print("Вы спасены. Авторитет +2")
                    avt = avt+2
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас не смогли спасти. Вы проиграли")
                    break
                
            if ch == 4:
                r = random.randint(5000, 15000)
                print("Они хотят", r, "руб.\nЧтобы отдать введите 1\nЧтобы отказать введите 2")
                v = int(input())
                if v == 1:
                    if money >= r:
                        money = money-r
                        print("Вы откупились")
                        ask = 0
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                    else:
                        print("Вам не хватило денег.\nВас поймали, вы проиграли.")
                        break
                if v == 2:
                    print("Вас поймали, вы проиграли")
                    break
                    
            if ch == 5:
                print("Вас поймали, вы проиграли")
                break
                
    if ask == 4:
        rask = random.randint(1, 100)
        if rask < 65:
            print("\nВас нашла полиция!")
            print("Команды:\nЗащищаться оружием - 1\nСкрыться на транспорте - 2\nВызвать банду - 3\nОткупиться - 4\nСдаться - 5")
            ch = int(input())
            if ch == 1:
                r = random.randint(1, 10)
                zach = gun+r
                if zach > 15:
                    print("Вы защитились, но в перестрелке получилиранение. Авторитет +10")
                    avt = avt+10
                    live = live-26
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали, вы проиграли")
                    break
            if ch == 2:
                r = random.randint(1, 10)
                zuch = car+r
                if zuch > 15:
                    print("Вы скрылись. Авторитет +5")
                    avt = avt+5
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали вы проиграли")
                    break
            
            if ch == 3:
                r = random.randint(1, 10)
                zach = band*r
                if zach > 30:
                    print("Вы спасены. Авторитет +2")
                    avt = avt+2
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас не смогли спасти. Вы проиграли")
                    break
                
            if ch == 4:
                r = random.randint(20000, 50000)
                print("Они хотят", r, "руб.\nЧтобы отдать введите 1\nЧтобы отказать введите 2")
                v = int(input())
                if v == 1:
                    if money >= r:
                        money = money-r
                        print("Вы откупились")
                        ask = 0
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                    else:
                        print("Вам не хватило денег.\nВас поймали, вы проиграли.")
                        break
                if v == 2:
                    print("Вас поймали, вы проиграли")
                    break
                    
            if ch == 5:
                print("Вас поймали, вы проиграли")
                break
                
    if ask == 5:
        rask = random.randint(1, 100)
        if rask < 76:
            print("\nВас нашла полиция!")
            print("Команды:\nЗащищаться оружием - 1\nСкрыться на транспорте - 2\nВызвать банду - 3\nОткупиться - 4\nСдаться - 5")
            ch = int(input())
            if ch == 1:
                r = random.randint(1, 10)
                zach = gun+r
                if zach > 20:
                    print("Вы защитились, но в перестрелке получилиранение. Авторитет +10")
                    avt = avt+10
                    live = live-26
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали, вы проиграли")
                    break
            if ch == 2:
                r = random.randint(1, 10)
                zuch = car+r
                if zuch > 20:
                    print("Вы скрылись. Авторитет +5")
                    avt = avt+5
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали вы проиграли")
                    break
            
            if ch == 3:
                r = random.randint(1, 10)
                zach = band*r
                if zach > 37:
                    print("Вы спасены. Авторитет +2")
                    avt = avt+2
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас не смогли спасти. Вы проиграли")
                    break
                
            if ch == 4:
                r = random.randint(50000, 250000)
                print("Они хотят", r, "руб.\nЧтобы отдать введите 1\nЧтобы отказать введите 2")
                v = int(input())
                if v == 1:
                    if money >= r:
                        money = money-r
                        print("Вы откупились")
                        ask = 0
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                    else:
                        print("Вам не хватило денег.\nВас поймали, вы проиграли.")
                        break
                if v == 2:
                    print("Вас поймали, вы проиграли")
                    break
                    
            if ch == 5:
                print("Вас поймали, вы проиграли")
                break
                
    if ask == 6:
        rask = random.randint(1, 100)
        if rask < 90:
            print("\nВас нашла полиция!")
            print("Команды:\nЗащищаться оружием - 1\nСкрыться на транспорте - 2\nВызвать банду - 3\nОткупиться - 4\nСдаться - 5")
            ch = int(input())
            if ch == 1:
                r = random.randint(1, 10)
                zach = gun+r
                if zach > 27:
                    print("Вы защитились, но в перестрелке получилиранение. Авторитет +10")
                    avt = avt+10
                    live = live-26
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали, вы проиграли")
                    break
            if ch == 2:
                r = random.randint(1, 10)
                zuch = car+r
                if zuch > 27:
                    print("Вы скрылись. Авторитет +5")
                    avt = avt+5
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас поймали вы проиграли")
                    break
            
            if ch == 3:
                r = random.randint(1, 10)
                zach = band*r
                if zach > 50:
                    print("Вы спасены. Авторитет +2")
                    avt = avt+2
                    ask = 0
                    print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                else:
                    print("Вас не смогли спасти. Вы проиграли")
                    break
                
            if ch == 4:
                r = random.randint(250000, 1000000)
                print("Они хотят", r, "руб.\nЧтобы отдать введите 1\nЧтобы отказать введите 2")
                v = int(input())
                if v == 1:
                    if money >= r:
                        money = money-r
                        print("Вы откупились")
                        ask = 0
                        print("День:", day, "\nДеньги:", money, "руб.\nАвторитет:", avt, "\nПодкотрольные районы:", rg, "\nОружие:", gun, "\nТранспорт:", car, "\nУровень розыска:", ask, "\nЧеловек в банде:", band, "\nЗдоровье:", live )
                    else:
                        print("Вам не хватило денег.\nВас поймали, вы проиграли.")
                        break
                if v == 2:
                    print("Вас поймали, вы проиграли")
                    break
                    
            if ch == 5:
                print("Вас поймали, вы проиграли")
                break
                
    cmd = input()
    if cmd == '89183877010':
        print("1 Код на деньги")
        print("2 Код на понижение розыска")
        v = int(input())
        if v == 1:
            print("Введите нужную сумму")
            m = int(input())
            money = money+m
    
        if v == 2:
            print("Введите сколько звезд убрать")
            z = int(input())
            ask = ask-z
    
    if cmd == '0':
        print("Пропустить день - 1")
        print("Ограбить прохожего - 2")
        print("Украсть тачку - 3")
        print("Захватить район - 4")
        print("Собрать дань с района - 5")
        print("Вербовать людей в банду - 6")
        print("Купить лицензии - 7")
        print("Купить оружие - 8")
        print("Ограбить магазин - 9")
        print("Личиться в больнице - 10")
        print("Продать или купить вещи - 11")
        input('Введите Enter')
        day = day-1
        money = money+235
        avt = avt+1
        
        
    if cmd == '1':
        print("День прошел бессмыслено")
    if cmd == '2':
        r2 = random.randint(1, 10)
        if r2 < 8:
            r = random.randint(1, 1000)
            money = money + (avt + r)*gun
            print("Вы ограбили прохожего на",(avt + r)*gun, "руб")
            avt = avt+5
            r3 = random.randint(1, 10)
            if r3 < 6:
                ask = ask+1
            dayz = day
            input('Введите Enter')
        else:
            print("Прохожий убежал. Авторитет -3")
            avt = avt-3
            dayz = day
            ask = ask+1
            input('Введите Enter')

    if cmd == '3':
        r = random.randint(1, 1000)
        if r+avt > 500:
            ch = random.randint(1, 992)
            if ch < 801:    
                print("Вы угнали тачку мощностью 1")
                if car == 1:
                    car = 1
                ask = ask+1
                input('Введите Enter')
            if 951 > ch > 800:
                print("Вы угнали тачку мощностью 2")
                if car < 2:
                    car = 2
                ask = ask+1
                input('Введите Enter')
            if 986 > ch > 950:
                print("Вы угнали тачку мощностью 3\nАвторитет +3")
                if car < 3:
                    car = 3
                ask = ask+1
                avt = avt+3
                input('Введите Enter')
            if 991 > ch > 985:
                print("Вы угнали тачку мощностью 4\nАвторитет +12")
                if car < 4:
                    car = 4
                ask = ask+2
                avt = avt+12
                input('Введите Enter')
            if 993 > ch > 990:
                print("Вы угнали тачку мощностью 5\nАвторитет +20")
                if car < 5:
                    car = 5
                ask = ask+2
                avt = avt+20
                input('Введите Enter')
        else:
            print("Угнать машину не удалось, вас нашла полиция\nПришлось сбежать")
            ask = ask+1
            input('Введите Enter')

    if cmd == '4':
        print("Команды:")
        print("Захватить район - 1")
        print("Выкупить район - 2")
        ch = int(input())
        if ch == 1:
            print("Список районов")
            print("1 Блов Брик - 2 чел.; оружие 3; 1500 р.")
            print("2 Биг Бич - 4 чел.; оружие 4; 9000 р.")
            print("3 Лонг Ган - 7 чел.; оружие 4; 13000 р.")
            print("4 Рич ВИЧ - 8 чел.; оружие 5; 20000 р.")
            print("5 Лич Пич - 12 чел.; оружие 7;00 р.")
            print("6 Рус Бич - 23 чел.; оружие 10; 100000 р.")
            v = int(input())
            if v == 1:
                r = random.randint(1, 3)
                power = band*gun+r
                r1 = random.randint(1, 3)
                power1 = 6+r1
                if power >= power1:
                    r = random.randint(1, 5)
                    avt = avt+20
                    rg = 1
                    if power-power1 > 16:
                        print("Район захвачен. Это было просто")
                        input('Введите Enter')
                    if 8 < power-power1 < 17:
                        print("Район захвачен.\nНо ты получил легкое ранение.")
                        live = live-17
                        input('Введите Enter')
                    if 4 < power-power1 < 9:
                        print("Район захвачен.\nНо ты получил серьезное ранение.")                        
                        live = live-57
                        input('Введите Enter')
                    if 1 < power-power1 < 5:
                        if band > 1:
                            print("Район захвачен.\nНо вы потеряли одного нигера")
                            band = band-1
                            input('Введите Enter')
                        if band < 2:
                            print("Район захвачен.\nНо ты очень сильно ранен")
                            live= live-86
                            input('Введите Enter')
                    if 0 <= power-power1 < 3:
                        if band > 1:
                            print("Район захвачен.\nНо вы ранены и потеряли нигера")
                            band = band-1
                            live = live-43
                            input('Введите Enter')
                        else:
                            print("Район захвачен.\nНо вы сильно ранены и кто-то позвонил ментам")
                            live = live-67
                            ask = ask+3
                            input('Введите Enter')
                else:
                    print("Район не захвачен. Вы сильно ранены")
                    live = live-84
                    input('Введите Enter')

            if v == 2:
                r = random.randint(1, 5)
                power = band*gun+r
                r1 = random.randint(1, 5)
                power1 = 16+r1
                if power >= power1:
                    r = random.randint(1, 5)
                    avt = avt+50
                    rg = 2
                    if power-power1 > 16:
                        print("Район захвачен. Это было просто")
                        input('Введите Enter')
                    if 8 < power-power1 < 17:
                        print("Район захвачен.\nНо ты получил легкое ранение.")
                        live = live-17
                        input('Введите Enter')
                    if 4 < power-power1 < 9:
                        print("Район захвачен.\nНо ты получил серьезное ранение.")                        
                        live = live-57
                        input('Введите Enter')
                    if 1 < power-power1 < 5:
                        if band > 1:
                            print("Район захвачен.\nНо вы потеряли одного нигера")
                            band = band-1
                            input('Введите Enter')
                        if band < 2:
                            print("Район захвачен.\nНо ты очень сильно ранен")
                            live= live-86
                            input('Введите Enter')
                    if 0 <= power-power1 < 3:
                        if band > 1:
                            print("Район захвачен.\nНо вы ранены и потеряли нигера")
                            band = band-1
                            live = live-43
                            input('Введите Enter')
                        else:
                            print("Район захвачен.\nНо вы сильно ранены и кто-то позвонил ментам")
                            live = live-67
                            ask = ask+3
                            input('Введите Enter')
                else:
                    print("Район не захвачен. Вы сильно ранены")
                    live = live-93
                    input('Введите Enter')

                
            if v == 3:
                r = random.randint(1, 8)
                power = band*gun+r
                r1 = random.randint(1, 8)
                power1 = 28+r1
                if power >= power1:
                    avt = avt+100
                    rg = 3
                    if power-power1 > 16:
                        print("Район захвачен. Это было просто")
                        input('Введите Enter')
                    if 8 < power-power1 < 17:
                        print("Район захвачен.\nНо ты получил легкое ранение.")
                        live = live-27
                        input('Введите Enter')
                    if 4 < power-power1 < 9:
                        print("Район захвачен.\nНо ты получил серьезное ранение.")                        
                        live = live-57
                        input('Введите Enter')
                    if 1 < power-power1 < 5:
                        print("Район захвачен.\nНо вы потеряли одного нигера")
                        band = band-1
                        input('Введите Enter')
                    if 0 <= power-power1 < 3:
                        print("Район захвачен.\nНо вы ранены и потеряли нигера")
                        band = band-1
                        live = live-47
                        input('Введите Enter')
                else:
                    print("Район не захвачен. Вы сильно ранены и потеряли одного нигера")
                    live = live-84
                    band = band-1
                    input('Введите Enter')

                        
                        
            if v == 4:
                r = random.randint(1, 10)
                power = band*gun+r
                r1 = random.randint(1, 10)
                power1 = 40+r1
                if power >= power1:
                    avt = avt+200
                    rg = 4
                    if power-power1 > 16:
                        print("Район захвачен. Это было просто")
                        input('Введите Enter')
                    if 8 < power-power1 < 17:
                        print("Район захвачен.\nНо ты получил легкое ранение.")
                        live = live-31
                        input('Введите Enter')
                    if 4 < power-power1 < 9:
                        print("Район захвачен.\nНо ты получил серьезное ранение.")                        
                        live = live-60
                        input('Введите Enter')
                    if 1 < power-power1 < 5:
                        print("Район захвачен.\nНо вы потеряли двух нигеров")
                        band = band-2
                        input('Введите Enter')
                    if 0 <= power-power1 < 3:
                        print("Район захвачен.\nНо вы ранены и потеряли двух нигеров")
                        band = band-2
                        live = live-37
                        input('Введите Enter')
                else:
                    print("Район не захвачен. Вы сильно ранены и потеряли трех нигеров")
                    live = live-84
                    band = band-3
                    input('Введите Enter')

                
            if v == 5:
                r = random.randint(1, 12)
                power = band*gun+r
                r1 = random.randint(1, 12)
                power1 = 84+r1
                if power >= power1:
                    avt = avt+300
                    rg = 5
                    if power-power1 > 16:
                        print("Район захвачен. Это было просто")
                        input('Введите Enter')
                    if 8 < power-power1 < 1:
                        print("Район захвачен.\nНо ты получил легкое ранение.")
                        live = live-27
                        input('Введите Enter')
                    if 4 < power-power1 < 9:
                        print("Район захвачен.\nНо ты получил серьезное ранение.")                        
                        live = live-57
                        input('Введите Enter')
                    if 1 < power-power1 < 5:
                        print("Район захвачен.\nНо вы потеряли двух нигеров")
                        band = band-2
                        input('Введите Enter')
                    if 0 <= power-power1 < 3:
                        print("Район захвачен.\nНо вы ранены и потеряли трех нигеров")
                        band = band-3
                        live = live-24
                        input('Введите Enter')
                else:
                    print("Район не захвачен. Вы сильно ранены и потеряли четырех нигеров")
                    live = live-84
                    band = band-4
                    input('Введите Enter')

                        
            if v == 6:
                r = random.randint(1, 15)
                power = band*gun+r
                r1 = random.randint(1, 15)
                power1 = 230+r1
                if power >= power1:
                    avt = avt+450
                    rg = 6
                    if power-power1 > 16:
                        print("Район захвачен. Это было просто")
                        input('Введите Enter')
                    if 8 < power-power1 < 17:
                        print("Район захвачен.\nНо ты получил ранение.")
                        live = live-37
                        input('Введите Enter')
                    if 4 < power-power1 < 9:
                        print("Район захвачен.\nНо ты получил серьезное ранение.")                        
                        live = live-67
                        input('Введите Enter')
                    if 1 < power-power1 < 5:
                        print("Район захвачен.\nНо вы потеряли четырех нигеров")
                        band = band-4
                        input('Введите Enter')
                    if 0 <= power-power1 < 3:
                        print("Район захвачен.\nНо вы ранены и потеряли четырех нигеров")
                        band = band-5
                        live = live-27
                        input('Введите Enter')
                else:
                    print("Район не захвачен. Вы сильно ранены и потеряли 7 нигеров")
                    live = live-84
                    band = band-7
                    input('Введите Enter')

                        
        if ch == 2:
            print("Список районов")
            print("1 Блов Брик - цена 15000; 1500 р.")
            print("2 Биг Бич - цена 90000; 9000 р.")
            print("3 Лонг Ган - цена 130000; 13000 р.")
            print("4 Рич ВИЧ - цена 200000; 20000 р.")
            print("5 Лич Пич - цена 500000 ;50000 р.")
            print("6 Рус Бич - цена 1000000; 100000 р.")
            v = int(input())
            if v == 1:
                if money >= 15000:
                    rg = 1
                    money = money-15000
                    avt = avt+15
                    print("Район куплен")
                    input('Введите Enter')
                else:
                    print("Не хватает денег")
                    input('Введите Enter')
            if v == 2:
                if money >= 90000:
                    rg = 2
                    money = money-90000
                    avt = avt+37
                    print("Район куплен")
                    input('Введите Enter')
                else:
                    print("Не хватает денег")
                    input('Введите Enter')
            if v == 3:
                if money >= 130000:
                    rg = 3
                    money = money-130000
                    avt = avt+75
                    print("Район куплен")
                    input('Введите Enter')
                else:
                    print("Не хватает денег")
                    input('Введите Enter')
            if v == 4:
                if money >= 200000:
                    rg = 4
                    money = money-200000
                    avt = avt+150
                    print("Район куплен")
                    input('Введите Enter')
                else:
                    print("Не хватает денег")
                    input('Введите Enter')
            if v == 5:
                if money >= 500000:
                    rg = 5
                    money = money-500000
                    avt = avt+230
                    print("Район куплен")
                    input('Введите Enter')
                else:
                    print("Не хватает денег")
                    input('Введите Enter')
            if v == 6:
                if money >= 1000000:
                    rg = 6
                    money = money-1000000
                    avt = avt+370
                    print("Район куплен")
                    input('Введите Enter')
                else:
                    print("Не хватает денег")
                    input('Введите Enter')

    if cmd == '5':
        unfun = unfun+1
        dayun = day
        if rg == 1:
            money = money+1500  
            print("Вы собрали 1500 р.\nНедовольство жителей =", unfun)
        if rg == 2:
            money = money+9000
            print("Вы собрали 9000 р.\nНедовольство жителей =", unfun)
        if rg == 3:
            money = money+13000
            print("Вы собрали 13000 р.\nНедовольство жителей =", unfun)
        if rg == 4:
            money = money+20000
            print("Вы собрали 20000 р.\nНедовольство жителей =", unfun)
        if rg == 5:
            money = money+50000
            print("Вы собрали 50000 р.\nНедовольство жителей =", unfun)
        if rg == 6:
            money = money+100000
            print("Вы собрали 100000 р.\nНедовольство жителей =", unfun)
        input('Введите Enter')

    if cmd == '6':
        if day-dayv > 6:
            r = random.randint(1, 1000)
            if r+avt > 410:
                ra = random.randint(1, 1000)
                rm = random.randint(2000, 1000000)
                dayv = day
                print("Вы нашли нигера\nОн хочет:", rm, "руб.", "\nДолжно быть минимум", ra, "авторитета\nВы согласны?\n1 - да\n2 - нет")
                v = int(input())
                if v == 1:
                    if money >= rm:
                        if avt >= ra:
                            money = money-rm
                            band = band+1
                            print("Вы успешно завербовали нигера")
                            input('Введите Enter')
                        else:
                            print("Нехватает авторитета")
                            input('Введите Enter')
                    else:
                        print("Нехватает денег")
                        input('Введите Enter')
            else:
                print("Вы никого не нашли\nПопробуйте через неделю")
                input('Введите Enter')
        else:
            print("Вербовать людей можно только раз в неделю.")
            input('Введите Enter')

    if cmd == '7':
        print("1 Лицензия на оружие 45900 р.")
        v = int(input())
        if v == 1:
            if money >= 45900:
                lic = 1
                money = money-45900
                print("Лицензия куплена")
                input('Введите Enter')
            else:
                print("Не хватает денег")
                input('Введите Enter')
   
    if cmd == '8':
        if lic == 1:
            print("1 Пистолет BP-17; 24365 р.")
            print("2 Пистолет JL-47; 35090 р.")
            print("3 Пистолет-Автомат AM-12; 45750 р.")
            print("4 УЗИ UlTI; 68597 р.")
            print("5 АК-47; 86280 р.")
            print("6 СЛОН; 126974 р.")
            ch = int(input())
            if ch == 1:
                if money >= 24365:
                    gun = 2
                    money -= 24365
                    print("Оружие куплено")
                    input('Введите Enter')
                else:
                    print("Вам нехватает денег")
                    input('Введите Enter')

            if ch == 2:
                if money >= 35090:
                    gun = 3
                    money -= 35090
                    print("Оружие куплено")
                    input('Введите Enter')
                else:
                    print("Вам нехватает денег")
                    input('Введите Enter')

            if ch == 3:
                if money >= 45750:
                    gun = 4
                    money -= 45750
                    print("Оружие куплено")
                    input('Введите Enter')
                else:
                    print("Вам нехватает денег")
                    input('Введите Enter')

            if ch == 4:
                if money >= 68597:
                    gun = 5
                    money -= 68597
                    print("Оружие куплено")
                    input('Введите Enter')
                else:
                    print("Вам нехватает денег")
                    input('Введите Enter')

            if ch == 5:
                if money >= 86280:
                    gun = 6
                    money -= 86280
                    print("Оружие куплено")
                    input('Введите Enter')
                else:
                    print("Вам нехватает денег")
                    input('Введите Enter')

            if ch == 6:
                if money >= 126974:
                    gun = 7
                    money -= 126974
                    print("Оружие куплено")
                    input('Введите Enter')
                else:
                    print("Вам нехватает денег")
                    input('Введите Enter')


        else:
            print("Сначала купите лицензию")
            input('Введите Enter')

    if cmd == '9':
        r = random.randint(1, 5)
        pow = (band+r)*gun
        pow2 = random.randint(5, 30)
        if pow > pow2:
            rm = random.randint(1000, 30000)
            money = money+rm
            ask = ask+3
            avt = avt+50
            print("Вы ограбили магазин на", rm, "р.")
            input('Введите Enter')
        else:
            live = live-86
            ask = ask+2
            print("Ограбить магазин не удалось\nВы сильно ранены")
            input('Введите Enter')

    if cmd == '10':
        print("Восстановление 1 HP - 500 руб.\nВведите кол-во HP для восстановления")
        clive = int(input())
        if money >= clive*500:
            live = live+clive
            money = money-clive*500
            print("Вы выличились за", clive, "р.")
            input('Введите Enter')
        else:
            print("Не хватает денег")
            input('Введите Enter')

    if cmd == '11':
        rc1 = random.randint(4000, 9000)
        rc2 = random.randint(500, 3000)
        rc3 = random.randint(500000, 850000)
        rc4 = random.randint(2000, 9500)
        rc5 = random.randint(15000, 26000)
        print("1 Кольян -", sl1, "шт. Цена", rc1)
        print("2 Косяк -", sl2, "шт. Цена", rc2)
        print("3 Тачка -", sl3, "шт. Цена", rc3)
        print("4 BMX -", sl4, "шт. Цена", rc4)
        print("5 Пушка -", sl5, "шт. Цена", rc5)
        v = int(input())
        if v == 1:
            print("1 Купить")
            print("2 Продать")
            ch = int(input())
            if ch == 1:
                if money >= rc1:
                    sl1 = sl1+1
                    money = money-rc1
                    print("Вещь куплена")
                    input('Введите Enter')
                else:
                    print("Нехватает денег")
                    input('Введите Enter')
            if ch == 2:
                if sl1 > 0:
                    sl1 = sl1-1
                    money = money+rc1
                    print("Вещь продана")
                    input('Введите Enter')
                else:
                    print("У тебя нету этой вещи")
                    input('Введите Enter')

        if v == 2:
            print("1 Купить")
            print("2 Продать")
            ch = int(input())
            if ch == 1:
                if money >= rc2:
                    sl2 = sl2+1
                    money = money-rc2
                    print("Вещь куплена")
                    input('Введите Enter')
                else:
                    print("Нехватает денег")
                    input('Введите Enter')
            if ch == 2:
                if sl2 > 0:
                    sl2 = sl2-1
                    money = money+rc2
                    print("Вещь продана")
                    input('Введите Enter')
                else:
                    print("У тебя нету этой вещи")
                    input('Введите Enter')

        if v == 3:
            print("1 Купить")
            print("2 Продать")
            ch = int(input())
            if ch == 1:
                if money >= rc3:
                    sl3 = sl3+1
                    money = money-rc3
                    print("Вещь куплена")
                    input('Введите Enter')
                else:
                    print("Нехватает денег")
                    input('Введите Enter')
            if ch == 2:
                if sl3 > 0:
                    sl3 = sl3-1
                    money = money+rc3
                    print("Вещь продана")
                    input('Введите Enter')
                else:
                    print("У тебя нету этой вещи")
                    input('Введите Enter')
        
        if v == 4:
            print("1 Купить")
            print("2 Продать")
            ch = int(input())
            if ch == 1:
                if money >= rc4:
                    sl4 = sl4+1
                    money = money-rc4
                    print("Вещь куплена")
                    input('Введите Enter')
                else:
                    print("Нехватает денег")
                    input('Введите Enter')
            if ch == 2:
                if sl4 > 0:
                    sl4 = sl4-1
                    money = money+rc4
                    print("Вещь продана")
                    input('Введите Enter')
                else:
                    print("У тебя нету этой вещи")
                    input('Введите Enter')

        if v == 5:
            print("1 Купить")
            print("2 Продать")
            ch = int(input())
            if ch == 1:
                if money >= rc5:
                    sl5 = sl5+1
                    money = money-rc5
                    print("Вещь куплена")
                    input('Введите Enter')
                else:
                    print("Нехватает денег")
                    input('Введите Enter')
            if ch == 2:
                if sl5 > 0:
                    sl5 = sl5-1
                    money = money+rc5
                    print("Вещь продана")
                    input('Введите Enter')
                else:
                    print("У тебя нету этой вещи")
                    input('Введите Enter')
        rt = random.randint(1, 100)
        if rt < 18:
            ask += 1
            print(red+"Ваш уровень розыска увеличелся!"+white)
            input('Введите Enter')


