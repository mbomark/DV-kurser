 
användare = {'a':'1', 'b':'2', 'c':'3'}
    
saker = {'a':["fanta", "pepsi"],'b': [],'c': [] }

def inlogg():                               #function för inlogg               
    global login
    login = str(input("användarnamn: "))
    #print(login)
    
    if login == användare:                  #finns användarnamn?
                                #använder == istället för 'in' så att den ska vara exakt

        global lösen
        lösen = input("lösenord: ")
        #print(lösen)

        if lösen == användare[login]:           #stämmer lösenordet?
            #print (lösen)

            
            meny()

        else:
            print("fel lösenord")
            inlogg()

        
        
    else:
        print("användare finns inte")           #om användare inte finns
        inlogg()

def meny():                             #meny för användare med olika alternativ
                print("1. lista saker")
                print("2. lägg till saker")
                print("3. logga ut")
                #global val
                val = str(input("välj: "))
    
                if val == "1":                        #printar användarens sake
r
                    for n in range(len(saker[login])):
                        print(saker[login][n])

                    meny()
                elif val == "2":                      #läggertill saker

                    
                    läggtill()

                elif val == "3":                  #loggaut
                    print(val)
                    inlogg()

                else:                           #ej alternativ som input
                    meny()
                    

def läggtill():
                        print("avsluta: skriv quit")
                        global nysak
                        nysak = str(input("lägg till: "))
                        if nysak == "quit":
                            meny()
                        else:
                            saker[login].append(nysak)
                            print(saker.get(login))
                            meny()

        
inlogg()

