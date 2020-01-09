"""
Dette programmet tar i bruk spillebrett-klassen for å opprette et objekt. 
Brukeren blir bedt om antall rader og kolonner, og dette blir brukt til å
opprette objektet. Deretter printes brettet ved hjelp av tegnBrett-metoden. 
Simuleringen utspiller seg ved hjelp av en while-løkke, hvor bruker kan taste 
inn enter for å komme til neste generasjon, eller q for å avslutte. Cellene vil 
endre status til levende eller død avhengig av sine omgivelser. 

Programmet lar brukeren observere simuleringen generasjon for generasjon ved å 
tegne opp spillebrettet i terminalen sammen med tilleggsinformasjon om hvilken
generasjon vi serpå samt hvor mange celler som for øyeblikket lever.
"""

from spillebrett import Spillebrett     #spillebrett-klassen importeres

def main(): 
    
    #her blir bruker bedt om hvor mange rader og kolonner hen ønsker
    #dette lagres i hver sin variabel
    antallrader = int(input("Hvor mange rader vil du ha?: "))
    antallkolonner = int(input("Hvor mange kolonner vil du ha?: "))
    
    #variablene blir brukt til å opprette et objekt av spillebrett-klassen
    brett1 = Spillebrett(antallrader, antallkolonner)
    #brettes printes ved hjelp av tegnBrett-metoden
    brett1.tegnBrett()
    
    
    svar = 0          #setter svar-variabelen for at while-løkken skal starte
    
    while svar != "q":   
        svar = input("Tast Enter for å fortsette, q for å avslutte: ")
        #brukeren får spørsmål om å fortsette eller avslutte
        #for å komme til neste generasjon må brukeren taste enter
        while svar == "":
            #hvis bruker taster enter blir brettet oppdatert og skrevet ut
            brett1.oppdatering()
            brett1.tegnBrett()
            #bruker blir spurt på nytt om å fortsette
            svar = input("Tast Enter for å fortsette, q for å avslutte: ")

main()


