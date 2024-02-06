def create_login_page(self):
    self.login_frame = ttk.Frame(self.root)
    self.login_frame.grid(row=0, column=0, padx=20, pady=20)
    # center the login frame
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_columnconfigure(0, weight=1)
    ttk.Label(self.login_frame, text="Login to BingDrive", font=('Helvetica', 16, 'bold')).grid(row=0, column=0,
                                                                                                columnspan=2, pady=10)
    tk.Label(self.login_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
    self.name_entry = ttk.Entry(self.login_frame)
    self.name_entry.grid(row=1, column=1, pady=5)

    ttk.Label(self.login_frame, text="Level:").grid(row=2, column=0, sticky=tk.W, pady=5)
    self.level_entry = ttk.Entry(self.login_frame)
    self.level_entry.grid(row=2, column=1, pady=5)

    ttk.Label(self.login_frame, text="Matric Number:").grid(row=3, column=0, sticky=tk.W, pady=5)
    self.matric_number_entry = ttk.Entry(self.login_frame)
    self.matric_number_entry.grid(row=3, column=1, pady=5)

    ttk.Label(self.login_frame, text="Department:").grid(row=4, column=0, sticky=tk.W, pady=5)
    self.department_entry = ttk.Entry(self.login_frame)
    self.department_entry.grid(row=4, column=1, pady=5)

    ttk.Button(self.login_frame, text="Login", command=self.login).grid(row=5, column=0, columnspan=2, pady=10)


def login(self):
    name = self.name_entry.get()
    level = self.level_entry.get()
    matric_number = self.matric_number_entry.get()
    department = self.department_entry.get()

    self.current_user = User(name, level, matric_number, department)

    # Destroy the login frame and create the main app window
    self.login_frame.destroy()
    self.create_main_app()
