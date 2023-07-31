from pathlib import Path


def get_calories_from_elf_with_most_calories(input_filepath: Path) -> int:
    all_calories = get_all_calories_from_file(input_filepath)
    amount_of_calories_per_elf = [
        sum(elf_calories)
        for elf_calories in group_calories_by_elf(all_calories)
    ]
    amount_of_calories_per_elf.sort()
    return amount_of_calories_per_elf[-1], sum(amount_of_calories_per_elf[-3:])


def get_all_calories_from_file(filepath: Path) -> list[str]:
    with open(filepath) as f:
        data = f.readlines()
    return data


def group_calories_by_elf(all_elf_colories: list) -> list[int]:
    one_elf_calories = []
    for element in all_elf_colories:
        element = element.strip()
        if not element:
            yield one_elf_calories
            one_elf_calories = []
            continue
        one_elf_calories.append(int(element))
    yield one_elf_calories


if __name__ == "__main__":

    current_dir = Path(__file__).parent
    input_filepath = current_dir / '../../inputs/2022/day_1.txt'
    max_calories, sum_of_top_thre_calories = get_calories_from_elf_with_most_calories(input_filepath)
    print(max_calories, sum_of_top_thre_calories)
