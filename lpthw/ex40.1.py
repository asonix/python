#!/usr/bin/env python3

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

t = Song(["We're all living in america",
          "america",
          "wundebar"])

t.sing_me_a_song()

lyrics = ["I warned you",
          "about stairs,",
          "bro"]

u = Song(lyrics)

u.sing_me_a_song()
