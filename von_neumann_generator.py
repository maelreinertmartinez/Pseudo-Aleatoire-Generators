def extract_digits_from_the_middle(value: int, length: int) -> int:
    value_str = str(value)
    middle_index = len(value_str) // 2
    diff = (length // 2)
    if length % 2 == 0:
        return int(value_str[middle_index - diff: middle_index + diff])
    return int(value_str[middle_index - diff: middle_index + diff + 1])

def generate_values_from_von_neumann_generator(seed: int, nb_iterations: int) -> list[int]:
    length = len(str(seed))
    value = seed ** 2
    values = [extract_digits_from_the_middle(value, length)]
    for i in range(nb_iterations - 1):
        value = values[i] ** 2
        values.append(extract_digits_from_the_middle(value, length))
    return values

