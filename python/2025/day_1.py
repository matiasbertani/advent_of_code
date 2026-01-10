
from pathlib import Path


sample_input = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

expected_result = 6


def test_challenge() -> None:
    result = find_password(sample_input)
    assert result == expected_result


def get_dial_instructions() -> list[str]:
    return [instruction.strip() for instruction in get_day_input()]


def get_day_input() -> list[str]:
    current_dir = Path(__file__).parent
    input_filepath = current_dir / '../../inputs/2025/day_1.txt'
    with open(input_filepath) as f:
        data = f.readlines()
    return data


def find_password(instruccions: list[str]) -> int:

    password = int()
    current = 50

    for instruction in instruccions:

        count = how_many_times_will_pass_thorugh_zero(current, instruction)
        current = move_dial(current, instruction)
        if current == 0:
            password += 1
        password += count

    return password


def move_dial(current: int, instruction: str) -> int:

    direction = instruction[0]
    shift, _ = normalize_shift(int(instruction[1:]))
    shift = int(instruction[1:]) % 100

    current += (100 - shift) if direction == "L" else shift

    return (current - 100) if current > 99 else current


def normalize_shift(shift: int) -> int:
    count = 0
    while shift > 99:
        count += 1
        shift -= 100
    return shift, count


def how_many_times_will_pass_thorugh_zero(current, instruction):

    direction = instruction[0]
    shift, count = normalize_shift(int(instruction[1:]))

    if (
        direction == "L" and shift > current and current != 0
        or direction == "R" and shift > (100 - current)
    ):
        count += 1

    return count


if __name__ == "__main__":

    test_challenge()

    instruccions = get_dial_instructions()
    password = find_password(instruccions)
    print(f"The password is: {password}")
