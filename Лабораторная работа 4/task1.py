# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    total = []
    with open(INPUT_FILENAME, 'r') as f:
        dict_reader = csv.DictReader(f)
        for i in dict_reader:
            total.append(i)
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(total, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
