def generate_values_from_randu_generator(x0: int, nb_iterations: int) -> list[int]:
    values = [(65539 * x0) % (2 ** 31)]
    for i in range(nb_iterations - 1):
        values.append((65539 * values[i]) % (2 ** 31))
    return values

def verify_equation(values: list[int]) -> bool:
    for i in range(len(values) - 2):
        if values[i + 2] != (6*values[i + 1] - 9*values[i]) % (2 ** 31):
            print(f"Erreur à l'indice {i + 2}: {values[i]} != 6*{values[i - 1]} - 9*{values[i - 2]} = {6*values[i - 1] - 9*values[i - 2]}")
            return False
    print("Aucune erreur n'a été trouvée")
    return True
