class Movie:
    def __init__(self, title, date, quality):
        self.title = title
        self.date = date
        self.quality = quality
        self.actors = []


class Actor:
    def __init__(self, name):
        self.name = name


class MovieManager:
    def __init__(self):
        self.movies = []
        self.actors = []
        self.movie_id = 0

    def add_movie(self, title, date, quality):

        if len(title) > 20:
            print("Invalid title")
            return
        if not (1888 <= int(date) <= 2024):
            print("Invalid date")
            return
        if quality not in ['720p', '1080p', '4K']:
            print("Invalid quality")
            return

        movie = Movie(title, date, quality)
        self.movies.append(movie)
        movie_id = self.movie_id
        self.movie_id += 1

        print(f"Added successfully {movie_id}")

    def rem_movie(self, movie_id):
        for movie in self.movies:
            if movie_id == movie:
                self.movies.remove(movie)
                print(f"Removed successfully {movie_id}")
                return

        print("Invalid movie id")

    def add_cast(self, name):
        if len(name) > 20 or not name.isalpha():
            print("Invalid name")
            return

        cast = Actor(name)
        cast_id = len(self.actors)
        self.actors.append(cast)

        print(f"Added successfully {cast_id}")

    def rem_cast(self, cast_id):
        if cast_id >= len(self.actors):
            print("Invalid cast id")
            return

        self.actors.pop(cast_id)
        print(f"Removed successfully {cast_id}")

    def show_movie(self, movie_id):
        if movie_id >= len(self.movies):
            print("Invalid movie id")
            return

        movie = self.movies[movie_id]
        print(movie)

    def show_cast(self, cast_id):
        if cast_id >= len(self.actors):
            print("Invalid cast id")
            return

        actor = self.actors[cast_id]
        print(actor)

    def link_cast_to_movie(self, cast_id, movie_id):
        if cast_id >= len(self.actors):
            print("Invalid cast id")
            return

        if movie_id >= len(self.movies):
            print("Invalid movie id")
            return

        movie = self.movies[movie_id]
        movie.actors.append(cast_id)
        print(f"Successfully linked {cast_id} to {movie_id}")

    def filter_movies_by_title(self, pattern):
        filtered_movies = [str(i) for i, movie in enumerate(self.movies) if movie.title.startswith(pattern)]
        filtered_movies.sort()

        print("[" + ", ".join(filtered_movies) + "]")

    def filter_movies_by_date(self, ineq, n):
        filtered_movies = []
        for i, movie in enumerate(self.movies):
            date = movie.date

            if ineq == ">=" and date >= n:
                filtered_movies.append(str(i))
            elif ineq == ">" and date > n:
                filtered_movies.append(str(i))
            elif ineq == "<=" and date <= n:
                filtered_movies.append(str(i))
            elif ineq == "<" and date < n:
                filtered_movies.append(str(i))
            elif ineq == "=" and date == n:
                filtered_movies.append(str(i))

        filtered_movies.sort()

        print("[" + ", ".join(filtered_movies) + "]")


manager = MovieManager()

manager.add_movie("Movie 1", "2022", "1080p")
manager.rem_movie(0)
manager.add_cast("John Doe")
manager.rem_cast(0)
manager.show_movie(0)
manager.show_cast(0)
manager.link_cast_to_movie(0, 0)
manager.filter_movies_by_title("The")
manager.filter_movies_by_date(">=", 2022)
