import pickle
import random
from tryb_walki import fight
from wczytywanie_zapisków import loading
from add_points import add_points


print(''' 
############..############..#####.......###..###......###
############..############..###.##......###..###......###
############..##............###..##.....###..###......###
###..##..###..############..###...##....###..###......###
###......###..############..###....##...###..###......###
###......###..##............###.....##..###..###......###
###......###..############..###......##.###..###......###
###......###..############..###.......#####..############''')
print('1. Nowa gra')
print('2. Wczytaj grę')
print('3. Wyjdź z gry')

menu_choice = 0
new_game=1
load_game=2
end_game=3
minimum_menu_choice=1
maximum_menu_choice=3
while not (menu_choice >= minimum_menu_choice and menu_choice <= maximum_menu_choice):
  try:
    menu_choice = int(input('Wpisz numer zadania które chciałbyś wykonać:'))
  except:
    print('Wpisz numere od 1 do 3')


if menu_choice == new_game:

  print('''
  #..#.###..####.#####.#####.####.###.
  #.#..#.#..##...#...#...#...#..#.#.#.
  ##...###..####.#####...#...#..#.###.
  #.#..#.#..#....#...#...#...#..#.#.#.
  #..#.#..#.####.#...#...#...####.#..#
  ....................................
  ###.####.####.#####.#####.####.#....
  #.#.#..#.#......#...#...#.#....#....
  ###.#..#.####...#...#####.#....#....
  #...#..#....#...#...#...#.#....#....
  #...####.####...#...#...#.####.#....''')



  min_choice_race=1
  max_choice_race=4
  save = open('game_save', 'wb')
  name = input('Wpisz swój nick')
  choice_race = 0
  while not (choice_race >= min_choice_race and choice_race <= max_choice_race):
    while True:
      try:
        choice_race = int(input('''Wpisz jedną z 4 cyferek- każda oznacza inną rasę:
      1-Wojownik                        2-Łucznik                      3-Mag                        4-Ninja
      - Posiada tarcze (10% szans         - atakuje z dystancu (3       - Może się leczyć (20%       - Jest bardzo zwinny (20%
        na obronę przed atakiem)            pierwsze ciosy w walce        szans na przywrócenie        na uniknięcie ciosu)
                                            są jego)                      punktów życia z zakresu    - pierwszy cios jest
                                                                            10 co atak)                zawsze jego
      - 150 punktow życia                 - 80 punktów życia            - 50 punktów życia           - 120 punktów życia  
      - zadaje obrażenia z zakresu        - zadaje obrażenia z zakresu  - Zadaje obrażenia z zakresu - Zadaje obrażenia z                           
        8-10                                12-15                         15-20                        zakresu 10-12     '''))

      except:
        print("Wpisz liczbę z zakresu od 1 do 4, potwierdź enterem")
      break
  warrior=1
  archer=2
  wizard=3
  if choice_race == warrior:
    race = [name, 'wojownik', 150, [8, 10], 10, 0, 0, 1]#nazwa,klasa, hp, obrażenia, szansa na unik, szansa na leczenie, leczone punkty, poziom
  elif choice_race == archer:
    race = [name, 'łucznik', 80, [12, 15], 0, 0, 0, 1]
  elif choice_race == wizard:
    race = [name, 'mag', 50, [15, 20], 0, 20, 10, 1]
  else:
    race = [name, 'ninja', 120, [10, 12], 20, 0, 0, 1]
  pickle.dump(race, save)
  save.close()
  save= open ('game_save', 'rb')
  all_saves = pickle.load(save)
  
  input('Wciśnij enter, jeżeli jesteś gotowy na pierwszą misję')




elif menu_choice == load_game:
  
  save = open('game_save', 'rb')
  all_saves = pickle.load(save)

  


  print (loading(all_saves))
  input('enter')



if all_saves [7] == 1 :
  input ('Witaj na pierwszej misji, aby przejść dalej wciśnij (enter)')
  input('Pracujesz w służbie u króla, a ta misja ma za zadanie przeszkolić Cię do prawdziwej walki, (enter)')
  input ('Pierwsze wyzwanie: (enter)')
  input('Pokonaj trenera(enter)')
  trener=['Trener', 'wojownik', 20, [2,5],30, 0, 0]


  print(fight(all_saves, trener))
  
  save.close()

  if trener[2]<=0:
    save = open('game_save', 'r+b')
    all_saves = pickle.load (save)
    all_saves[7]+=1
    input('Okej- szkolenie zakończone')
    print('Otrzymujesz 5 punktów do rozdania do swoich umiejętności. Co chciałbyś ulepszyć?')
    print(add_points(5, all_saves))
    print(all_saves)
    save.close()
    












