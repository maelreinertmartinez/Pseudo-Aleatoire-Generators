from random import randint

from chart_generator import generate_chart, generate_square_with_randu_generator
from displayer import display_randu_result, display_von_neumann_result
from randu_generator import generate_values_from_randu_generator, verify_equation
from von_neumann_generator import generate_values_from_von_neumann_generator


def generate_chart_and_display_values_from_randu_generator(x0: int, nb_iterations: int, title: str) -> None:
    values = generate_values_from_randu_generator(x0, nb_iterations)
    display_randu_result(title, x0, nb_iterations, values)
    generate_chart(values, f"{title} (RANDU, X0: {x0}, Itérations: {nb_iterations})")

def generate_chart_and_display_values_from_von_neumann_generator(seed: int, nb_iterations: int, title: str) -> None:
    values = generate_values_from_von_neumann_generator(seed, nb_iterations)
    display_von_neumann_result(title, seed, nb_iterations, values)
    generate_chart(values, str(f"{title} (Von Neumann, Seed: {seed}, Itérations: {nb_iterations})"))


if __name__ == '__main__':

    # Générateur de Von Neumann

    # Exemple de génération de nombres pseudo-aléatoires avec le générateur de Von Neumann
    generate_chart_and_display_values_from_von_neumann_generator(3546, 40, "Générateur de Von Neumann")

    # Utilisation de seed aléatoire pour trouver des défauts dans le générateur de Von Neumann
    # for i in range(100):
    #     seed = randint(1000, 1000000)
    #     generate_chart_and_display_values_from_von_neumann_generator(seed, 100, "")

    # Jeu de tests pour le générateur de nombres pseudo-aléatoires de Von Neumann
    generate_chart_and_display_values_from_von_neumann_generator(486128, 30, "Problème du zéro")
    generate_chart_and_display_values_from_von_neumann_generator(450953, 100, "Périodicité réduite de 4 pas")


    # Générateur "RANDU"

    # Exemple de génération de nombres pseudo-aléatoires avec le générateur "RANDU"
    generate_chart_and_display_values_from_randu_generator(3546, 40, "Générateur \"RANDU\"")

    # Vérification de l'équivalence de la relation X_{n+2} = 6 * X_{n+1} + 9 * X_n (mod 2^{31})
    # pour le générateur "RANDU"
    result = generate_values_from_randu_generator(3546, 100)
    display_randu_result("Vérification de l'équation X_{n+2}", 3546, 100, result)
    verify_equation(result)


    # Échantionnage d'un carré avec le générateur "RANDU"
    generate_square_with_randu_generator(1234, 100000)
    generate_square_with_randu_generator(1234, 10000)