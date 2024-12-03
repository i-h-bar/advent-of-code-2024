

def main():
    """Purposefully done without regex"""

    corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    valid_muls = []

    for i in range(len(corrupted_memory)):
        if corrupted_memory[i: i+4] != "mul(":
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

    print(sum(x * y for x, y in valid_muls))




if __name__ == "__main__":
    main()
