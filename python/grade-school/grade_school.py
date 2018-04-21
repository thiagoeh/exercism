from collections import OrderedDict


class School(object):
    def __init__(self, name):
        self.name = name
        self.roster = OrderedDict()

    def add(self, name, grade):
        self.roster[name] = grade

    def grade(self, grade_number):
        return [student for student in self.roster if self.roster[student] == grade_number]

    def sort(self):
        # sort the roster by student name
        self.roster = OrderedDict(sorted(self.roster.items()))
        # A set containing grades from current students
        grades = set(self.roster.values())

        roster_sorted = []
        # Add to roster_sorted a tuple for each grade, containing another tuple with students names as the second item in the parent tuple
        for grade_ in grades:
            students = [student[0]
                        for student in self.roster.items() if student[1] == grade_]
            roster_sorted.append((grade_, tuple(students),))
        return roster_sorted
