from lib.database_connection import DatabaseConnection
"""
When calling #all on CohortRepository
A list of all cohorts is returned
"""
def test_list_all_cohorts(db_connection):
    db_connection.seed("seeds/student_directory.sql")