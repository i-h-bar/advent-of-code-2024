
def is_safe(report: list[int]):
    ascending = report[0] < report[1]
    if not (0 < abs(report[0] - report[1]) < 4):
        return False

    for a, b in zip(report[1:-1], report[2:]):
        if (a < b) is not ascending or not (0 < abs(a - b) < 4):
            return False

    return True


def main():
    report_1 = [7, 6, 4, 2, 1]
    report_2 = [1, 2, 7, 8, 9]
    report_3 = [9, 7, 6, 2, 1]
    report_4 = [1, 3, 2, 4, 5]
    report_5 = [8, 6, 4, 4, 1]
    report_6 = [1, 3, 6, 7, 9]
    reports = [report_1, report_2, report_3, report_4, report_5, report_6]

    for i, report in enumerate(reports):
        print(f"{i} - {"Safe" if is_safe(report) else "Unsafe"}")


if __name__ == "__main__":
    main()