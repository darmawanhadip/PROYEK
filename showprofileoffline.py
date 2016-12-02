class Profile(Music,Pintas):
    def __init__(self, root, title, usr):
        self.root = root
        self.root.title(title)
        self.root.geometry('300x420+450+150')
        self.root.configure(background='gray')
        self.tempusr = usr
        Pintas.bg(self)
        self.imageback = Image.open('image\gback.png')
        self.displayback = ImageTk.PhotoImage(self.imageback)
        self.buttonback = Button(self.root, text='Back', command=self.uprofile, image=self.displayback).place(x=250, y=10)
        self.labelProfile = Label(self.root, text='Your Profile', fg='blue', font=("Helvetica", 14), bg='black').place(x=10,y=50)

        c.execute('''SELECT name FROM user WHERE username = ?''', (usr,))
        for row in c.fetchone():
            self.tempname = str(row)
        self.labelname = Label(self.root, text='Name : '+self.tempname, fg='white', font=("Helvetica", 12), bg='black').place(x=10,y=75)

        c.execute('''SELECT age FROM user WHERE username = ?''', (usr,))
        for row in c.fetchone():
            self.tempage = str(row)
        self.labelage = Label(self.root, text='Age : '+self.tempage, fg='white', font=("Helvetica", 12), bg='black').place(x=10,y=100)

        c.execute('''SELECT bio FROM user WHERE username = ?''', (usr,))
        for row in c.fetchone():
            self.tempbio = str(row)
        self.labelbio = Label(self.root, text='Bio : '+self.tempbio, fg='white', font=("Helvetica", 12), bg='black').place(x=10,y=125)

        c.execute('''SELECT highscore FROM user WHERE username = ?''', (usr,))
        for row in c.fetchone():
            self.tempscore0 = row
        self.labelhighscore = Label(self.root, text='Highscore : '+str(self.tempscore0), fg='white', font=("Helvetica", 12),bg='black').place(x=10, y=150)
        self.buttoneditprofile = Button(self.root, text='Edit Profile', command=self.eprofile, width='15').place(x=10,y=185)

        Music.ButtonMusicMainMenu(self)
    def eprofile(self):
        uspr = self.tempusr
        self.root.destroy()
        self.eprofile = Tk()
        self.app = EditProfile(self.eprofile, 'Edit Profile', uspr)
        self.eprofile.deiconify()
    def uprofile(self):
        uspr = self.tempusr
        self.root.destroy()
        self.menu = Tk()
        self.app = Main_Menu(self.menu, 'Main_Menu', uspr)
        self.menu.deiconify()
