from pathlib import Path


def parse_file(path: str) -> list[list[int]]:
    path = Path(path)
    return [[int(num) for num in report.split()] for report in path.read_text().split("\n")]


def is_safe(report: list[int]):
    if not report:
        return False

    ascending = report[0] < report[1]
    if not (0 < abs(report[0] - report[1]) < 4):
        return False

    for a, b in zip(report[1:-1], report[2:]):
        if (a < b) is not ascending or not (0 < abs(a - b) < 4):
            return False

    return True

def is_safe_with_damper(report: list[int]):
    if not report:
        return False

    ascending = report[0] < report[1]
    if not (0 < abs(report[0] - report[1]) < 4):
        reports = [[num for i, num in enumerate(report) if i != x] for x in range(len(report))]
        return any(is_safe(r) for r in reports)

    for i, (a, b) in enumerate(zip(report[1:-1], report[2:])):
        if (a < b) is not ascending or not (0 < abs(a - b) < 4):
            reports = [[num for i, num in enumerate(report) if i != x] for x in range(len(report))]
            return any(is_safe(r) for r in reports)

    return True

def count_safe_reports(reports: list[list[int]], with_damper: bool = False) -> int:
    safety_check = is_safe
    if with_damper:
        safety_check = is_safe_with_damper

    safe = 0
    for report in reports:
        if safety_check(report):
            safe += 1

    return safe


def main():
    reports = parse_file("input.txt")
    safe = count_safe_reports(reports, with_damper=True)
    print(safe)


if __name__ == "__main__":
    main()