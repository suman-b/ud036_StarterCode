import media
import fresh_tomatoes

shawshank_redemption = media.Movie ('The Shawshank Redemption','https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg','https://www.youtube.com/watch?v=6hB3S9bIaco')

godfather = media.Movie('The Godfather','https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg','https://www.youtube.com/watch?v=sY1S34973zA')

dark_knight = media.Movie('The Dark Knight','https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg','https://www.youtube.com/watch?v=EXeTwQWrcwY')

sholay = media.Movie('Sholay','https://upload.wikimedia.org/wikipedia/en/5/52/Sholay-poster.jpg','https://www.youtube.com/watch?v=6uqcput3XEI')

pulp_fiction = media.Movie('Pulp Fiction','https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg','https://www.youtube.com/watch?v=s7EdQ4FqbhY')

departed = media.Movie('The Departed','https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg','https://www.youtube.com/watch?v=iojhqm0JTW4')

movies = [shawshank_redemption,godfather,dark_knight,sholay,pulp_fiction,departed]

fresh_tomatoes.open_movies_page(movies)