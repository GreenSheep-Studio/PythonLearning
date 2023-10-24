Input_str = input()
List1 = [Name.strip() for Name in Input_str.split(',')]
Dict = {}
for Name in List1:
    if Name in Dict:
        Dict[Name] += 1
    else:
        Dict.update({Name: 1})
for Name, Count in Dict.items():
    print(f"{Name}:{Count}")