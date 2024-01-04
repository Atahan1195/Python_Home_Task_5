import logging
from students_limit_error import StudentsLimitError
from student import Student

logging.basicConfig(filename='group.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Group:

    def __init__(self, title, max_students=10):
        self.title = title
        self.max_students = max_students
        self.__students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            logging.error(f'Error adding student to group')
            raise TypeError('Not a Student')
        if student in self.__students:
            logging.error(f'Error adding student to group')
            raise ValueError('Student already in group')
        if len(self.__students) == self.max_students:
            logging.error(f'Error adding student to group')
            raise StudentsLimitError(self.max_students)

        self.__students.append(student)
        logging.info(f'Student {student.name} added to group {self.title}')
