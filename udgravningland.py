

#def undergrav

    nedgravning = 100 #kr pr m
    underboring = 1000 #kr pr m

    #taller=3

    print("")
    print("Du har valgt Kabel Nedgravning")
    print("Udfyld felterne her under med værdier")
    print("")
    grav = int(input("Indtast tallet for meter nedgravning: "))

    ubor = int(input("Indtast antal meter underboring: "))

    nedgrav = grav*nedgravning
    underbor = ubor*underboring
    totalpris = nedgrav+underbor

