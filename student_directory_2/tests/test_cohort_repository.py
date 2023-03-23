from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student
"""
When calling #all on CohortRepository
A list of all cohorts is returned
"""
def test_list_all_cohorts(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    repository = CohortRepository(db_connection)
    result = repository.all()
    assert result == [
        Cohort(1,'March 2023', '10-Mar-2023'),
        Cohort(2,'May 2023', '17-May-2023'),
        Cohort(3,'August 2023', '03-Aug-2023'),
        Cohort(4,'November 2023', '25-Nov-2023')
    ]

"""
When calling #find on CohortRepository with an id
The cohort corresponding to that id is returned
"""
def test_find(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    repository = CohortRepository(db_connection)
    result = repository.find(2)
    assert result == Cohort(2,'May 2023', '17-May-2023')

"""
When calling #create on CohortRepository with some fields
And then list out all the records
The new cohort is in the list
"""
def test_create(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    repository = CohortRepository(db_connection)
    cohort = Cohort(None, 'December 2023', '01-Dec-2023')
    repository.create(cohort)
    result = repository.all()
    assert result == [
        Cohort(1,'March 2023', '10-Mar-2023'),
        Cohort(2,'May 2023', '17-May-2023'),
        Cohort(3,'August 2023', '03-Aug-2023'),
        Cohort(4,'November 2023', '25-Nov-2023'),
        Cohort(5, 'December 2023', '01-Dec-2023')
    ]

"""
When calling #delete on CohortRepository with an id
And then list out all the records
The deleted record does not show up
"""
def test_delete(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    repository = CohortRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        Cohort(1,'March 2023', '10-Mar-2023'),
        Cohort(2,'May 2023', '17-May-2023'),
        Cohort(4,'November 2023', '25-Nov-2023')
    ]

"""
When calling #find_with_students with a cohort id
Can get the Cohort with a list of the student prepopulated
"""
def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    repository = CohortRepository(db_connection)
    result = repository.find_with_students(1)
    assert result == "Cohort - id: 1, Name: March 2023, Start Date: 10-Mar-2023\nStudent - id: 1, Name: Student 1, Cohort_id: 1\nStudent - id: 2, Name: Student 2, Cohort_id: 1\nStudent - id: 4, Name: Student 4, Cohort_id: 1\nStudent - id: 7, Name: Student 7, Cohort_id: 1\n"
    