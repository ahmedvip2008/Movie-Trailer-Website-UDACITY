import fresh_tomatoes
import media

# Define some movies as instances of the class Movie
ratatouille  = media.Movie("Ratatouille ",
                    "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=-tNqfcZKn6k")


The_Pursuit_of_Happyness  = media.Movie("The Pursuit of Happyness ",
                    "A struggling salesman takes custody of his son as he's poised to begin a life-changing professional endeavor.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

Like_Stars_on_Earth  = media.Movie("Like Stars on Earth ",
                    "An eight-year-old boy is thought to be a lazy trouble-maker, until the new art teacher has the patience and compassion to discover the real problem behind his struggles in school.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTVmYTk2NjAtYzY3MS00YjFjLTlkYzktYzg3YzMyZDQyOWRiXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_SY1000_CR0,0,692,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=DBg6HSMF9X8")

# Create a list of a movies objects
movies = [ ratatouille , The_Pursuit_of_Happyness , Like_Stars_on_Earth]

# Create and open an html file to display a web page of the movies
fresh_tomatoes.open_movies_page(movies)
