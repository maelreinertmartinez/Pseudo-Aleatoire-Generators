def display_result(title: str, header: dict, result: list) -> None:
    min_width = 50
    max_key_width = max(len(str(key)) for key in header.keys())
    max_value_width = max(len(str(value)) for value in header.values())
    total_width = max_key_width + max_value_width + 7 if max_key_width + max_value_width > min_width else min_width
    max_value_width = total_width - max_key_width - 7

    t_title = f"[{title}]"
    print(f"{t_title:=^{total_width}}")

    for key, value in header.items():
        print(f"| {key:<{max_key_width}} | {value:<{max_value_width}} |")

    print("=" * total_width)

    for i in range(len(result)):
        print(f"| {i:<{max_key_width}} | {result[i]:<{max_value_width}} |")

    print("=" * total_width)

def display_von_neumann_result(title: str, seed: int, nb_iterations: int, values: list[int]) -> None:
    display_result(f"{title} (Von Neumann)", {
        "Graine": seed,
        "Nombre d'itérations": nb_iterations
    }, values)

def display_randu_result(title: str, x0: int, nb_iterations: int, values: list[int]) -> None:
    display_result(f"{title} (RANDU)", {
        "X0": x0,
        "Nombre d'itérations": nb_iterations
    }, values)