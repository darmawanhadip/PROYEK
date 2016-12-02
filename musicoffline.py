class Music():
    def ButtonMusic(self):
        self.imageplay = Image.open('image\gplay.png')
        self.displayplay = ImageTk.PhotoImage(self.imageplay)
        self.buttonplay = Button(self.root, command=self.PlayMusicLogin, image=self.displayplay).place(x=70, y=355)
        self.imageresume = Image.open('image\gresume.png')
        self.displayresume = ImageTk.PhotoImage(self.imageresume)
        self.buttonresume = Button(self.root, command=self.UnpauseMusic, image=self.displayresume).place(x=110, y=355)
        self.imagepause = Image.open('image\gpause.png')
        self.displaypause = ImageTk.PhotoImage(self.imagepause)
        self.buttonpause = Button(self.root, command=self.PauseMusic, image=self.displaypause).place(x=150, y=355)
        self.imagestop = Image.open('image\gstop.png')
        self.displaystop = ImageTk.PhotoImage(self.imagestop)
        self.buttonstop = Button(self.root, command=self.StopMusic, image=self.displaystop).place(x=190,y=355)
    def ButtonMusicMainMenu(self):
        self.imageplay = Image.open('image\gplay.png')
        self.displayplay = ImageTk.PhotoImage(self.imageplay)
        self.buttonplay = Button(self.root, command=self.PlayMusicMainMenu, image=self.displayplay).place(x=70, y=370)
        self.imageresume = Image.open('image\gresume.png')
        self.displayresume = ImageTk.PhotoImage(self.imageresume)
        self.buttonresume = Button(self.root, command=self.UnpauseMusic, image=self.displayresume).place(x=110, y=370)
        self.imagepause = Image.open('image\gpause.png')
        self.displaypause = ImageTk.PhotoImage(self.imagepause)
        self.buttonpause = Button(self.root, command=self.PauseMusic, image=self.displaypause).place(x=150, y=370)
        self.imagestop = Image.open('image\gstop.png')
        self.displaystop = ImageTk.PhotoImage(self.imagestop)
        self.buttonstop = Button(self.root, command=self.StopMusic, image=self.displaystop).place(x=190, y=370)
    def ButtonMusicAdmin(self):
        self.imageplay = Image.open('image\gplay.png')
        self.displayplay = ImageTk.PhotoImage(self.imageplay)
        self.buttonplay = Button(self.root, command=self.PlayMusicAdmin, image=self.displayplay).place(x=70, y=370)
        self.imageresume = Image.open('image\gresume.png')
        self.displayresume = ImageTk.PhotoImage(self.imageresume)
        self.buttonresume = Button(self.root, command=self.UnpauseMusic, image=self.displayresume).place(x=110, y=370)
        self.imagepause = Image.open('image\gpause.png')
        self.displaypause = ImageTk.PhotoImage(self.imagepause)
        self.buttonpause = Button(self.root, command=self.PauseMusic, image=self.displaypause).place(x=150, y=370)
        self.imagestop = Image.open('image\gstop.png')
        self.displaystop = ImageTk.PhotoImage(self.imagestop)
        self.buttonstop = Button(self.root, command=self.StopMusic, image=self.displaystop).place(x=190, y=370)
    def ButtonMusicPlay(self):
        self.imageplay = Image.open('image\gplay.png')
        self.displayplay = ImageTk.PhotoImage(self.imageplay)
        self.buttonplay = Button(self.root, command=self.PlayMusicGame, image=self.displayplay).place(x=140, y=355)
        self.imageresume = Image.open('image\gresume.png')
        self.displayresume = ImageTk.PhotoImage(self.imageresume)
        self.buttonresume = Button(self.root, command=self.UnpauseMusic, image=self.displayresume).place(x=180, y=355)
        self.imagepause = Image.open('image\gpause.png')
        self.displaypause = ImageTk.PhotoImage(self.imagepause)
        self.buttonpause = Button(self.root, command=self.PauseMusic, image=self.displaypause).place(x=220, y=355)
        self.imagestop = Image.open('image\gstop.png')
        self.displaystop = ImageTk.PhotoImage(self.imagestop)
        self.buttonstop = Button(self.root, command=self.StopMusic, image=self.displaystop).place(x=260, y=355)
    def PlayMusicLogin(self):
        mixer.init()
        mixer.music.load('sound\musiclogin.mp3')
        mixer.music.play()
        self.cekmusic=1
    def PlayMusicMainMenu(self):
        mixer.init()
        mixer.music.load('sound\musicmenu.mp3')
        mixer.music.play()
        self.cekmusic = 1
    def PlayMusicGame(self):
        mixer.init()
        mixer.music.load('sound\musicgame.mp3')
        mixer.music.play()
        self.cekmusic = 1
    def PlayMusicAdmin(self):
        mixer.init()
        mixer.music.load('sound\musicadmin.mp3')
        mixer.music.play()
        self.cekmusic = 1
    def PauseMusic(self):
        mixer.music.pause()
        self.cekmusic = 1
    def UnpauseMusic(self):
        mixer.music.unpause()
        self.cekmusic = 1
    def StopMusic(self):
        mixer.music.stop()
        self.cekmusic = 1 # ##CLASS UNTUK
