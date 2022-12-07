from math import *  #käsu paigutus oli vale

print("Ruudu karakteristikud") #pane f täht
a=float(input("Sisesta ruudu külje pikkus => ")) # muudetud , на * lisatud float
S=a**2 #eemaldatud osa
print("Ruudu pindala", round(S,1)) #
P=4*a
print("Ruudu ümbermõõt", (P,1))  #muudetud , на "
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #eemaldatud lisasulud
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # pane float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # pane float
S=b*c
print("Ristküliku pindala", round(S,1)) #postville "
P=2*(b+c) #pone *
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b*2+c*2) #eemaldatud  math
print("Ristküliku diagonaal", round(di,1)) # pane sulgud ja "
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) # pane " 
d=2*r #pane "
print("Ringi läbimõõt", round(d,1)) # eemaldatud D
S=pi*r**2 # () "
print("Ringi pindala", round(S,2))
C=2*pi*r #pane "
print("Ringjoone pikkus", round(C,2))
