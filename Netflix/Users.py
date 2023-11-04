from Movies import Movies
class Users(Movies):
    def __init__(self, name, id, fav_genre, subscription):
        self.name = name
        self.id = id
        self.fav = []
        self.fav_genre = fav_genre
        self.recommended_and_genre = {}
        self.watched = {}
        self.subscription = subscription
        self.new_reccomended = None

    def add_to_watched(self, new_movie,rating):

        if new_movie in Movies.all_movies:
            self.watched[new_movie] = rating


    def add_to_fav(self, new_fav):

        if new_fav in Movies.all_movies:
            self.fav.append(new_fav)
            return f"{new_fav} is added to your list of favourite movies"

    def creating_fav_genre(self):
        genre_count = {
            'drama' : 0,
            'action' : 0,
            'documantary': 0
        }
        for movie in self.watched:
            genre = self.genre
            genre_count[genre] +=1
        self.favorite_genre = max(genre_counts, key=genre_counts.get)

    def reccommended_movies(self):
        if self.new_reccomended is not None:
            if new_reccomended in Movies.all_movies and self.fav_genre == self.recommended_and_genre[new_reccomended]:
                self.recommended_and_genre[new_reccomended] = Movies.genre_split(self.recommended_and_genre[new_reccomended])

    def ask_for_reccomendations(self):
        key_list = list(self.recommended_and_genre.keys())
        return f'Your reccomendations: {key_list}'
    def ask_for_watched_movies(self):
        key_list = list(self.watched.keys())
        return f'Your watched movies: {key_list}'