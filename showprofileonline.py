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

        sql = "SELECT NAME FROM USER \
                        WHERE USERNAME = '%s'" % (usr)
        try:
            cursor.execute(sql)
            for row in cursor.fetchone():
                self.tempname = str(row)
        except:
            print "Error: unable to fecth data"

        self.labelname = Label(self.root, text='Name : '+self.tempname, fg='white', font=("Helvetica", 12), bg='black').place(x=10,y=75)

        sql = "SELECT AGE FROM USER \
                    WHERE USERNAME = '%s'" % (usr)
        try:
            cursor.execute(sql)
            for row in cursor.fetchone():
                self.tempage = str(row)
        except:
            print "Error: unable to fecth data"

        self.labelage = Label(self.root, text='Age : '+self.tempage, fg='white', font=("Helvetica", 12), bg='black').place(x=10,y=100)

        sql = "SELECT BIO FROM USER \
                WHERE USERNAME = '%s'" % (usr)
        try:
            cursor.execute(sql)
            for row in cursor.fetchone():
                self.tempbio = str(row)
        except:
            print "Error: unable to fecth data"

        self.labelbio = Label(self.root, text='Bio : '+self.tempbio, fg='white', font=("Helvetica", 12), bg='black').place(x=10,y=125)

        sql = "SELECT HIGHSCORE FROM USER \
                    WHERE USERNAME = '%s'" % (usr)
        try:
            cursor.execute(sql)
            for row in cursor.fetchone():
                self.tempscore0 = row
        except:
            print "Error: unable to fecth data"

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
