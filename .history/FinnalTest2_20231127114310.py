plans = [{"area":"居住用地","rate": 21.40},

        {"area":"公共设施用地","rate":24.50},

        {"area":"工业用地","rate": 2.00},

        {"area":"道路广场用地","rate": 25.20},

        {"area":"绿地","rate":24.10}

        ]

area = input()

isFound = __________(1) __________

 

for p in plans:

    if p["area"] == __________(2) __________:

        isFound = True

        print("%s占比：%.2f__________(3) __________"%(__________(4) __________,p["rate"]))

       #【提醒】__ (3)__用于输出"%"   

        break

if isFound ==False:

    print("__________(5) __________")