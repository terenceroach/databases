-- First, we must delete (drop) all our tables starting with students
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
-- Second, we must delete (drop) all our tables now from cohorts
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date text
);


CREATE SEQUENCE IF NOT EXISTS stidents_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);



-- Finally, we add any records that are needed for the tests to run
INSERT INTO cohorts (name, starting_date) VALUES ('March 2023', '10-Mar-2023');
INSERT INTO cohorts (name, starting_date) VALUES ('May 2023', '17-May-2023');
INSERT INTO cohorts (name, starting_date) VALUES ('August 2023', '03-Aug-2023');
INSERT INTO cohorts (name, starting_date) VALUES ('November 2023', '25-Nov-2023');





-- Finally, we add any records that are needed for the tests to run
INSERT INTO students (name, cohort_id) VALUES ('Student 1', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student 2', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student 3', 3);
INSERT INTO students (name, cohort_id) VALUES ('Student 4', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student 5', 2);
INSERT INTO students (name, cohort_id) VALUES ('Student 6', 2);
INSERT INTO students (name, cohort_id) VALUES ('Student 7', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student 8', 4);
INSERT INTO students (name, cohort_id) VALUES ('Student 9', 2);
INSERT INTO students (name, cohort_id) VALUES ('Student 10', 3);
INSERT INTO students (name, cohort_id) VALUES ('Student 11', 4);
INSERT INTO students (name, cohort_id) VALUES ('Student 12', 2);