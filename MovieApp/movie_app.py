from MovieApp.movie_specification.movie import Movie
from MovieApp.user import User


class MovieApp:

    def __init__(self):

        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):

        user = self.__find_user_by_username(username)
        if user:
            raise Exception("User already exist!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):

        user = self.__find_user_by_username(username)
        if user is None:
            raise Exception("This user is does not exist!")
        if user != movie.owner:
            raise Exception(f"(username) is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            return "Movie already added to the collection!"
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):
        user = self.__find_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie: Movie):
        user = self.__find_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):

        user = self.__find_user_by_username(username)
        if movie in user.movies_owned:
            raise Exception(f"{username} is is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):

        user = self.__find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} nas not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):

        result = []
        if self.movies_collection:

            for movie in sorted(self.movies_collection, key=lambda m: (-m.year, m.title)):
                result.append(movie.details())
            return '\n'.join(result)
        return "No movies found."

    def __str__(self):

        result = []
        if self.users_collection:
            result.append(f"All users: {', '.join(x.username for x in self.users_collection)}")
        else:
            result.append('All users: No users.')

        if self.movies_collection:
            result.append(f"All movies: {', '.join(x.title for x in self.movies_collection)}")
        else:
            result.append('All movies: No movies.')

        return '\n'.join(result)

    def __find_user_by_username(self, name):

        for username in self.users_collection:
            if username.username == name:
                return username
        return None
