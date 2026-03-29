class Song: # Class attributes shared by all Song objects
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level tracking whenever a new song is created
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    @classmethod
    def add_song_to_count(cls):
        # Increase total number of Song objects by 1
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre only if it is not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)

    def add_to_genres(self):
        # Pass this song's genre into the class-level genre tracker
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist only if not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    def add_to_artists(self):
        # Pass this song's artist into the class-level artist tracker
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increase count for this genre, or create it if missing
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    def add_to_genre_count(self):
        # Update the count for this song's genre
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        # Increase count for this artist, or create it if missing
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    def add_to_artists_count(self):
        # Update the count for this song's artist
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1