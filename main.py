from caesar.caesar import Caesar
from vigenere.vigenere import Vigenere

if __name__ == "__main__":

    while True:
        # Traitement du choix de l'algorithme
        out = -1
        alg = 0
        while alg == 0:
            print("Quel algorithme sera utilisé ? (Q : pour quitter)\n\t1 - César\n\t2 - Vigenère")
            alg = input()
            if alg.lower() == "q":
                out = 0
                break

            try:
                alg = int(alg)
                if alg > 2 or alg < 1:
                    raise ValueError()
            except ValueError:
                print(
                    "La valeur donnée n'est pas un algorithme possible!\n"
                    "\t1 - César\n\t2 - Vigenère"
                )
                alg = 0

        if out == 0:
            break

        # Traitement du choix de la clé
        cle = -1
        while True:
            print("Quelle sera la clé de l'algorithme choisi ? (Q : pour quitter)")
            if alg == 1:
                print("\t[0;26]")
            else:
                print("\t[a-zA-Z]+")
            cle = input()

            if cle.lower() == "q":
                out = 0
                break

            # Si c'est l'algorithme de César, il faut que ce soit un chiffre.
            if alg == 1:
                try:
                    cle = int(cle)
                    break
                except ValueError:
                    print(
                        "La clé donnée n'est pas un entier!\n"
                        "Merci de donner une valeur correcte!\n"
                    )
                    cle = -1
            elif alg == 2:
                break

        if out == 0:
            break

        chiffr = -1
        while chiffr == -1:
            print("Il faut chiffrer le message ou le déchiffrer ? (Q : pour quitter)\n\t1 - Chiffrer\n\t2 - Déchiffrer")
            chiffr = input()
            if chiffr.lower() == "q":
                out = 0
                break

            try:
                chiffr = int(chiffr)
                if chiffr > 2 or chiffr < 1:
                    raise ValueError()
            except ValueError:
                print(
                    "La valeur donnée n'est pas un choix possible!\n"
                    "\t1 - Chiffrer\n\t2 - Déchiffrer"
                )
                chiffr = -1

        if out == 0:
            break

        print("Quel message faudra-t'il ", end="")
        if chiffr == 2:
            print("dé", end="")
        print("chiffrer ?")
        mess = input()

        if alg == 1:  # César
            alg = Caesar(cle)
        elif alg == 2:  # Vigenere
            alg = Vigenere(cle)
        else:
            print("L'aglorithme n'est pas le bon... ceci ne devrait jamais arriver")
            quit(-1)

        outMess = ""
        if chiffr == 1:
            outMess = alg.cipher_string(mess)
        elif chiffr == 2:
            outMess = alg.decipher_string(mess)
        else:
            print("Le choix de (dé)chiffrement n'est pas le bon... ceci ne devrait jamais arriver")
            quit(-1)

        print("Le message initial était :\n{}\nAprès ".format(mess), end="")
        if chiffr == 2:
            print("dé", end="")
        print("chiffrement, le message est :\n{}".format(outMess))
    print("Bye!")
