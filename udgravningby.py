import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

tid=0.2
tid2=3
tid3=2

def place_value(number):
    return ("{:,}".format(number))

def gravby():


    Landsby = 300 #kr pr m
    Storby = 750 #kr pr m
    Landevej = 100 #kr pr m
    Underboring = 1000 #kr pr m


    taller=3

    time.sleep(tid)

    print("")
    print("Du har valgt kabelgedgravning")
    print("Udfyld felterne her under med værdier")
    print("")

    time.sleep(tid)

    vej = int(input("Indtast antal meter landevej: "))
    land = int(input("Indtast antal meter landsby: "))
    strby = int(input("Indtast antal meter storby: "))
    ubor = int(input("Indtast antal meter underboring: "))

    landevej = vej*Landevej
    landsby = land*Landsby
    storby = strby*Storby
    underboring = ubor*Underboring

    totalpris = landevej+landsby+storby+underboring

    time.sleep(tid)

    print("")
    print("Prisen for landevej", (place_value(landevej)),"kr")
    print("Prisen for landsby", (place_value(landsby)),"kr")
    print("Prisen for storby", (place_value(storby)),"kr")
    print("Prisen for underboring", (place_value(underboring)),"kr")
    print("")

    print(color.BOLD + "Samlet pris for kabelnedgravning", color.RED + place_value(totalpris) + color.END, color.BOLD + "kr inkl. moms" + color.END)
    print("")

    File_navn=input("Indtast projektnavnet")
    f = open(File_navn, "a") # Filen åbnes og nu kan der adder noget tekst til den
    string6=str(place_value(landevej))
    string6="\n"+"Prisen for landevej: "+string6+"kr inkl. moms"+"\n" # \n laver en ny line i filen
    f.write(string6)

    string7=str(place_value(landsby))
    string7="Prisen for landsby: "+string7+"kr inkl. moms" +"\n" # \n laver en ny line i filen
    f.write(string7)

    string8=str(place_value(storby))
    string8="Prisen for storby: "+string8+"kr inkl. moms" +"\n" # \n laver en ny line i filen
    f.write(string8)

    string9=str(place_value(underboring))
    string9="Prisen for underboring: "+string9+"kr inkl. moms" +"\n" # \n laver en ny line i filen
    f.write(string9)

    string10=str(place_value(totalpris))
    string10="Samlet pris for kabelnedgravning: "+string10+"kr inkl. moms" +"\n" # \n laver en ny line i filen
    f.write(string10)
    f.close()
    print("------------------------------------------------------------------------")
    time.sleep(tid3)
