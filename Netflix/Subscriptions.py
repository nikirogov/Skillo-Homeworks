class Movies:
    all_movies = []

    def __init__(self, movie_name, movie_id, genre):
        self.movie_name = movie_name
        self.genre = genre
        self.movie_id = movie_id
        self.all_movies.append(self)

class Users:
    def __init__(self, name, id, subscription):
        self.name = name
        self.id = id
        self.watched = []  # Store watched movies as a list
        self.favorite_genre = None
        self.recommended_movies = []

    def add_to_watched(self, movie, rating):
        # Add the movie to the watched list
        self.watched.append((movie, rating))

    def create_favorite_genre(self):
        genre_counts = {'drama': 0, 'action': 0, 'documantary': 0}

        for movie, _ in self.watched:
            genre = movie.genre
            genre_counts[genre] += 1

        self.favorite_genre = max(genre_counts, key=genre_counts.get)

    def recommend_movies(self, movies):
        for movie in movies:
            if movie.genre == self.favorite_genre:
                self.recommended_movies.append(movie)

# Creating movie instances
movie1 = Movies("Stranger things", '321', 'drama')
movie2 = Movies("Cristiano Ronaldo", '4321', 'documantary')
movie3 = Movies("Star Wars", '54321', 'action')
movie4 = Movies("Dir hard 3", '654321', 'documantary')

# Creating user instances
user1 = Users("Alice", '123', '31/12/2023')
user2 = Users("Bob", '1234', '31/12/2023')

# Adding watched movies and ratings
user1.add_to_watched(movie4, 4)
user1.add_to_watched(movie3, 3)
user1.add_to_watched(movie2, 2)
user2.add_to_watched(movie3, 1)
user2.add_to_watched(movie4, 5)

# Calculate favorite genre
user1.create_favorite_genre()
user2.create_favorite_genre()

# Recommend movies
user1.recommend_movies(Movies.all_movies)
user2.recommend_movies(Movies.all_movies)

print("User 1's favorite genre:", user1.favorite_genre)
print("User 1's recommended movies:", [movie.movie_name for movie in user1.recommended_movies])
print("User 2's favorite genre:", user2.favorite_genre)
print("User 2's recommended movies:", [movie.movie_name for movie in user2.recommended_movies])
