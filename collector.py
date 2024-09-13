def collect_seed() -> int:
    seed = -1
    while seed / (10 ** 3) < 1:
        seed = int(input("Saisissez une graine (d'au moins 4 chiffres): "))
        if seed / (10 ** 3) < 1:
            print("La graine doit avoir au moins 4 chiffres")
    return seed

def collect_number_of_iteration() -> int:
    nb_iterations = -1
    while nb_iterations <= 0:
        n = int(input("Saisissez le nombre d'itérations à faire: "))
        if nb_iterations <= 0:
            print("Le nombre d'itérations doit être supérieur à 0")
    return nb_iterations
