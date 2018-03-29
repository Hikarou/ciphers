from vigenere import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Programme de chiffrement et déchiffrement\nContient Vigenère et César")
    parser.add_argument('method', metavar='method', type=int,
                        help='L\'algorithme choisi\n0 : Vignere\n 1 : Ceasar')
    parser.add_argument('key', metavar='key', type=int,
                        help='La clé qui sera utilisée pour de (dé)chiffrement')
    parser.add_argument('message', metavar='str', type=str,
                        help='Le message à (dé)chiffrer')

    args = parser.parse_args()

    clair = args.message

    if args.method == 0:
        algo = vigenere.Vigenere(args.key)
    else:
        print("Algorithme choisi ({}) n'existe pas".format(args.method))
        exit(1)

    chiff = algo.cipher_string(clair)

    reclair = algo.decipher_string(chiff)

    print("Le message en clair est :\n{}\nLe message chiffré est :\n{}\nPuis déchiffré :\n{}".format(clair, chiff,
                                                                                                     reclair))
