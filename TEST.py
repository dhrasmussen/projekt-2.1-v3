#https://www.tutorialspoint.com/python/python_files_io.htm


if __name__ == "__main__":
    File_navn=input("Indtast navnet på opgaven! ")
    f = open(File_navn, "w") #Filen oprettes og hvis der eksistere en i forvejen overskrives den!

    string1=input("Ansvarlig: ")
    string1=File_navn+"\n"+"Ansvarlig: "+string1+"\n" # \n laver en ny line i filen
    f.write(string1) #string1 skrives til filen
    f.close() # Filen lukkes ned

#    f = open(File_navn, "a") # Filen åbnes og nu kan der adder noget tekst til den
#    string1=input("Single Mode: ")
#    string1=string1+"\n" # \n laver en ny line i filen
#    f.write(string1)

#    string2=input("Multi Mode: ")
#    string2=string2+"\n" # \n laver en ny line i filen
#    f.write(string2)

#    string3=input("Udgravningspris: ")
#    string3=string3+"\n" # \n laver en ny line i filen
#    f.write(string3)
#    f.close()
