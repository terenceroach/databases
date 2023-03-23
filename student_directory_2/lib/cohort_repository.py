from lib.cohort import Cohort
from lib.student import Student
class CohortRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM cohorts")
        cohorts = []
        for row in rows:
            cohort = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(cohort)
        return cohorts
    
    def find(self, cohort_id):
        rows = self._connection.execute("SELECT * FROM cohorts WHERE id = %s", [cohort_id])
        row = rows[0]
        return Cohort(row["id"], row["name"], row["starting_date"])
    
    def find_with_students(self, cohort_id):
        rows = self._connection.execute("SELECT cohorts.id AS c_id, cohorts.name AS c_name, cohorts.starting_date, students.id AS s_id, students.name AS s_name, students.cohort_id FROM cohorts JOIN students ON cohorts.id = students.cohort_id WHERE cohorts.id = %s", [cohort_id])
        students_string = ""
        for row in rows:
            students_string += f"Student - id: {row['s_id']}, Name: {row['s_name']}, Cohort_id: {row['cohort_id']}\n"
        cohort_string = f"Cohort - id: {rows[0]['c_id']}, Name: {rows[0]['c_name']}, Start Date: {rows[0]['starting_date']}\n"
        full_string = cohort_string + students_string
        return full_string
    
    def create(self, cohort):
        self._connection.execute("INSERT INTO cohorts (name, starting_date) VALUES (%s, %s)", [cohort.name, cohort.starting_date])

    def delete(self, cohort_id):
        self._connection.execute("DELETE FROM cohorts WHERE id = %s", [cohort_id])
