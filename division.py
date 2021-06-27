# Detta är ett divisionsspel programmerat av Oskar Bork, Mars 2021

import random, time, pyinputplus

namn = ['Lisa', 'Abdullah', 'Oskar', 'Maja', 'Rektorn', 'Leo', 'En liten katt', 'En sengångare', 'Råttan Alfred', 'Tomten'
, 'Vaktmästaren', 'Maggan', 'Pjotr', 'Frans Perietti', 'Kungen', 'Tilde', 'Thomas', 'Sara']
subjektiv = ['stolar', 'tärningar', 'chokladbitar', 'ostar', 'äpplen', 'muffinsar', 'radiostyrda flygplan', 'bananer', 'tallrikar'
, 'röda små bollar', 'potatisar', 'plättar', 'söndriga lampor', 'diskmaskiner', 'rymdfarkoster', 'glassbåtar', 'äppelskruttar', 'skedar']
rättSvarFraser = ['Helt rätt, snyggt jobbat!', 'Stämmer bra!', 'Imponerande, det är korrekt!', 'Nää, det blev inte helt rätt... Skoja bara, bra jobbat!', 'Wup wup, snyggt räknat!', 'Wow, du är ju grym på matte!'
, 'Du har koll på din division!', 'Oja! Helt rätt.']
tankeFraser = ['Ska bara hämta miniräknaren...', 'Då ska vi se...', 'Ska bara ta en sipp kaffe...', 'Startar upp tankenöten, en sekund bara...'
, 'Tänk, tänk, tänk...', 'Vänta lite bara...']   
nästaFrågaFras = ['Ok, här kommer en till.', 'Håll i dig, nu kommer nästa!', 'Alright, en till fråga beställd!', 'En till?!', 'Nä, dom är slut tyvärr... Skoja!', 'Comming right up!', 'En sekund bara...'
, 'En till, en till...', 'Tänk vad kul det är med matte va?', 'Då letar jag upp en till... Här!', 'Då ska vi se...', 'Vart la jag nu de där matteproblemen...', 'Hoppas de inte är slut. Vänta, här har jag en!']
räkneOrd = ['första', 'andra', 'tredje', 'fjärde', 'femte', 'sjätte', 'sjunde', 'åttonde', 'nionde', 'tionde', 'elfte', 'tolfte', 'trettonde'
, 'fjortonde', 'femtonde','sextonde', 'sjuttonde', 'artonde', 'nittonde', 'tjugonde']


print('Hej, välkommen till detta divisions-spel!\n')

antalFrågor = pyinputplus.inputInt('Hur många frågor ska det vara? ')
talUppTill = pyinputplus.inputInt('Maxtal för division: ')

# Variabler
antalRättSvar = 0
svåraTäljare = []
svåraNämnare = []

# Algoritm som tar fram primtal upp till maxtalet. 
primtalLista = [2]
ärPrimtal = False
for N in range(2, talUppTill):  
    for i in range(2, N):
        if N % i == 0:
            ärPrimtal = False
            break
        else:
            ärPrimtal = True
    if ärPrimtal:
        primtalLista.append(N)

# Main-loop TODO: gör om till forloop som 
for i in range(0,antalFrågor):
    print('\nHär kommer', räkneOrd[i], 'frågan:\n')
    time.sleep(0.5)

    täljare = random.randint(3,talUppTill) # Dra en random täljare
    urval_nämnare = [2,3,4,5,6] # Dra en random nämnare
    delbara_nämnare = [] # Listan som ska fyllas med möjliga nämnare
    felSvarUpptäckt = False # Nollställer triggern för fel svar

    if täljare in primtalLista:  # Tillåt inte primtal
        täljare = täljare + 1

    for i in urval_nämnare: # Skapa en lista med möjliga nämnare
        if täljare%i == 0:
            delbara_nämnare.append(i)

    nämnare = random.choice(delbara_nämnare)  # Dra en nämnare från listan

    # Skriv ut frågan med variablerna
    time.sleep(1)
    print(random.choice(namn),'har', täljare ,random.choice(subjektiv), 'och vill dela dem i', nämnare, 'lika stora högar. Hur många blir det i varje hög?')
    
    # Dessa fraser ligger här för att de ska kunna påverkas av vald täljare och nämnare 
    felSvarFraser = ['Bra försök, men inte helt rätt!', 'Oooh, nära!', 'Nope, det var inte helt rätt.', 'Jag kommer fram till något annat.', 'Hm, min miniräknare visar inte det.'
    , 'Det var nog bara ett slarvfel.', 'Jag låtsas som att jag inte såg det där svaret.', f'Hmm, {täljare} delat på {nämnare} blir något annat']

    # Spelarens input in en loop
    while True:
        svar = pyinputplus.inputNum('Svar: ') #inhämta svar
        time.sleep(0.3)
        print(random.choice(tankeFraser))
        time.sleep(1)
        print('...')
        time.sleep(0.5)

        if svar == int(täljare/nämnare): # vid rätt svar, bryt loopen
            if not felSvarUpptäckt: # Om felSvar triggern inte är triggad, ge poäng 
                antalRättSvar += 1
            break
        else: # Vid fel svar:
            print(random.choice(felSvarFraser))
            if not felSvarUpptäckt: # Lägger till talen som spelaren misslyckades på. Gör det bara en gång. 
                svåraTäljare.append(täljare)
                svåraNämnare.append(nämnare)                
            felSvarUpptäckt = True

            time.sleep(1)
            print('Pröva igen!')
    
    print(random.choice(rättSvarFraser))
    print()
    time.sleep(0.5)

# Efter alla frågor

# räkna upp antal rätt svar, ev. också procent 
print('Du fick rätt på', antalRättSvar, 'av', antalFrågor, 'frågor.')
print('Bra jobbat!\n')

svåraTal = zip(svåraNämnare, svåraTäljare) #Lägger in nämnarna och täljarna i en lista 

# Skriv ut vilka frågor som spelaren behövde fler än 1 försök på
if len(svåraNämnare) > 0: # Kollar om det finns några frågor som spelaren misslyckades på. 
    print('De frågor som du behövde fler än ett försök på var:')
    for n,t in svåraTal:
        print(t, '/', n, '=')

        
input('\nTryck för att avsluta... ')