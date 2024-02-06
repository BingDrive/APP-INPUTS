import customtkinter as CTk
def button_callback():
    print("button pressed")

app = CTk.CTk()
app.title("BingDrive")
app.geometry("800x600")
app._set_appearance_mode("light")


welcome_label = CTk.CTkLabel(app, text="WELCOME TO BINGDRIVE",
                             fg_color=("white","black"),
                             font=("Helvetica", 24),
                             text_color=("black", "white"))
welcome_label.pack(pady=20)

login_button = CTk.CTkButton(app, text="LOGIN",
                             command=button_callback,
                             corner_radius=32,
                             fg_color=("#C850C0","black"),
                             hover_color="#4158D0")
login_button.place(relx=0.5, rely=0.5, anchor="center")

book_ride_button = CTk.CTkButton(app, text="Book a Ride",
                                 width=140, height=28,
                                 corner_radius=150,
                                 fg_color=("#C850C0","black"),
                                 hover_color="#4158D0")
book_ride_button.place(relx=0.5, rely=0.5)
book_ride_button.pack(pady=20)

view_history_button = CTk.CTkButton(app, text="View Drive History",
                                    width=140,
                                    height=28,
                                    corner_radius=150,
                                    fg_color=("#C850C0","black"),
                                    hover_color="#4158D0")
view_history_button.place(relx=0.5, rely=0.5)
view_history_button.pack(pady=20)

view_map_button = CTk.CTkButton(app, text="View Map",
                                width=140,
                                height=28,
                                corner_radius=150,
                                fg_color=("#C850C0","black"),
                                hover_color="#4158D0")
view_map_button.place(relx=0.5, rely=0.5)
view_map_button.pack(pady=20)

app.mainloop()
