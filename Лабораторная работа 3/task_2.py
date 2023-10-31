def find_common_participants(first, second, separator = ','):
    res = set(first.split(separator))
    res = list(res.intersection(second.split(separator)))
    res.sort()
    return res


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
