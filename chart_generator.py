import matplotlib.pyplot as plt

from randu_generator import generate_values_from_randu_generator


def generate_chart(values: list, title: str) -> None:
    plt.plot(values, "ob")
    plt.title(title)
    plt.ylabel('Valeur')
    plt.xlabel('Itération')
    plt.show()

def generate_square_with_randu_generator(x0: int, nb_iterations: int) -> None:
    x = []
    y = []
    values = generate_values_from_randu_generator(x0, nb_iterations)

    for i in range(0, nb_iterations):
        if i % 2 == 0:
            x.append(values[i] / (2 ** 31))
        else:
            y.append(values[i] / (2 ** 31))

    plt.plot(x, y, ",b")
    plt.gca().set_aspect("equal")
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    plt.title("Échantillonnage d'un carré unité avec le générateur \"RANDU\"")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()