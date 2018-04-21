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
        # sort the rooster by student name
        self.rooster = OrderedDict(sorted(self.rooster.items()))
        # A set containing grades from current students
        grades = set(self.rooster.values())

        rooster_sorted = []
        # Add to rooster_sorted a tuple for each grade, containing another tuple with students names as the second item in the parent tuple
        for grade_ in grades:
            students = [student[0]
                        for student in self.rooster.items() if student[1] == grade_]
            rooster_sorted.append((grade_, tuple(students),))
        return rooster_sorted
