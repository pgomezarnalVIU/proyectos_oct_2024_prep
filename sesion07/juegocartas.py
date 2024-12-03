from carta import Carta,Tipo

carta01 = Carta("Pikachu",15,20,Tipo.ELECTRICO)
print(f"Mi carta tiene {carta01.defensa} ptos de vida")
carta01.quitarVida(5)

#print(f"Mi carta tiene {carta01.defensa} ptos de vida")
carta01.printCarta()

carta02 = Carta("Charizard",20,10)
carta02.printCarta()