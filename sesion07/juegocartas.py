from carta import Carta,Tipo

carta01 = Carta("Pikachu",15,20,Tipo.ELECTRICO)
# print(f"Mi carta tiene {carta01.__defensa} ptos de vida") ERROR
vidaPikachu=carta01.quitarVida(5)
print(f"Pikachu tiene {vidaPikachu} ptos de vida")
vidaPikachu+=10
#carta01.__defensa = 10000 ERROR

#print(f"Mi carta tiene {carta01.defensa} ptos de vida")
carta01.printCarta()

carta02 = Carta("Charizard",20,10)
carta02.printCarta()

carta03 = Carta("Mothim")
carta03.printCarta()

carta04 = Carta(nombre="Togekiss",defensa=15)
carta04.printCarta()
carta04.printCartaDeveloper()