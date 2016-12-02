class Login(Music,Pintas):
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry('300x420+450+150')
        Music.PlayMusicLogin(self)
        #self.root.configure(background='black')
        Pintas.bg(self)
        self.labelspace = Label(self.root, bg='black').pack()
        self.imagelogo = Image.open('image\logo.png')
        self.displaylogo = ImageTk.PhotoImage(self.imagelogo)
        self.labellogo = Label(self.root, image=self.displaylogo, bg='black').pack()
        self.labelusername = Label(self.root, text='Username: ', bg='black', fg='white').pack()
        self.stringusername = StringVar()
        self.entryusername = Entry(self.root, textvariable=self.stringusername).pack()
        self.labelpassword = Label(self.root, text='Password: ', bg='black', fg='white').pack()
        self.stringpassword = StringVar()
        self.entrypassword = Entry(self.root, textvariable=self.stringpassword, show='*').pack()
        self.labelspace = Label(self.root, bg='black').pack()
        self.imagebuttonlogin = Image.open('image\gbuttonlogin.png')
        self.displaybuttonlogin = ImageTk.PhotoImage(self.imagebuttonlogin)
        self.buttonlogin = Button(self.root, command=self.Login_menu, image=self.displaybuttonlogin, width='120', height='20').pack()
        self.labelspace = Label(self.root, bg='black').pack()
        self.imagebuttonregister = Image.open('image\gbuttonregister.png')
        self.displayregister = ImageTk.PhotoImage(self.imagebuttonregister)
        self.buttonregister = Button(self.root, command=self.Register_menu, image=self.displayregister, width='120', height='20').pack()

        Music.ButtonMusic(self)
    def Login_menu(self):
        user_name = self.stringusername.get()
        user_pass = self.stringpassword.get()
        if user_name == '' or user_pass == '':
            tkMessageBox.showwarning(title="Error!", message="Empty Username / Password")
        elif user_name == 'admin' and user_pass == 'admin':
            self.root.destroy()
            self.admininsert = Tk()
            self.app = AdminInsert(self.admininsert,'Insert Quiz')
            self.admininsert.deiconify()
        else:
            sql = "SELECT * FROM USER \
                    WHERE USERNAME = '%s' AND PASSWORD = '%s'" % (user_name,user_pass)
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if results:
                    self.root.destroy()
                    self.menu = Tk()
                    self.app = Main_Menu(self.menu, 'Main Menu', user_name)
                    self.menu.deiconify()
                else:
                    tkMessageBox.showwarning(title="Error !", message="Wrong Username / Password")
            except:
                print "Error: unable to fecth data"
    def Register_menu(self):
        self.root.destroy()
        self.register = Tk()
        self.app = Register(self.register, 'Register')
        self.register.deiconify()
