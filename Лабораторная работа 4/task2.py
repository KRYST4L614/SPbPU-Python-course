import json


def task() -> float:
    sum = 0
    with open('input.json', 'r') as f:
        data = json.load(f)
        for i in data:
            sum += i['score'] * i['weight']
    return round(sum, 3)


print(task())
