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

    # Assures that the 'students' list is always sorted
    @students.setter
    def students(self, students):
        self._students = sorted(students)

    def plants(self, student):
        """
        Return a list of plants names for an student
        """
        student_index = self.students.index(student)

        # Get all respective letters for plants from the student
        student_plants = []
        for row in self.diagram.split('\n'):
            student_plants.extend(row[student_index*2:student_index*2+2])

        # Convert each letter to the plant name
        return [self.plants_names[char] for char in student_plants]
