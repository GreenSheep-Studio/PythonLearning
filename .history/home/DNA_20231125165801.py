def translateDna(dnaStr):
    rnaStr = []
    for s in dnaStr:
        if s == "A" or s == "C" or s == "G":
            rnaStr.append(s)
        elif s == "T":
            rnaStr.append("U")
        else:
            return "非DNA数据"
    return "".join(rnaStr)
def main ():
    dnaStr = input()
    rnaStr = translateDna(dnaStr)
    if rnaStr == "非DNA数据":
        print(rnaStr)
    else:
        print(f"{dnaStr}=>{rnaStr}")
if __name__ == "__main__":
    main ()