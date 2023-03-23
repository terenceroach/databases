from lib.cohort import Cohort
"""
When a cohort is created
It has id, name and starting_date properties
"""
def test_cohort_properties():
    cohort = Cohort(1, 'March 2023', '13-Mar-2023')
    assert cohort.id == 1
    assert cohort.name == 'March 2023'
    assert cohort.starting_date == '13-Mar-2023'

"""
We can compare two identical cohorts
And have them be equal
"""
def test_equality():
    cohort_1 = Cohort(1, 'March 2023', '13-Mar-2023')
    cohort_2 = Cohort(1, 'March 2023', '13-Mar-2023')
    assert cohort_1 == cohort_2

"""
Cohorts are formatted to string
"""
def test_formatting():
    cohort = Cohort(1, 'March 2023', '13-Mar-2023')
    assert str(cohort) == "Cohort(1, March 2023, 13-Mar-2023)"