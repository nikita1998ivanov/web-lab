groupmates = [
    {
        "name": u"Кирилл",
        "group": u"убап-1702",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Илья",
        "group": u"убап-1701",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Даня",
        "group": u"убап-1702",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Женя",
        "group": u"убап-1701",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]
def print_students(students):
    print u"Имя студента".ljust(15), \
        u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20)
    for student in students:
        print \
            student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20)
    print "\n"
def filter_students(students, min_middle):
    result = []
    for student in students:
        middle = 0
        for value in student["marks"]:
            middle += value
        middle /= len(student["marks"])
        if middle >= min_middle:
            result.append(student)
    return result
print_students(groupmates)
print_students(filter_students(groupmates, 4))
