from student import Student
from teacher import Teacher
from library import Library


student_1 = Student('Alexander Schiller', 0)
student_1.print_info()


teacher1 = Teacher('Nick', 0)
teacher1.print_info()

library = Library()
library.__dict__ = {'Chuk Palahniuk': 'Fight club'}
library.print_info()