import customtkinter

App = customtkinter.CTk()

class Button_UI():
    def __init__(self, master, text, font, wight, height, x_pos, y_pos):
        self.button = customtkinter.CTkButton(master=master, text=text, font=font, width=wight, height=height)
        self.button.place(x=x_pos, y=y_pos)

def App_Project(Name):
    App.geometry("1500x800")
    App.title(f"{Name}")
    App.resizable(False, False)



    App.mainloop()