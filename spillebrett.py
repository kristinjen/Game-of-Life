"""
Dette programmet definerer klassen Spillebrett. Objekter av denne klassen tar to
parametre: antall rader og antall kolonner. Hvert felt på "brettet" inneholder 
en celle, som er et objekt av klassen Celle. En celle kan være levende eller 
død. Selve rutenettet blir opprettet i konstruktøren, ved hjelp av en nøstet
for-løkke. I tillegg har den en generasjonsvariabel, som holder på brettets 
generasjon i form av en tallvariabel. Den første metoden er tegnBrett, som
viser brettet i terminalen, samt skriver hvor mange levende celler brettet har 
og hvilken generasjon det er. Antall levende celler kommer fra metoden 
finnAntallLevende, som ved hjelp av nøstet for-løkke teller opp hvor mange 
av cellene i brettet som lever. Metoden _generer er den som endrer cellenes
status, med 1/3 sjanse for å leve. Fordi den kalles i konstruktøren vil det skje 
idet objektet opprettes. Neste metode er finnNabo. Denne går alle naboene til 
en celle på en gitt posisjon og returnerer en liste med alle nabo-cellene. Ved 
hjelp av flere if-sjekker unngår metoden å legge til ugyldige indekser. Den 
siste metoden er oppdatering. Denne metoden går gjennom celle for celle i 
brettet og sjekker ved hjelp av finnNaboer om cellen har for få eller for 
mange levende naboer til å leve selv (under- eller overpopulasjon), eller om 
skal fortsette å leve/vekkes til live. Deretter endrer metoden cellenes status
i henhold til disse reglene. Til slutt oppdaterer den generasjonsvariabelen. 

"""

from celle import Celle
#brukes til å ha celler på brettet som kan være levende og døde
from random import randint
#brukes til å fylle brettet med celler som har 1/3 sjanse for å være levende



class Spillebrett:
    def __init__(self, rad, kolonne):   #to parametre: antall rader og kolonner
        self._rader = rad
        self._kolonner = kolonne

        self._rutenett = []             #opprettelsen av rutenettet
        for x in range(self._rader):
            self._rutenett.append([])   #radene opprettes
            for y in range(self._kolonner): 
            #antall celler i hver rad = kolonner
                self._rutenett[x].append(Celle())   #celler blir fylt inn

        self._generasjon = 0            #generasjonsvariabel
        self._generer()                 #cellene endres til levende, 1/3 sjanse

    def tegnBrett(self):                #denne metoden skriver ut brettet 
        for rad in self._rutenett:      #nøstet forløkke
            for celle in rad:
                print(celle.hentStatusTegn(), end="")
            print() #denne tomme printen sørger for at brettet blir firkanta
        #følgende print-setning skriver ut generasjon og antall levende celler
        print(f"Generasjon: {self._generasjon} – Antall levende celler: {self.finnAntallLevende()}")
        
    def finnAntallLevende(self):        #finner antall levende celler i brettet
        teller = 0                      
        for rad in self._rutenett:      #nøstet løkke
            for celle in rad:           #sjekker hver celle
                if celle.erLevende() == 1:  
                    teller += 1         #hvis den er levende, går telleren opp
        return teller                   #telleren returneres
    
    def _generer(self):
        #generer endrer cellenes status når spillebrett-objektet opprettes   
        #cellene har 1/3 sannsynlighet for å bli satt til levende
        #dette gjøres ved at randint velger et tilfeldig tall mellom 1 og 3
        for rad in self._rutenett:      #nøstet løkke
            for celle in rad:           #for hver celle velger randint et tall
                tall = randint(1, 3)    #tallene er 1, 2 eller 3
                if tall == 1:           #hvis tallet er en, blir status levende
                    celle.settLevende()
                
    def finnNabo(self, rad, kol):       #returnerer naboene til en gitt celle
        naboer = []
        #naboene er de som er over, under, ved siden og diagonalt ut fra cellen
        for x in range(-1, 2):          #nøstet løkke for å nå inn til cellene
            for y in range(-1, 2):      
                naboRad = rad + x       #raden plusses med -1, 0 og +1
                naboKol = kol + y       #kolonnen plusses med -1, 0 og +1
                
                gyldig = True           #man antar at naboen er "ekte"
                
                #denne if-sjekken ser om naboen er cellen selv
                if naboRad == rad and naboKol == kol:
                    gyldig = False
                
                #følgende to if-sjekker ser om naboen eksisterer
                #hvis den er på en rad som ikke finnes, blir gyldig False
                if naboRad >= self._rader or naboRad < 0:
                    gyldig = False      #hvis "naboen" er på uekte rad

                #her sjekkes om indeks/kolonne ikke eksisterer
                if naboKol >= self._kolonner or naboKol < 0:
                    gyldig = False
                
                #hvis den ikke er seg selv, og ikke er på en ugyldig plass i 
                #rutenettet, blir den lagt til i nabolisten
                if gyldig:  
                    naboer.append(self._rutenett[naboRad][naboKol])
        
        return naboer                   #nabolisten returneres
        
    def oppdatering(self):              #denne metoden lager en ny generasjon
        recover = []                    #liste over celler som skal "vekkes"
        kill = []                       #liste over celler som skal drepes
        
        #en nøstet for-løkke går gjennom alle posisjoner i rutenettet
        #jeg kaller gjeldende posisjon for hovedcellen
        for x in range(len(self._rutenett)):    
            for y in range(len(self._rutenett[x])):    
                
                alive = []  #liste hvor levende naboer legges
                
                #naboene til hovedcellen hentes med finnNabo
                naboene = self.finnNabo(x, y) 
                
                for elem in naboene:          #en for-løkke går gjennom naboer   
                    if elem.erLevende():      #status-sjekk på hver nabo 
                        alive.append(elem)    #levende naboer legges i alive
                
                #følgende if-sjekk ser om hovedcellen er levende
                if self._rutenett[x][y].erLevende() is True:
                    #har hovedcellen for få eller for mange levende naboer?
                    if len(alive) < 2 or len(alive) > 3:
                        #da må den dø
                        kill.append(self._rutenett[x][y])
                
                #hvis hovedcellen er død fra før...
                if self._rutenett[x][y].erLevende() == False:
                    #...sjekkes det om den har tre levende naboer...
                    if len(alive) == 3:
                        #...da blir den vekket til live
                        recover.append(self._rutenett[x][y])        
        
        #for å unngå at cellene endres underveis og skaper krøll, blir 
        #de bare lagt til i en liste som endrer statusen deres her til slutt
        for celle in recover:
            celle.settLevende()
        
        for celle in kill:
            celle.settDoed()
        
        #når alt dette er gjort, økes generasjonstelleren med 1
        self._generasjon +=1
        



