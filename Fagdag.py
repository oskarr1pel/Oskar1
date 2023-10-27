                                      ### TEGNING AV GRAFER ###




                ### Enkel graftegning ###
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

xverdier = [2,4,6]      #x-verdiene til grafen
yverdier = [3,6,9]      #y-verdiene til grafen

plt.plot(xverdier,yverdier)          #For å vise funksjonen må man alltid avslutte programmet med plt.plot(verdier) og plt.show()
plt.show()
"""
"""
def f(x):           #For å finne punkter i en funksjon bruker vi append sammen i en løkke 
    return x**2

xverdier = []
yverdier = []

for xverdi in range(10):
    xverdier.append(xverdi)
    yverdier.append(f(xverdi))

plt.plot(xverdier,yverdier)
plt.show()
"""
"""
def f(x):           #Annen versjon av funksjonen ovenfor, hvor vi her bruker lispace of numpy. 
    return x**2

xverdier = np.linspace(0, 10, 11)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()
"""
#Oppgave 1
"""
#For at funksjonen ovenfor skal bli totalt glatt, burde 100 verdier holde fra x=0 til 10
def f(x):           
    return x**2

xverdier = np.linspace(0, 10, 101)  #utvider til 100
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)   #Når vi skriver ut grafen ser den nokså smud og glatt ut!
plt.show()
"""
#Oppgave 2
#a)b)c)d)
"""¨

def f(x):               #Metode 1 for å tegne grafen fra -2 til 2
    return 4*x**3-x**5

xverdier = np.linspace(-2, 2, 50)   #For å endre på antall punkter vi plotter inn må vi endre på det siste tallet bak linspace()
yverdier = f(xverdier)

plt.plot(xverdier,yverdier)
plt.scatter(xverdier,yverdier)
plt.show()

###

def f(x):               #Metode 2 for å tene grafen fra -2 til 2
    return 4*x**3-x**5

xverdier = []
yverdier = []

for xverdi in range(-2,2):
    xverdier.append(xverdi)
    yverdier.append(f(xverdi))

plt.plot(xverdier,yverdier)
plt.scatter(xverdier,yverdier)
plt.show()
"""


                ### Tilpasse grafer
"""
#For å legge til design på graf må vi introdusere nye begreper 
def f(x):
    return x**2

xverdier = np.linspace(0, 10, 50)
yverdier = f(xverdier)

plt.plot(xverdier,yverdier)

plt.grid()              #.grid brukes for å lage et gitter med enhetene, slik som i Geogebra
plt.title("Funksjonen $f(x)=x^2")           #.title settes over funksjonen som tittelen av hva som blir printet ut. Man bruker også $ når vi skriver mattematikk
plt.xlabel("$x")            #.xlabel brukes for å definere x-aksen sitt navn som da er $x 
plt.ylabel("$y")            #.ylabel brukes for å definere y-aksen sitt navn som da er $y
plt.xlim(0, 10)             #.xlim brukes for å definere hvilke x-verdier som skal være synlige på grafen, altså fra x=0 til 10
plt.ylim(0,150)             #.ylim brukes for å definere hvilke y-verdier som skal være synlige på grafen, altså fra y=0 til 150

plt.show()              #.show viser som sagt funksjonen og all print og design rundt den
"""
"""
#Litt flere begreper og moduler som vi kan bruke for designet på en funksjon, litt unødvendig 
xverdier = np.linspace(-2, 2, 20)
yverdier = xverdier**5

plt.axhline(0, color="black", zorder=0)
plt.axvline(0, color="black", zorder=0)
plt.plot(xverdier, yverdier, color="coral", linestyle="dashed", zorder=1)
plt.scatter(xverdier, yverdier, color="skyblue", marker="D", zorder=2)
plt.grid()

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
"""
"""
#Oppgave 3a)b)
def f(x): 
    return 2*x-3
xverdier = np.linspace(0, 10, 100)
yverdier = f(xverdier)

print(plt.style.available)           #printer ut de innebygde tilgjengelige stilene 

plt.grid()
plt.plot(xverdier, yverdier, color="coral", linestyle="dashed", zorder=1)
plt.scatter(xverdier,yverdier)
plt.show()
"""
"""
#Oppgave 4
#For å skrive flere grafer i samme figur må vi introdusere subplot
#For å sette de to grafene sammen i samme figur, må subplottet være likt på begge. 
xverdier = np.linspace(0, 20, 50)

#Graf 1:
yverdier = 0.5*xverdier**2
plt.subplot(1, 1, 1)
plt.plot(xverdier, yverdier)

#Graf 2: 
yverdier = -0.3*xverdier**3
plt.subplot(1, 1, 1)                
plt.plot(xverdier, yverdier)

plt.show()
"""
"""
#Oppgave 5
#For å skrive alle 4 funksjonene i samme figur starter vi med å definere alle 4, og så y-verdiene deres
def f1(x):
    return 2*x+1
def f2(x):
    return x**2-3
def f3(x):
    return 2**(x)
def f4(x):
    return x/3
#Regner ut tilførende y-verdier til hver funksjon  
x = np.linspace(-10, 10, 400)
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)
y4 = f4(x)

plt.figure(figsize=(8,6))            #Tegn grafene 

plt.plot(x, y1, label='y = 2x+1')
plt.plot(x, y2, label='y = x^2-3')
plt.plot(x, y3, label='y = 2^x')
plt.plot(x, y4, label='y = x/3')

plt.xlabel('x-akse')
plt.ylabel('y-akse')
plt.title('Grafer til fire funksjoner i samme figur')
plt.legend()            #Viser grafisk forklaring basert på 'label' i plt.plot()

plt.grid(True)
plt.show()
"""
"""
#Oppgave 6
#for å representere tallene under i en graf må vi plotte den inn. 
aarstall = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
antall = [4478497, 4503436, 4524066, 4552252, 4577457, 4606363, 4640219, 4681134, 4737171, 4799252, 4858199, 4920305, 4985870, 5051275, 5109056, 5165802, 5213985, 5258317, 5295619, 5328212, 5367580, 5391369, 5425270]
xverdier = aarstall
yverdier = antall

plt.grid()
plt.xlabel('årstall')
plt.ylabel('antall')
plt.plot(xverdier, yverdier)
plt.show()
"""
"""
#For å representere tabeller og diagrammer bruker vi bar eller barh
utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

plt.figure(figsize=(10, 5))
plt.subplots_adjust(0.4)
plt.barh(utdanningsprogram, antall)  # Lager stolpediagrammet
plt.title("Søkertall fordelt på yrkesrettede utdanningsprogrammer i 2021")
plt.grid(axis="y")  # Legger til rutenett (bare horisontale linjer)
plt.show()          # Viser diagrammet
"""
"""
#Oppgave 7 
Land = [
    "Kina", 
    "Japan", 
    "Tyskland", 
    "USA", 
    "Sør-Korea"
    "India", 
    "Spania", 
    "Mexico", 
    "Brazil", 
    "Storbritania"
]
Antall= [24420744, 7873886, 5746808, 3934357, 3859991, 3677605, 2354117, 1993168, 1778464, 1722698]

plt.figure(figsize=(10,5))
plt.subplots_adjust(0.2)
plt.barh(Land, Antall)  #Lager stolpediagrammet
plt.title('Top 10 bil produksjonsland')
plt.grid(axis="y")
plt.xlabel('antall biler')
plt.show()
"""
              











                                    ### DATABEHANDLING, CSV-FILER OG JSON ###

import csv

# Prøv å åpne CSV-filen og lese dataene. Hvis det oppstår en feil, skriv ut en feilmelding.
try:
    with open('Prosjekter/omsetning.csv', 'r', encoding="ISO-8859-1") as file:
        reader = csv.DictReader(file, delimiter=';')
        max_omsetning = 0
        max_naring = ''
        
        # Loop over radene i CSV-filen og finn den bransjen med høyest omsetning i 2019
        for row in reader:
            omsetning_2019 = row['Omsetning (mill. kr) 2019']
            if omsetning_2019 == '':  # Hopp over tomme rader hvis det finnes noen
                continue
            try:
                omsetning_2019 = float(omsetning_2019.replace(',', '.'))
            except ValueError:
                print(f'Ugyldig verdi for omsetning i 2019 i rad {reader.line_num}: {omsetning_2019}')
                continue
            if omsetning_2019 > max_omsetning:
                max_omsetning = omsetning_2019
                max_naring = row['næring (SN2007)']
        
        if max_naring != '':
            print(f"{max_naring} var bransjen med høyest omsetning, med {max_omsetning} millioner kroner i 2019.")
        else:
            print('Ingen omsetningsdata funnet i CSV-filen.')
except FileNotFoundError:
    print('CSV-filen ble ikke funnet på angitt sti.')
except csv.Error:
    print('Det oppsto en feil under lesing av CSV-filen.')
except Exception as e:
    print(f'En uventet feil oppsto: {e}')