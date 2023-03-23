from lib.student import Student
"""
When a student is created
It has id, name and cohort_id properties
"""
def test_student_properties():
    student = Student(1, 'Student One', 1)
    assert student.id == 1
    assert student.name == "Student One"
    assert student.cohort_id == 1

"""
We can compare two identical students
And have them be equal
"""
def test_equality():
    student1 = Student(1, 'Student One', 1)
    student_2 = Student(1, 'Student One', 1)
    assert student1 == student_2

"""
students are formatted to string
"""
def test_formatting():
    student = Student(1, 'Student One', 1)
    assert str(student) == "Student(1, Student One, 1)"