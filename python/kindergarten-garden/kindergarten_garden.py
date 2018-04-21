class Garden(object):
    default_students = [
        'Alice',
        'Bob',
        'Charlie',
        'David',
        'Eve',
        'Fred',
        'Ginny',
        'Harriet',
        'Ileana',
        'Joseph',
        'Kincaid',
        'Larry',
    ]

    def __init__(self, diagram, students=default_students):
        self.diagram = diagram
        self.students = students

        self.plants_names = {
            'C': 'Clover',
            'G': 'Grass',
            'R': 'Radishes',
            'V': 'Violets',
        }

    @property
    def students(self):
        return self._students

    # The setter assures that the 'students' list is always sorted
    @students.setter
    def students(self, students):
        self._students = sorted(students)

    def plants(self, student):
        student_index = self.students.index(student)
        rows = self.diagram.split()
        student_plants = []
        for row in rows:
            student_plants.extend(row[student_index*2:student_index*2+2])

        return [self.plants_names[char] for char in student_plants]
