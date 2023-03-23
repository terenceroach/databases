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