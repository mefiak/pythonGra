def fight(player, opponent):
  import random
  nick1 = player[0]
  nick2 = opponent[0]

  print(nick1)
  print('...........VS...........')
  print('........................', nick2)
  input('Walka rozpocznie się po kliklnięciu entera')

  start = (random.randint(1, 2))

  if player[1] == 'łucznik' or start == 1:
    starter = player
    end = opponent


  else:
    starter = opponent
    end = player

  count = 0

  while starter[2] > 0 and end[2] > 0:
    count += 1
    miss1_random = int(random.randint(0, 100))
    miss2_random = int(random.randint(0, 100))
    miss1 = starter[4]
    miss2 = end[4]
    demage1 = random.randint(starter[3][0], starter[3][1])
    demage2 = random.randint(end[3][0], end[3][1])
    heal1_random = random.randint(0, 100)
    heal2_random = random.randint(0, 100)
    hp1 = starter[2]
    hp2 = end[2]
    prob_heal1 = starter[5]
    prob_heal2 = end[5]
    amount_heal1 = starter[6]
    amount_heal2 = end[6]

    print('atakuje', starter[0])

    if starter[1] == 'łucznik' and count <= 3:
      if miss2_random <= miss2:
        print('unik')
        demage1 == 0
        continue
      else:
        end[2] -= demage1
        continue


    else:
      if miss2_random <= miss2:
        print('unik')
        demage1 == 0

        if heal1_random <= prob_heal1:
          hp1 += amount_heal1
      else:
        end[2] -= demage1

        if heal1_random <= prob_heal1:
          hp1 += amount_heal1

      if miss1_random <= miss1:
        print('unik')
        demage2 == 0

        if heal2_random <= prob_heal2:
          hp2 += amount_heal2


      else:
        starter[2] -= demage2

        if heal2_random <= prob_heal2:
          hp2 += amount_heal2

      print(starter[0], '-', demage2)
    if heal2_random <= prob_heal2:
      print('+', amount_heal1)
    print(starter[0], 'pozostało', hp1, 'punktów życia')
    print(end[0], '-', demage1)
    if heal2_random <= prob_heal2:
      print('+', amount_heal2)
    print(end[0], 'pozostało', hp2, 'punktów życia')
    input('kliknij enter, żeby rozpocząć kolejną wymianę ciosów')


    print(starter[0], 'pozostało', starter[2], 'punktów życia')
    print(end[0], 'pozostało', end[2], 'punktów życia')

  if hp1 <= 0 and hp2 <= 0:
    print('Remis')
  elif hp1 <= 0 and hp2 >= 0:
    print('Wygrał', opponent[0])
  else:
    print('Wygrał', player[0])