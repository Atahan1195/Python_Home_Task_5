class StudentsLimitError(Exception):
    def __init__(self, max_students, message='Too many students'):
        self.max_students = max_students
        self.message = message
        super().__init__()

    def __str__(self):
        return f'Limit of students is {self.max_students}\n. {self.message}'
