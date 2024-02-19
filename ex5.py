movies = []
actors = []
movie_id = 0


def add_movie(title, date, quality):
    global movie_id

    if len(title) > 20:
        print("Invalid title")
        return
    if not (1888 <= int(date) <= 2024):
        print("Invalid date")
        return
    if quality not in ['720p', '1080p', '4K']:
        print("Invalid quality")
        return

    movie = {'id': movie_id, 'title': title, 'date': date, 'quality': quality, 'actors': []}
    movies.append(movie)
    movie_id += 1

    print(f"Added successfully {movie['id']}")


add_movie("Movie 1", "2022", "1080p")


def rem_movie(movie_id):
    global movies

    for movie in movies:
        if movie['id'] == movie_id:
            movies.remove(movie)
            print(f"Removed successfully {movie_id}")
            return

    print("Invalid movie id")


rem_movie(0)


def add_cast(name):
    global actors

    if len(name) > 20 or not name.isalpha():
        print("Invalid name")
        return

    cast_id = len(actors)
    actors.append(name)

    print(f"Added successfully {cast_id}")


add_cast("John Doe")


def rem_cast(cast_id):
    global actors

    if cast_id >= len(actors):
        print("Invalid cast id")
        return

    actors.pop(cast_id)
    print(f"Removed successfully {cast_id}")


rem_cast(0)


def show_movie(movie_id):
    global movies, actors

    if movie_id >= len(movies):
        print("Invalid movie id")
        return

    movie = movies[movie_id]
    title = movie['title']
    date = movie['date']
    quality = movie['quality']
    cast_ids = movie['cast_ids']
    casts = [actors[cast_id] for cast_id in cast_ids]

    print(f"{{title:\"{title}\", date:\"{date}\", quality:\"{quality}\", casts:{casts}}}")


show_movie(0)


def show_cast(cast_id):
    global movies, actors

    if cast_id >= len(actors):
        print("Invalid cast id")
        return

    actor = actors[cast_id]
    name = actor
    movie_ids = [str(i) for i, movie in enumerate(movies) if cast_id in movie['cast_ids']]

    print(f"{{name:\"{name}\", movies:{movie_ids}}}")


show_cast(0)


def link_cast_to_movie(cast_id, movie_id):
    global movies, actors

    if cast_id >= len(actors):
        print("Invalid cast id")
        return

    if movie_id >= len(movies):
        print("Invalid movie id")
        return

    movie = movies[movie_id]
    cast_ids = movie['cast_ids']

    if cast_id in cast_ids:
        print("Already linked")
        return

    cast_ids.append(cast_id)
    print(f"Successfully linked {cast_id} to {movie_id}")


link_cast_to_movie(0, 0)


def filter_movies_by_title(pattern):
    global movies

    filtered_movies = [str(i) for i, movie in enumerate(movies) if movie['title'].startswith(pattern)]
    filtered_movies.sort()

    print("[" + ", ".join(filtered_movies) + "]")


filter_movies_by_title("The")


def filter_movies_by_date(ineq, n):
    global movies

    filtered_movies = []
    for i, movie in enumerate(movies):
        date = movie['date']

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


filter_movies_by_date(">=", 2022)


def filter_movies_by_quality(pattern):
    global movies

    filtered_movies = [str(i) for i, movie in enumerate(movies) if movie['quality'] == pattern]
    filtered_movies.sort()

    print("[" + ", ".join(filtered_movies) + "]")


filter_movies_by_quality("HD")
