from collections import OrderedDict


class School(object):
    def __init__(self, name):
        self.name = name
        self.rooster = OrderedDict()

    def add(self, name, grade):
        self.rooster[name] = grade

    def grade(self, grade_number):
        return [student for student in self.rooster if self.rooster[student] == grade_number]

    def sort(self):
        self.rooster = OrderedDict(sorted(self.rooster.items()))
        grades = set(self.rooster.values())

        rooster_sorted = []
        for grade_ in grades:
            students_in_grade = []
            for student in self.rooster.items():
                if student[1] == grade_:
                    students_in_grade.append(student[0])
            rooster_sorted.append((grade_, tuple(students_in_grade),))
        return rooster_sorted
