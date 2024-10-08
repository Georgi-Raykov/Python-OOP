from Spoopify.song import Song


class Album:

    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):

        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        elif any([x.name == song.name for x in self.songs]):
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                if not self.published:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
                else:
                    return "Cannot remove songs. Album is published."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):

        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {''.join(song.get_info())}\n"
        return result
