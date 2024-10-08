import customtkinter
import Save

class Button_UI():
    def __init__(self, master, text, font, height, wight, x_pos, y_pos):
        self.Button = customtkinter.CTkButton(master=master, font=font, text=text, width=wight, height=height)
        self.Button.place(x=x_pos, y=y_pos)

def App_Project_View():
    App = customtkinter.CTk()
    font = customtkinter.CTkFont("MV-crooker", 26)
    App.geometry("1500x800")
    App.title("lox")
    Button_Input_Id_Bot = Button_UI(App, "New Project", font, 35, 50, 1300, 15)
    Button_Delite_all_Project = Button_UI(App, "delite all project", font, 35, 150, 1010, 15)

    Save.load_Save()
    for i in range(len(Save.Name_list) // 2):
        button_name = f"Project_viewer_{i}"
        button = Project_viewer(f"{Save.Name_list[i]}", f"{Save.Index_list[i]}", "#323232", "Open", Project_App, 1440, 75, 35, Start_Y + i * 100, 75, 35, 1370, (Start_Y + i * 100) + 16, 45, (Start_Y + i * 100), 45, 35, 1140, (Start_Y + i * 100 + 16), "Dilite Project")
        globals()[button_name] = button
        button_list.append(button)


App.mainloop()
