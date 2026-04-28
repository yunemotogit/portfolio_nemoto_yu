class Bird:
    def __init__(self):
        self.song = "piyo"

    def change_song_(self,song):
        self.song = song
    
    def show_song(self):
        print(self.song)
        self.change_song_("koko")
        print(self.song)

Bird().show_song()


    
        