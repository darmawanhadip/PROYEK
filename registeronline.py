class Register(Music,Pintas):
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry('300x420+450+150')
        #self.root.configure(background='gray')
        Pintas.bg(self)
        self.labelspace = Label(self.root, bg='black').pack()
        self.labelRegister = Label(self.root, text='REGISTER ACCOUNT', fg='blue', font=("Helvetica", 16), bg='black').pack()
        self.labelspace = Label(self.root, bg='black').pack()
        self.labelname = Label(self.root, text='Name: ', bg='black', fg='white').pack()
        self.stringname = StringVar()
        self.entryname = Entry(self.root, textvariable=self.stringname).pack()
        self.labelage = Label(self.root, text='Age: ', bg='black', fg='white').pack()
        self.intage = StringVar()
        self.entryage = Entry(self.root, textvariable=self.intage).pack()
        self.labelusername = Label(self.root, text='Username: ', bg='black', fg='white').pack()
        self.stringusername = StringVar()
        self.entryusername = Entry(self.root, textvariable=self.stringusername).pack()
        self.labelpassword = Label(self.root, text='Password: ', bg='black', fg='white').pack()
        self.stringpassword = StringVar()
        self.entrypassword = Entry(self.root, textvariable=self.stringpassword, show='*').pack()
        self.labelspace = Label(self.root, bg='black').pack()
        self.imageregister = Image.open('image\gbuttonregister.png')
        self.displayregister = ImageTk.PhotoImage(self.imageregister)
        self.buttonregister = Button(self.root, image=self.displayregister, command=self.Register_menu, width='120',height='20').pack()
        self.labelspace = Label(self.root, bg='black').pack()
        self.imageback = Image.open('image\gbuttonback.png')
        self.displayback = ImageTk.PhotoImage(self.imageback)
        self.buttonback = Button(self.root, image=self.displayback, command=self.Login_menu, width='120', height='20').pack()

        Music.ButtonMusic(self)
    def Register_menu(self):
        name_person = self.stringname.get()
        user_name = self.stringusername.get()
        user_pass = self.stringpassword.get()
        user_age = self.intage.get()
        user_bio = 'This is my BIO'
        user_hs = 0
        user_maxcat = 5
        if name_person == '' or user_name == '' or user_pass == '' or user_age == 0:
            tkMessageBox.showwarning(title="Error !", message="Empty Name/Age/Username/Password")
        else:
            #c.execute("SELECT * FROM USER WHERE USERNAME = ?", (user_name,))

            sql = "SELECT * FROM USER \
                    WHERE USERNAME = '%s'" % (user_name)

            cursor.execute(sql)
            results = cursor.fetchall()
            if results:
                tkMessageBox.showwarning(title="Error !", message="Username Already")
            else:
                # c.execute("INSERT INTO user (username, password, name, age, bio, highscore, maxcategory) VALUES (?,?,?,?,?,?,?)",
                # (user_name, user_pass, name_person, user_age, user_bio,user_hs, user_maxcat,))
                # conn.commit()

                sql = "INSERT INTO USER(USERNAME, PASSWORD, NAME, \
                                        AGE, BIO, HIGHSCORE, MAXCATEGORY) \
                                            VALUES ('%s', '%s', '%s', '%d', '%s', '%d', '%d' )" % \
                      (user_name, user_pass, name_person, int(user_age), user_bio, int(user_hs), int(user_maxcat))
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()

                tkMessageBox.showwarning(title="SUCCESS", message="Your Register Success")
                self.root.destroy()
                self.login = Tk()
                self.app = Login(self.login, 'Login')
                self.login.deiconify()
    def Login_menu(self):
        self.root.destroy()
        self.login = Tk()
        self.app = Login(self.login, 'Login')
        self.login.deiconify()
