from pathlib import Path

XMAS = "XMAS"
DIAGONAL_RIGHT = [(1, 1), (2, 2), (3, 3)]
DIAGONAL_LEFT = [(-1, 1), (-2, 2), (-3, 3)]
RIGHT = [(0, 1), (0, 2), (0, 3)]
DOWN = [(1, 0), (2, 0), (3, 0)]
CONVERTION = lambda x: (-1 * x[0], -1 * x[1])

DIRECTIONS = [
    DIAGONAL_RIGHT,
    DIAGONAL_LEFT,
    RIGHT,
    DOWN,
    list(map(CONVERTION, DIAGONAL_RIGHT)),
    list(map(CONVERTION, DIAGONAL_LEFT)),
    list(map(CONVERTION, RIGHT)),
    list(map(CONVERTION, DOWN))
]


def parse_file(path: str) -> list[list[str]]:
    path = Path(path)
    return [[char for char in list(line)] for line in path.read_text().split("\n")]


def xmas_count(puzzle: list[list[str]]) -> int:
    count = 0
    len_i = len(puzzle)
    for i in range(len_i):
        len_j = len(puzzle[i])
        for j in range(len_j):
            if puzzle[i][j] == "X":
                for direction in DIRECTIONS:
                    for z, (x, y) in enumerate(direction):
                        new_i = i + x
                        new_j = j + y
                        if (
                                (new_i < 0 or new_i > len_i - 1) or (new_j < 0 or new_j > len_j - 1)
                        ) or XMAS[z + 1] != puzzle[new_i][new_j]:
                            break

                    else:
                        count += 1

    return count


def shape_xmas(puzzle: list[list[str]]) -> int:
    count = 0
    MS_MAP = {"M": "S", "S": "M"}

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if i == 0 or i == len(puzzle) - 1 or j == 0 or j == len(puzzle[i]) - 1:
                continue

            if puzzle[i][j] == "A":
                if (letter := puzzle[i + 1][j + 1]) in MS_MAP:
                    other_letter = MS_MAP[letter]
                    if puzzle[i - 1][j - 1] == other_letter:
                        if (letter := puzzle[i - 1][j + 1]) in MS_MAP:
                            other_letter = MS_MAP[letter]
                            if puzzle[i + 1][j - 1] == other_letter:
                                count += 1

    return count


def main():
    puzzle = parse_file("input.txt")
    count = shape_xmas(puzzle)
    print(count)


if __name__ == "__main__":
    main()
