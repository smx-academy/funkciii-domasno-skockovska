#1. Da se kreira funkcija so ime pecati_zdravo koja ke prima parametar ime i da se pecati poraka so pozdrav zaedno so imeto koe e isprateno kako parametar. 
# Imeto da go vnese korisnikot.

"""def pecati_zdravo(ime):
    print("Zdravo {}" .format(ime))

korisnik = input("Vnesete go vaseto ime ")
pecati_zdravo(korisnik)

#2. Da se kreira funkcija so ime zbir koja ke prima dva broevi kako parametar, da se presmeta zbirot i da se ispecati dali zbirot e paren ili ne paren. 
# Broevite da gi vnese korisnikot.

def zbir(a,b):
    zbir = a + b
    print("Zbirot na broevite iznesuva " ,zbir)
    return zbir

a = int (input("Vnesete go prviot broj "))
b = int (input("Vnesete go vtoriot broj "))


zbir1 = zbir(a,b)

if zbir1%2 == 0:
    print("Zbirot e paren broj")
else:
    print("Zbirot e neparen broj")

#3. Da se kreira funkcija so ime najgolem_broj koja ke prima 3 parametri, da se najde najgolemiot broj i da se ispecati. Broevite da gi vnese korisnikot

def maximum(a,b,c):
    list = [a,b,c]
    return max(list)

a = int (input("Vnesete go prviot broj "))
b = int (input("Vnesete go vtoriot broj "))
c = int (input("Vnesete go tretion broj "))
print("Najgolemiot broj e: " ,maximum(a,b,c))


#4. Da se kreira funkcija plostina i funkcija perimetar koi ke primaat dva paremtri, da presmetuvaat plostinata i perimetarot na pravoagolnik. 
# Korisnikot da gi vnesuva broevite i korisnikot da izbere koja presmetka da se izvrsi. DA NE SE IZVRSUVAAT DVETE

def plostina(a,b):
    plostinanapravoagolnik = a * b
    print ("Plostinata na pravoagolnikot iznesuva {} " . format(plostinanapravoagolnik))
    
    
def perimetar(a,b):
    perimetarnapravoagolnik = 2*a + 2*b
    print ("Perimetarot na pravoagolnikot iznesuva {} " . format(perimetarnapravoagolnik))
    
a = int (input("Vnesete ja prvata strana "))
b = int (input("Vnesete ja vtorata strana "))


funk = input ("Koja funkcija sakate da se izvrsi: plostina/perimetar? ")
if funk == "plostina":
    plostina(a,b)
elif funk == "perimetar":
    perimetar(a,b)

#5. Da se kreira funkcija koja ke prima eden parametar lista i da moze da presmeta prosek na listata

def average(): 
     x=a+b+c+d+e
     x=x/5
     

my_list =[ ]
for i in range (5):
    userInput = int(input("Vnesete broj: "))
    my_list.append(userInput)
    
average = sum(my_list)/len(my_list)
print ("Prosekot na listata e: {} ".format(average))

#6. Da se kreira funkcija so ime najdolgo ime koja ke prima lista kako parametar, da go njade najdolgoto ime od lista, 
# da go ispecati i da kaze od kolku parametri e sostaveno. Korisnikot da gi vnesuva iminjata

def najdolgoime(nekoj_txt):
    br_karakteri = len(nekoj_txt)
    return br_karakteri

my_list =[ ]
for i in range (5):
    ime = input ("Vnesete go vaseto ime: ")
    my_list.append(ime)


br_karakteri_ime = najdolgoime(ime)

# ne znam kako da ja proveram listata koe ime e najdolgo

#7. Da se napravi funkcija koja ke presmetuva prosek na ucenik, otcenite da gi prima kako parametar vo lista. 
# Da ima druga funkcija koja kako parametri ke gi prima prosekot i imeto na ucenikot, ke presmetuva uspeh na ucenik spored prosekot i da ispecati so kakov uspeh e toj ucenik

def prosek (broevi):
    prosek = sum(broevi)/len(broevi)
    broevi = []

#tuka imam problem sto ne znam kako da gi dodavam vo ;lista so funkcija
"""
#8.Da se napravi funkcija koja kako parametar ke prima nekoj string i da proveri dali toj string e palindrom t.e. dali toj string se cita od dvete strani

def isPalindrome(s):
    return s == s[::-1]

s = input ("Vnesete go vasiot zbor za proverka: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
