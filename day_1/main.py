from pathlib import Path
from collections import defaultdict


def main():
    list_1, list_2 = parse_file("input.txt")
    calculate_similarity_addition(list_1, list_2)
    calculate_score_multiply(list_1, list_2)



def parse_file(path: str) -> tuple[list[int], list[int]]:
    path = Path(path)
    list_1 = []
    list_2 = []
    for line in path.read_text().split("\n"):
        num_1, num_2 = line.split("   ")
        list_1.append(int(num_1))
        list_2.append(int(num_2))

    return list_1, list_2


def calculate_similarity_addition(list_1: list[int], list_2: list[int]) -> None:
    total = sum((abs(a - b) for a, b in zip(sorted(list_1), sorted(list_2))))
    print(total)


def calculate_score_multiply(list_1: list[int], list_2: list[int]) -> None:
    counts = defaultdict(int)
    for num in list_2:
        counts[num] += 1

    similarity = sum(num * counts[num] for num in list_1)
    print(similarity)


if __name__ == "__main__":
    main()