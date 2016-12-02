class EditProfile(Music,Pintas):
    def __init__(self, root, title, usr):
        self.root = root
        self.root.title(title)
        self.root.geometry('300x420+450+150')
        self.tempusr = usr
        Pintas.bg(self)
        self.labelspace = Label(self.root, bg='black').pack()
        self.labelspace = Label(self.root, bg='black').pack()
        self.labelEdit = Label(self.root, text='EDIT PROFILE', fg='blue', font=("Helvetica", 16), bg='black').pack()

        c.execute('''SELECT name FROM user WHERE username = ?''', (usr,))
        for row in c.fetchone():
            self.tempname = str(row)
        self.labelname = Label(self.root, text='Name: ', bg='black', fg='white').pack()
        self.stringname = StringVar()
        self.stringname.set(self.tempname)
        self.entryname = Entry(self.root, textvariable=self.stringname).pack()

        c.execute('''SELECT age FROM user WHERE username = ?''', (usr,))
        for row in c.fetchone():
            self.tempage = str(row)
        self.labelage = Label(self.root, text='Age: ', bg='black', fg='white').pack()
        self.intage = IntVar()
        self.intage.set(self.tempage)
        self.entryage = Entry(self.root, textvariable=self.intage).pack()

        c.execute('''SELECT bio FROM user WHERE username = ?''', (usr,))
        for row in c.fetchone():
            self.tempbio = str(row)
        self.labelbio = Label(self.root, text='Bio: ', bg='black').pack()
        self.stringbio = StringVar()
        self.stringbio.set(self.tempbio)
        self.entrybio = Entry(self.root, textvariable=self.stringbio).pack()

        self.labelspace = Label(self.root, text='', bg='black').pack()
        self.buttonchange = Button(self.root, text='CHANGE', command=self.confirm_edit, width='16').pack()

        self.imageback = Image.open('image\gback.png')
        self.displayback = ImageTk.PhotoImage(self.imageback)
        self.buttonback = Button(self.root, command=self.back_profile, image=self.displayback).place(x=250, y=10)
        self.imagehome = Image.open('image\ghome.png')
        self.displayhome = ImageTk.PhotoImage(self.imagehome)
        self.buttonhome = Button(self.root, command=self.back_home, image=self.displayhome).place(x=20, y=10)

        Music.ButtonMusicMainMenu(self)
    def confirm_edit(self):
        uspr = self.tempusr
        name_person = self.stringname.get()
        user_age = self.intage.get()
        user_bio = self.stringbio.get()

        if name_person == '' or user_age == '' or user_bio == '':
            tkMessageBox.showwarning(title="Error !", message="Empty Name/Age/Bio")
        else:
            c.execute("UPDATE user SET name = ?, age = ?, bio = ? WHERE username = ?", (name_person,user_age,user_bio,uspr))
            conn.commit()
            tkMessageBox.showwarning(title="EDITING SUCCESS", message="Your Editing Success")
            self.root.destroy()
            self.uprofile = Tk()
            self.app = Profile(self.uprofile, 'Your Profile', uspr)
            self.uprofile.deiconify()
    def back_profile(self):
        uspr = self.tempusr
        self.root.destroy()
        self.uprofile = Tk()
        self.app = Profile(self.uprofile, 'Your Profile', uspr)
        self.uprofile.deiconify()
    def back_home(self):
        uspr = self.tempusr
        self.root.destroy()
        self.bhome = Tk()
        self.app = Main_Menu(self.bhome, 'Main_Menu', uspr)
        self.bhome.deiconify()
