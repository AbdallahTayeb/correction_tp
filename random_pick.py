from math import comb

def proba_k(n_rouges, n_blanches, n_bleues, k):
    nombre_de_tirages_possibles = comb(n_rouges + n_blanches + n_bleues, k)
    nombre_de_tirages_corrects = comb(n_rouges,1)*comb(n_blanches,1)*comb(n_bleues,1)
    proba = nombre_de_tirages_corrects/nombre_de_tirages_possibles

    return proba

def main():
    n_rouges = 100
    n_blanches = 100
    n_bleues = 100
    k = 3

    proba = proba_k(n_rouges, n_blanches, n_bleues, k)

    print(f"La probabilité d'avoir exactement une boule de chaque couleur parmi {k} boules tirées est de {proba:.2f}.")

    if __name__ == '__main__':
        main()