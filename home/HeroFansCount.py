Input_str = input()
NameList = [Name.strip() for Name in Input_str.split(',')]
Dict = {}
for Name in NameList:
    if Name:
        if Name in Dict:
            Dict[Name] += 1
        else:
            Dict[Name] = 1
    else:
        continue
result = "\n".join([i + ":" + str(Dict[i]) for i in Dict])
print(result, end="")