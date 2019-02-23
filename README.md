# ud036_StarterCode
Source code for a Movie Trailer website.
Movie Trailer Website contains 3 interrelated files
Media.Py defines the main Class file 
it has variables for initializing movie name, its poster image and you tube url


fresh_tomatoes.py contains the styles and scripting page for the movies website.
it is used to show the The main page layout and title bar
the file contains functions for
create_movie_tiles_content : creates the HTML movies content based on the movie objects passed as input
open_movies_page : opens movies page after creating the contents as described above


entertainment_center.py is the main file where the object instances of the movies are created
it contains a list of movie objects 
the values of all instance variables are setup by calling the constructer method.
after all the intances are initialized the open_movies_page of fresh_tomatoes is called 
It displays the webpage with contents of the movie list on the browser. 