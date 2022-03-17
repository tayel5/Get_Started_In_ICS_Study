class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

time = Song(["Do you have the time",
                 "To listen to me whine",
                 "about python and C# all at once"])

plague = Song(["Ring a round the rosies",
                   "A pocket full of posies"])


time.sing_me_a_song()

plague.sing_me_a_song()