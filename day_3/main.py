from pathlib import Path


def mul_no_conditionals(corrupted_memory) -> int:
    """Purposefully done without regex"""

    valid_muls = []
    for i in range(len(corrupted_memory)):
        if corrupted_memory[i: i + 4] != "mul(":
            continue
        else:
            first = ""
            second = ""
            constructing_first = True
            valid = False
            for x in range(i + 4, i + 13):
                char = corrupted_memory[x]
                if char.isnumeric():
                    if constructing_first:
                        first += char
                    else:
                        second += char
                elif char == "," and constructing_first:
                    constructing_first = False
                elif char == ")" and not constructing_first:
                    if first and second:
                        valid = True

                    break
                else:
                    break

            if valid:
                valid_muls.append((int(first), int(second)))

    return sum(x * y for x, y in valid_muls)


def mul(corrupted_memory: str) -> int:
    """Purposefully done without regex"""
    mul_enabled = True
    valid_muls = []
    for i in range(len(corrupted_memory)):
        if corrupted_memory[i: i + 4] == "do()":
            mul_enabled = True
        elif corrupted_memory[i: i + 7] == "don't()":
            mul_enabled = False

        if corrupted_memory[i: i + 4] == "mul(" and mul_enabled:
            first = ""
            second = ""
            constructing_first = True
            valid = False
            for x in range(i + 4, i + 13):
                char = corrupted_memory[x]
                if char.isnumeric():
                    if constructing_first:
                        first += char
                    else:
                        second += char
                elif char == "," and constructing_first:
                    constructing_first = False
                elif char == ")" and not constructing_first:
                    if first and second:
                        valid = True

                    break
                else:
                    break

            if valid:
                valid_muls.append((int(first), int(second)))

    return sum(x * y for x, y in valid_muls)


def main():
    corrupted_memory = Path("input.txt").read_text()
    answer = mul(corrupted_memory)
    print(answer)


if __name__ == "__main__":
    main()
