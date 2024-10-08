import customtkinter

import Main
import Save

Color_Base = "#008000"
Color_Hover = "#006400"
File = open("File\\Save.txt", mode="r+", encoding="utf-8")
App = customtkinter.CTk()
button_list = []

class Project_Label:
    def __init__(self, master, width_label, height_label, label_x_pos, label_y_pos, text_button, width_button, height_button, button_x_pos, button_y_pos, Name, x_name_pos, y_name_pos):
        font = customtkinter.CTkFont(family="MV-crooker", size=26)
        self.label = customtkinter.CTkLabel(master=master, text="", width=width_label, height=height_label, bg_color="#383838")
        self.label.place(x=label_x_pos, y=label_y_pos)
        self.name_project = customtkinter.CTkLabel(master=master, text=f"{Name}", font=font, bg_color="#383838")
        self.name_project.place(x=x_name_pos, y=y_name_pos)
        def Open_Project():
            Main.App_Project(Name)
        self.button = customtkinter.CTkButton(master=master, font=font, text=text_button, width=width_button, height=height_button, bg_color="#383838", fg_color=Color_Base, hover_color=Color_Hover, command=Open_Project)
        self.button.place(x=button_x_pos, y=button_y_pos)

class Button_UI():
    def __init__(self, master, text, wight, height, x, y, comand):
        font = customtkinter.CTkFont(family="MV-crooker", size=26)
        self.Button = customtkinter.CTkButton(master=master, text=text, fg_color=Color_Base, hover_color=Color_Hover, width=wight, height=height, font=font, command=comand)
        self.Button.place(x=x, y=y)

def Project_View_App():
    App.resizable(False, False)
    App.geometry("1500x800")
    App.title("Project View")
    Save.load_Save()
    Name_list = Save.Name_list
    for i in range(len(Name_list)):
        Y_Spawn = 75 + (i * 100)
        #master, width_label, height_label, label_x_pos, label_y_pos, text_button, width_button, height_button, button_x_pos, button_y_pos
        button_name = f"Project_viewer_{i}"
        button = Project_Label(App, 1480, 75, 10, Y_Spawn, "Open", 50, 35, 1390, Y_Spawn + 15, f"{Save.Index_list[i]} -  {Name_list[i]}", 30, Y_Spawn + 18)
        globals()[button_name] = button
        button_list.append(button)

    Button_New_Project = Button_UI(App, "New Project", 50, 35, 1300, 15, New_project)
    Button_Delite_All_Project = Button_UI(App, "Delite All Project", 50, 35, 1010, 15, Dilete_All_Project)
    App.mainloop()

def New_project():
    font = customtkinter.CTkFont(family="MV-crooker", size=26)
    Input_Name = customtkinter.CTkInputDialog(text="Input Name", font=font, button_fg_color=Color_Base, button_hover_color=Color_Hover, title="Input Name New Project")
    Name_input = Input_Name.get_input()
    if Name_input not in Save.Name_list:
        Save.Save(Name_input)
        Main.App_Project(Name_input)
        App.destroy()
    else:
        New_project()

def Dilete_All_Project():
    File.truncate(0)
    button_list = []
    App.destroy()

Project_View_App()