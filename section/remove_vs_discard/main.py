marvel_movies = {
    'Avengers: Endgame',
    'Black Panther',
    'Iron Man',
    'The Dark Knight',
    'Spider-Man: No Way Home',
    'Guardians of the Galaxy',
    'Justice League'
}

movies_to_remove = ["The Dark Knight", "Justice League"]

for x in movies_to_remove:
    marvel_movies.discard(x)


# Testing
print("Updated set:", marvel_movies)