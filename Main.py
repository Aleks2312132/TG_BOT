from customtkinter import *
import customtkinter
import telebot

#other Code
import Save

#color
Color_Base = "#2E8B57"
Color_Haver = "#006400"
#other
Bot_ID = str
Name_Project = str
Project_index = int
Name_File = f"{Name_Project}{Project_index}"
#File = open(f"File/{Name_File}.txt", mode="r+", encoding="utf-8")

class Button():
    def __init__(self, master, text, height, wight, corner_radius, comand, x_pos, y_pos):
        self.Button = customtkinter.CTkButton(master=master, text=text, corner_radius=corner_radius, fg_color=Color_Base, hover_color=Color_Haver, width=wight, height=height, command=comand)
        self.Button.place(x=x_pos, y=y_pos)
class Label():
    def __init__(self, master, text, font, x_pos, y_pos, color):
        self.Label = customtkinter.CTkLabel(master=master, text=text, font=font, bg_color=color)
        self.Label.place(x=x_pos, y=y_pos)
class App():
    def __init__(self, Name, Logo, x, y, resize):
        self.Window = customtkinter.CTk()
        self.Window.geometry(f"{x}x{y}")
        self.Window.title(f"{Name}")
        self.Window.resizable(resize, resize)
        self.Window.iconbitmap(f"Disign\\{Logo}.ico")
        self.Window.mainloop()

New_Send_Messange_app = App("New_Send_Messange_app", "TGK-Logo", 400, 400, False)
Start_Function_Window_app = App("/Start settings", "TGK-Logo", 1500, 800, False)
Project_App = App("/Start settings", "TGK-Logo", 1500, 800, False)
def find_Bot_id():
    pass
    #lines = File.readlines()
    #for line in lines:
    #    Id_Str = line.find(":")
    #    Bot_ID = Bot_ID[Id_Str + 1, -1]
    #    print(Bot_ID)
    #Project_Main(Name_Project, Project_index)

def New_Send_Messange():
    New_Send_Messange_app.geometry("400x400")
    New_Send_Messange_app.title("New Send Messange")

    Text_Switch = customtkinter.CTkCheckBox(master=New_Send_Messange_app, text="Send Text", fg_color=Color_Base, hover_color=Color_Haver, onvalue=True, offvalue=False) #comand
    Text_Switch.place(x=10, y=10)
    def Send_Settings():
        Active_Send_Text = Text_Switch.get()
        print(Active_Send_Text)

    Button_Save = customtkinter.CTkButton(master=New_Send_Messange_app, text="Save and Quit", fg_color=Color_Base, hover_color=Color_Haver, height=35, width=380, command=Send_Settings()).place(x=10, y=350)

    New_Send_Messange_app.mainloop()

def Window_def_Start():
    #Text_Print_Chat_type = customtkinter.CTkLabel(master=Start_Function_Window_app, text="Type start send message:", font=font).place(x=10, y=75)
    #Button_Save = customtkinter.CTkButton(Start_Function_Window_app, command=Save, text="Save", font=font, corner_radius=150, height=35, width=910, fg_color="#00afe6").place(x=570, y=740)
    #master, text, font, height, wight, corner_radius, comand, x_pos, y_pos
    Text_Catalog = Button(Start_Function_Window_app, "/Start settings", 50, 50, 10, 650, 7)
    Button_New_Send = Button(Start_Function_Window_app, "New send messange a /start", 35, 1480, 10, New_Send_Messange, 10, 65)

    #OptionMenu = customtkinter.CTkOptionMenu(master=Start_Function_Window_app, height=35, width=1000, font=font, dropdown_font=font, values=["Message: Text", "Message: Foto", "Message: Video", "Message: File"], fg_color="#00afe6").place(x=450, y=75)
    Button_Close_Start_Panel = Button(Start_Function_Window_app, "Back", 35, 35, 10, 10, 10)
    Start_Function_Window_app.mainloop()
    def Active_Text_Send_Massage():
        Input_Send_Text = customtkinter.CTkTextbox(master=Start_Function_Window_app, height=50, width=550).place(x=100, y=100)


def Window_Id_Bot():
    Id_Input = customtkinter.CTkInputDialog(text="ID-Bot", button_fg_color=Color_Base, button_hover_color=Color_Haver, title="Input Id-Bot")
    Id_Input.iconbitmap(default="Disign\TGK-Logo.ico")
    Bot_Id = Id_Input.get_input()
    if len(Bot_Id) == 47:
        Bot_ID = Bot_Id
        #line = File.readline(0)
        #i = line.find(":")
        #print(i)
        #File.write(f"Bot_Id:{Bot_ID}\n")
    else:
        Window_Id_Bot()

def Save_info():
    pass
def Settings_Window():
    pass

def Project_Main():
    font = customtkinter.CTkFont(family="MV-crooker", size=26)
    app = App("/Start settings", "TGK-Logo", 1500, 800, False)
    #load_Project()
    Name_App = Label(app, f"Telegram\nBot-Creater", 40, 50, "#2b2b2b")
    Personalization_Text_Down = Label(app, f"DenFaArt_Game", 3, 775, "#2b2b2b")
    Name_Project = Label(app, f"Project: lox", font, 895, 19, "#2b2b2b")
    Button_Settings = Button(app, "Settings", font, 35, 495, 15, Settings_Window, 30, 500)
    Button_Id_Bot = Button(app, "input ID-Bot", font, 35, 910, 15, Window_Id_Bot, 570, 75)
    Button_def_Start = Button(app, "/Start", font, 35, 910, 15, Window_def_Start, 570, 135)
    Button_New_def = Button(app, "New function", font, 35, 910, 15, Window_Id_Bot, 570, 195)
    Button_Save = Button(app, "Save", font, 10, 910, 15, Save_info(), 570, 740)

def Window_Id_Bot():
    Id_Input = customtkinter.CTkInputDialog(text="ID-Bot", button_fg_color=Color_Base, button_hover_color=Color_Haver, title="Input Id-Bot")
    Id_Input.iconbitmap(default="Disign\TGK-Logo.ico")
    Bot_Id = Id_Input.get_input()
    if len(Bot_Id) == 47:
        Bot_ID = Bot_Id
        #line = File.readline(0)
        # i = line.find(":")
        #print(i)
        #File.write(f"Bot_Id:{Bot_ID}\n")
    else:
        Window_Id_Bot()

def load_Project():
    #lines = File.readlines()
    pass

Save.load_Save()
#File.close()

#6598671793:AAEu28C3ifg2vmfU49fAR9IO0BZpzIRxzgg
#6799797880:AAFeNxGPwCEPni0bbyu11wwYt1fk4KSZK_o