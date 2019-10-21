#nazwa,klasa, hp, obrażenia, szansa na unik, szansa na leczenie, leczone punkty, poziom

def add_points(amount_points,character):
  print('Otrzymujesz', amount_points ,'punktów do rozdania do swoich umiejętności. Co chciałbyś ulepszyć?')
  minimum_number=1
  maximum_number=5
  number=0
  any_points=0 
  hp = int (character[2])
  minimal_hit = int (character[3][0])
  maximal_hit = int (character[3][1])
  miss_chance = int (character[4])
  heal_chance =int (character[5])
  amount_heal = int (character[6])


  while amount_points>any_points:
    print('masz', amount_points, 'punktów') 
    print('Jak narazie twoje umiejętności wynoszą: ')
    print('1. Punkty życia:', hp)
    print('2. Zadawane obrażenia:', minimal_hit, '-', maximal_hit)
    print('3. Szansa na unik:', miss_chance)
    print('4. Szansa na uleczenie:', heal_chance)
    print('5. Leczone punkty życia:', amount_heal)
    
    
    while not (number>=minimum_number and number<=maximum_number):
      
      while True :
        
        try:
          number=int(input('Wybierz numer rzeczy którą chciałbyś wzmocnić:'))
          print(character [number+1])
          break
        except IndexError:
          print ('wpisałeś złą liczbę')
        except ValueError:
          print('wpisz coś', 'albo przestań wpisywać tekst')
        except:
          print("znowu coś jest nie tak")
    
    
    while True:
      try:
        how_many=int(input('O ile?'))
        break
      except IndexError:
        print ('Wpisałeś złą liczbę')
      except ValueError:
        print('Wpisz coś', 'albo przestań wpisywać tekst')
      except:
        print("znowu coś jest nie tak")

    number_of_ability=number+1
    if how_many<=amount_points:
      amount_points-=how_many
      
      if number_of_ability==2:
        hp+=how_many

      
      elif  number_of_ability==3:
        minimal_hit+=how_many
        maximal_hit+=how_many
        
      
      elif number_of_ability==4:
        miss_chance+=how_many
      
      elif number_of_ability==5:
        heal_chance+=how_many

      elif number_of_ability==6:
        amount_heal+=how_many
    

    else:
      print ('masz za mało punktów')
  
  
  print ('nie masz już więcej punktów')
  print ('twoje umiejętności, to:')
  print('Punkty życia:', hp)
  print('Zadawane obrażenia:', minimal_hit, '-', maximal_hit)
  print('Szansa na unik:', miss_chance)
  print('Szansa na leczenie:', heal_chance)
  print('Leczone punkty życia:', amount_heal)
  return 
  
