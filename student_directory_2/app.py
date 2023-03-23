from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.cohort_repository import CohortRepository
from lib.student import Student

# Connect to the database
connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/student_directory.sql")

cohorts_repository = CohortRepository(connection)

cohorts = cohorts_repository.find_with_students(2)

print(cohorts)
# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)
