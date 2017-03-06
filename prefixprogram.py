a = "deci"
def prefix(a):
    if a == "deci":
        return("0,1")
    elif a == "centi":
        return("0,01")
    elif a == "mili":
        return("0,001")
    elif a == "mikro":
        return("0,000001")
    elif a == "nano":
        return("0,000000001")
    elif a == "piko":
        return("0,000000000001")
    elif a == "deka":
        return("10")
    elif a == "hekto":
        return("100")
    elif a == "kilo":
        return("1000")
    elif a == "mega":
        return("1000000")
    elif a == "giga":
        return("1000000000")
    elif a == "tera":
        return("1000000000000")
    else:
        return("Nincs ilyen prefix")
