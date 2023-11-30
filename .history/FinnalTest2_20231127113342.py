for cock in range(1,20):
    for hen in range(1,33):
        for chick in range(1,100): 
            if (cock + hen + chick) == 100 and (cock*5 + hen*3 + chick/3) == 100:
                  print("公鸡%d只，母鸡%d只，小鸡%d只。"%(cock,hen,chick))