class Movies:
    all_movies = []
    def __init__(self, movie_name, movie_id, genre):
        self.movie_name = movie_name
        self.genre = genre

        self.drama = []
        self.action = []
        self.documantary = []
        self.movie_id = movie_id


    def genre_split(self, genre):
        if self.genre == 'drama':
            self.drama.append(self.movie_name)
        if self.genre == 'action':
            self.action.append(self.movie_name)
        if self.genre == 'documantary':
            self.documantary.append(self.movie_name)

    def adding_all_movies(self):

        self.all_movies.append(self.movie_name)
        # new_movie_id = len(self.all_movies) + 1
        self.genre_split(self.genre)