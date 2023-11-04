from Users import Users
from Admins import Admins
# from Subscriptions import Subscriptions
from Movies import Movies

person1 = Users(
    name = "Alice",
    id = '123',
    fav_genre = 'none',
    subscription = '31/12/2023'
)
person2 = Users(
    name = "Bob",
    id = '1234',
    fav_genre = 'none',
    subscription = '31/12/2023'
)
person3 = Users(
    name = "Kanye",
    id = '12345',
    fav_genre = 'none',
    subscription = '31/09/2023'
)
person4 = Users(
    name = "Dylan",
    id = '123456',
    fav_genre = 'none',
    subscription = '31/12/2023'
)

movie1 = Movies(
    movie_name = 'Stranger things',
    movie_id = '321',
    genre = 'drama',

)
movie2 = Movies(
    movie_name = 'Cristiano Ronaldo',
    movie_id = '4321',
    genre = 'documantary',

)
movie3 = Movies(
    movie_name = 'Star Wars',
    movie_id = '54321',
    genre = 'action',

)
movie4 = Movies(
    movie_name = 'Dir hard 3',
    movie_id = '654321',
    genre = 'documantary',

)
movie1.adding_all_movies()
movie2.adding_all_movies()
movie3.adding_all_movies()
movie4.adding_all_movies()

person1.add_to_watched(new_movie= movie4, rating='4')
person1.add_to_watched(new_movie= movie3, rating='3')
person1.add_to_watched(new_movie= movie2, rating='2')

person2.add_to_watched(new_movie= movie3, rating='1')
person2.add_to_watched(new_movie= movie4, rating='5')

person1.add_to_fav(person1.watched)


person1.creating_fav_genre()
person1.reccommended_movies()

person2.add_to_fav(movie3)
person2.creating_fav_genre()
person2.reccommended_movies()
print(person1.fav, person1.creating_fav_genre())
