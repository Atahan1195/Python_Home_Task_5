#                                     HomeWork 5

# Домашнее задание (RU)
# Task 1
# Реализовать логирование событий в классах, которые использовали при решении предыдущих задач (про заказы, про меню).
# Убедитесь в работоспособности проекта.


# Task 2
# Разнесите классы, которые использовали при решении предыдущих задач (про заказы, про меню).
# Убедитесь в работоспособности проекта.

from group import Group
from student import Student

group = Group("Math", max_students=2)

student1 = Student("Alice", "2000-01-01", "Female")
student2 = Student("Bob", "2001-02-02", "Male")
student3 = Student("Charlie", "1999-03-03", "Male")

group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
