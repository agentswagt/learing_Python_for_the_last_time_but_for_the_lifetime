import tkinter as tk
import platform
import sys
import os
import pandas as pd


def execute():
    
    class_number = s.get()

    if class_number == "1":
        Subject_name2 = "english"


        teacher = "Muhammad Gofran"
        ID = "6911096065"
        Password = "14280529"
    if class_number == "2":
        Subject_name2 = "english"

        teacher = "Rokan Jahangir"
        ID = "5953408143"
        Password = "14220529"
    if class_number == "3":
        teacher_image = "biology.jpeg"
        Subject_name2 = "biology"
        teacher = "Goury Prova Das"
        ID = "7419175762"
        Password = "3456"
    if class_number == "4":

        Subject_name2 = "ict"
        teacher = "Abdullah Al Maruf"
        ID ="8615434353"
        Password = "8Lttk8"
    if class_number == "5":
        Subject_name2 = "Bangla"
        teacher = "Halima Khanom"

        ID = "7522389093"
        Password = "ABA6uJ"
    if class_number == "6":
        Subject_name2 = "Bangla"
        teacher = "Sultana Ara Begum"

        ID = "3329293832"
        Password = "14280529"
    if class_number == "7":
        Subject_name2 = "physics"
        teacher = "MD. Mujibul Alam"

        ID = "7645869114"
        Password = "AbCd0123"       
    if class_number == "8":
        Subject_name2 = "highermath"
        teacher = "MD. Amanat Ali Khan"

        ID = "7216954315"
        Password = "45678"
    if class_number == "9":
        Subject_name2 = "chemistry"
        teacher = "Ramkrisna Dhar"

        ID = "3346504150"
        Password = "W2FPcA"
    Subject_name2 = Subject_name2.capitalize()


    from tkinter.constants import X


    def class_link_openner():
        platforms = platform.system()
        platforms = platforms.lower()
        
        link = "https://us04web.zoom.us/j/{}".format(ID)
        if platforms.startswith("lin"):
            
            os.system("google-chrome {}".format(link))
            
        if platforms.startswith("win"):
            os.system("start chrome {}".format(link))
            
            df=pd.DataFrame([Password])
            df.to_clipboard(index=False,header=False)
            lebel55 = tk.Label(hello, text= "[+] Password Copied ! Just Paste it when Appeared").place(x = 50, y=260) 



    hello = tk.Tk()
    hello.title("{} Details".format(Subject_name2))
    canvas = tk.Canvas(hello, height= 300, width=400)

    canvas.pack()
    label3 = tk.Label(hello, text= "[+] Subject Name: {}\n\n[+] Teacher Name: {}\n\n[+] ID: {}\n\n[+] Password: {}".format(Subject_name2, teacher, ID, Password)).place(x = 110, y = 50)

    button = tk.Button(hello, text = "Link!!", command = class_link_openner).place(x = 150, y = 180)

    hello.mainloop()



root = tk.Tk()

#window and visual
root.title("Class Link Generator")
canvas = tk.Canvas(root, height= 500, width=700)
canvas.pack()

s = tk.StringVar()
#I/O operation

label1 = tk.Label(root, text= "COPY:: ClickTwice", width=50, font="Courier", height="50").place(x = 100, y = 10)
#label_w = tk.Label(root, text= "Class Link Generator", width=50, font="Courier", height=50).place(x = 100, y = -420)
label2 = tk.Label(root, text= "Class Number: ").place(x = 100, y = 90)
class_number1 = tk.Entry(root, textvariable= s,  bd=5)

canvas.create_window(250, 100, window = class_number1)





label3 = tk.Label(root, text= "[1] English - Gofran\n\n[2] English - Rokon\n\n[3] Biology\n\n[4] ICT\n\n[5] Bangla - Halima Khanom\n\n[6] Bangla - Sultana Ara Begum\n\n[7] Physcis\n\n[8] Highermath\n\n[9] Chemistry").place(x = 130, y = 120)

button = tk.Button(root, text = "Link!!", command = execute).place(x = 150, y = 390)









root.mainloop()


