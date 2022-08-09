baza = []

g1 = {}
g1['Tytuł'] = 'Minecraft'
g1['Rok wydania'] = 2007
g1['Gatunek'] = 'Surwiwal'
g1['Ocena graczy'] = 5.0
baza.append(g1)

g3 = {}
g3['Tytuł'] = 'CS:GO'
g3['Rok wydania'] = 2010
g3['Gatunek'] = 'FPS'
g3['Ocena graczy'] = 9.0
baza.append(g3)

g2 = {}
g2['Tytuł'] = 'Fortnite'
g2['Rok wydania'] = 2014
g2['Gatunek'] = 'Battle Royale'
g2['Ocena graczy'] = 10.0
baza.append(g2)

opcja = 0
while opcja != '12':
    if opcja == '0':
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        print('DOSTEPNE OPCJE:')
        print('1. Wyświetl nazwy wszystkich gier w bazie')
        print('2. Wyświetl wszystkie gry w bazie')
        print('3. Wyświetl TOP 5 gier w bazie')
        print('4. Wyświetl gry z gatunku')
        print('5. Dodaj grę do bazy')
        print('6. Edytuj grę w bazie')
        print('7. Usuń grę z bazy')
        print('8. Wyświetl informacje o grze')
        print('9. Oceń grę')
        print('10. Zapisz dane do pliku')
        print('11. Odczytaj dane z pliku')
        print('12. Zakończ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        opcja = input('Wybierz opcje: ')
        print('------------------------')

        #OPCJA 1
    elif opcja == '1':
        tytuly = []
        for gra in baza:
            tytuly.append(gra['Tytuł'])
        tytuly.sort()
        print(', '.join(tytuly))
        opcja = '0'

        #OPCJA 2
    elif opcja == '2':
        print('Tytuł - Rok wydania - Gatunek - Ocena graczy')
        #SORTOWANIE PO TYTULACH
        tytuly = []
        for gra in baza:
            tytuly.append(gra['Tytuł'])
        tytuly.sort()
        for tytul in tytuly:
            for gra in baza:
                if tytul == gra['Tytuł']:
                    print(gra['Tytuł'] + ' - ' + str(gra['Rok wydania']) + ' - ' + gra['Gatunek'] + ' - ' + str(gra['Ocena graczy']))
                else:
                    continue
        ###
        opcja = '0'

        #OPCJA 3
    elif opcja == '3':
        print('Tytuł - Rok wydania - Gatunek - Ocena graczy')
        oceny = []
        for gra in baza:
            oceny.append(float(gra['Ocena graczy']))
        oceny.sort()
        oceny.reverse()
        i=0
        top5=[]
        zaliczone = ''
        while i<=4:
            for gra in baza:
                if float(gra['Ocena graczy']) == oceny[i]:
                    if zaliczone.find(gra['Tytuł']) == -1:
                        zaliczone += gra['Tytuł']
                        top5.append(gra['Tytuł'] + ' - ' + str(gra['Rok wydania']) + ' - ' + gra['Gatunek'] + ' - ' + str(gra['Ocena graczy']))
                    else:
                        continue
            i+=1
        for i in range(0,5):
            print(top5[i])
        opcja = '0'
        ###

        #OPCJA 4
    elif opcja == '4':
        gatunek = input('Podaj gatunek, z którego gry chcesz zobaczyć: ')
        print('Gry z gatunku ' + gatunek + ':')
        gry_z_gatunku = []
        for gra in baza:
            if gra['Gatunek'] == gatunek:
                gry_z_gatunku.append(gra['Tytuł'])
        gry_z_gatunku.sort()
        if len(gry_z_gatunku) == 0:
            print('Brak gier z podanego gatunku')
        else:
            print(', '.join(gry_z_gatunku))
        opcja = '0'
        ###

        #OPCJA 5
    elif opcja == '5':
        print('---DODAJ GRĘ---')
        print('Zamiast spacji użyj "_"')
        title = input('Podaj tytuł: ')
        year = input('Podaj rok wydania: ')
        sort = input('Podaj gatunek: ')
        game = {}
        game['Tytuł'] = str(title)
        game['Rok wydania'] = int(year)
        game['Gatunek'] = str(sort)
        game['Ocena graczy'] = 0.0
        baza.append(game)
        opcja = '0'
        ###

        #OPCJA 6
    elif opcja == '6':
        print('Zamiast spacji użyj "_"')
        to_edit = input('Podaj tytuł gry, którą chcesz edytować: ')
        game2 = {}
        check = 0
        for gra in baza:
            if gra['Tytuł'] == to_edit:
                game2_year = input('Zmień rok wydania: ')
                game2_sort = input('Zmień gatunek: ')
                gra['Rok wydania'] = int(game2_year)
                gra['Gatunek'] = game2_sort
                check = 1
                print('Zmienione dane o grze:')
                print(gra)
        if check == 0:
            print('Podana gra nie istnieje w bazie')
        opcja = '0'
        ###

        #OPCJA 7
    elif opcja == '7':
        print('Zamiast spacji użyj "_"')
        to_remove = input('Podaj tytuł gry, którą chcesz usunąć: ')
        check2 = 0
        for gra in baza:
            if gra['Tytuł'] == to_remove:
                baza.remove(gra)
                check2 = 1
        if check2 == 0:
            print('Podana gra nie istnieje w bazie')
        opcja = '0'
        ###

        #OPCJA 8
    elif opcja == '8':
        print('Zamiast spacji użyj "_"')
        to_search = input('Podaj tytuł gry, którą chcesz zobaczyć: ')
        check4 = 0
        for gra in baza:
            if gra['Tytuł'] == to_search:
                print(gra)
                check4 = 1
        if check4 == 0:
            print('Podana gra nie istnieje w bazie')
        opcja = '0'
        ###

        #OPCJA 9
    elif opcja == '9':
        print('Zamiast spacji użyj "_"')
        to_evaluate = input('Podaj tytuł gry, którą chcesz ocenić: ')
        check3 = 0
        for gra in baza:
            if gra['Tytuł'] == to_evaluate:
                grade = input('Wystaw ocenę od 0 do 10: ')
                if float(grade) < 0 and float(grade) > 10:
                    print('Podano nieprawidłową wartość')
                else:
                    gra['Ocena graczy'] = float(grade)
                    check3 = 1
        if check3 == 0:
            print('Podana gra nie istnieje w bazie')
        opcja = '0'
        ###

        #OPCJA 10
    elif opcja == '10':
        zapis = open('gry.txt', 'w')
        do_zapisu = []
        for gra in baza:
            do_zapisu.append(gra['Tytuł'])
            do_zapisu.append(gra['Rok wydania'])
            do_zapisu.append(gra['Gatunek'])
            do_zapisu.append(gra['Ocena graczy'])
            txt = str(do_zapisu).replace("[", "").replace("]", "").replace(" ", "").replace("'", "") + '\n'
            zapis.write(txt)
            do_zapisu.clear()
        zapis.close()
        print('Zapis zakończony powodzeniem')
        opcja = '0'
        ###

        #OPCJA 11
    elif opcja == '11':
        plik = open('gry.txt', 'r')
        tresc = plik.readlines()
        baza.clear()
        for line in tresc:
            lista = line.strip().split(',')
            baza.append({'Tytuł': lista[0], 'Rok wydania': lista[1], 'Gatunek': lista[2], 'Ocena graczy': lista[3]})
        plik.close()
        print('Odczyt zakończony powodzeniem')
        opcja = '0'

    else:
        print('Nie ma takiej opcji')
        opcja = '0'
