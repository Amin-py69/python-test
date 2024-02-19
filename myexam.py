


class Film:
    def __init__(self, title, date, quality):
        self.title = title
        self.date = date
        self.quality = quality
        self.actors = []

    def add_movie(self, title, date, quality):

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
